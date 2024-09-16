import pygame
import math
from typing import Tuple

def ease_out_expo(x: float) -> float:
    return 1 if x == 1 else 1 - math.pow(2, -10 * x)

class DraggableImage:
    def __init__(self, image_path, x, y, size: Tuple[int, int] | None = None):
        # image, size, and rect
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image.copy()
        if size is not None: self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.original_size = self.image.get_size()
        self.default_position = self.rect.center
        self.target_pos = self.rect.center

        # scale
        self.scale = 1.0
        self.prev_scale = 1.0
        self.default_scale = 1.0
        self.dragging_scale = 1.1
        self.scale_anim_start = 0
        self.scale_anim_duration = 600
        
        # zoom
        self.zoom_scale = 2.8
        self.zoomed = False
        self.unzoom = False

        # dragging
        self.mouse_down = False
        self.mouse_down_pos = self.rect.center # this is the position of the mouse when the card was first clicked on
        self.mouse_down_center = self.rect.center # this is the center of the IMAGE when it was first clicked on
        self.mouse_down_time = 0
        self.mouse_pos = (0, 0)
        self.dragging = False
        self.dragging_dist = 0
        
        # handle multiple card mouse downs
        self.awaiting_mouse_down = False
        
        self.drop_in_lane = -1
        self.on_dropped: function | None = None
        self.locked = False
        
    # converts a top-left coordinate into a center coordinate
    # used when verifying the default position is not the same in the pygame loop where it is
    # more desirable to use top-left coordinates instead of center
    def topleft_to_center(self, topleft: tuple[int, int]):
        return (
            topleft[0] + self.original_size[0] / 2,
            topleft[1] + self.original_size[1] / 2
        )

    # draws the image to the screen, using smoothscale to transform it
    def draw(self, screen: pygame.Surface):
        # Draw image on top
        screen.blit(pygame.transform.smoothscale(self.original_image, self.rect.size), self.rect)

    # animates the scale and adjusts the position to compensate for the scale
    def animate_scale_and_position(self, target_scale):
        t = pygame.time.get_ticks()
        elapsed = t - self.scale_anim_start
        progress = elapsed / self.scale_anim_duration
        eased = ease_out_expo(progress)
        scale_dif = abs(target_scale - self.prev_scale)
        eased_dif = scale_dif * eased

        if target_scale < self.prev_scale: eased_dif *= -1.0
        scale = self.prev_scale + eased_dif

        new_size = (
            self.original_size[0] * scale,
            self.original_size[1] * scale
        )

        old_center = (self.rect.center[0], self.rect.center[1])

        self.rect.width = new_size[0]
        self.rect.height = new_size[1]

        self.rect.centerx -= self.rect.center[0] - old_center[0]
        self.rect.centery -= self.rect.center[1] - old_center[1]

        self.scale = scale
        
    def prepare_anim(self):
        self.scale_anim_start = pygame.time.get_ticks()
        self.prev_scale = self.scale
        
    def handle_mouse_down(self, pos):
        # register mouse is down and its position
        self.mouse_down = True
        self.mouse_down_pos = (pos[0], pos[1])
        self.mouse_down_center = self.rect.center
        self.mouse_down_time = pygame.time.get_ticks()
        self.dragging_dist = 0

    def handle_event(self, event: pygame.event.Event):
        if self.locked: return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # flag as waiting to check if this card is valid for mouse down
                self.awaiting_mouse_down = True
                
            # disable the zoom if the card is currently zoomed in
            if self.zoomed:
                # set unzoom so it doesn't try to zoom again on mouse up
                self.unzoom = True
                self.zoomed = False
                
                # move card back to default position
                self.target_pos = self.default_position
                
            # start scale up animation
            self.prepare_anim()

        elif event.type == pygame.MOUSEBUTTONUP:
            # drop this card in a lane if possible
            if self.drop_in_lane != -1:
                print("dropping in lane " + str(self.drop_in_lane))
                self.default_position = self.topleft_to_center((
                    10 + self.drop_in_lane * 159,
                    460
                ))
                if self.on_dropped is not None: self.on_dropped()
                
            # move card back to default position
            self.target_pos = self.default_position
                
                
            # begin zooming if:
            #   - not unzooming
            #   - mouse is down
            #   - not dragged more than 50px
            #   - mouse has not been down for more than 500ms
            if pygame.time.get_ticks() - self.mouse_down_time < 500:
                if self.dragging_dist <= 50:
                    if not self.unzoom and self.mouse_down:
                        self.zoomed = True
                        self.target_pos = (400, 500)

            # set mouse down and dragging to false
            self.mouse_down = False
            self.dragging = False
            
            # reset unzoom so it can be zoomed again
            self.unzoom = False
            
            # update scale animation start time and previous scale
            self.prepare_anim()
            

        elif event.type == pygame.MOUSEMOTION:
            # do nothing if currently zoomed or unzooming
            if self.zoomed or self.unzoom: return
            
            if not self.dragging and self.mouse_down:
                # could start scale up animation here if desired? I prefer on mouse down though
                self.dragging = True

            if self.dragging:
                # update mouse pos
                self.mouse_pos = event.pos
                # update target position while dragging
                self.target_pos = (
                    self.mouse_down_center[0] + (event.pos[0] - self.mouse_down_pos[0]),
                    self.mouse_down_center[1] + (event.pos[1] - self.mouse_down_pos[1])
                )
                self.dragging_dist = math.dist(self.mouse_down_center, self.target_pos)

    def update(self):
        # drag animation multiplier
        multiplier = 0.15

        # calculate distance for each axis
        distance_to_target = (
            self.target_pos[0] - self.rect.centerx,
            self.target_pos[1] - self.rect.centery
        )
        
        # either floor or ceil the value, to make sure it can never round down to 0
        # if not rounded, you can get values like 0.4 or -0.4, which will never move the card by
        # the pixel, which means it never truly reaches the destination.
        distx = multiplier * distance_to_target[0]
        if distx < 0: distx = math.floor(distx)
        else: distx = math.ceil(distx)
        
        disty = multiplier * distance_to_target[1]
        if disty < 0: disty = math.floor(disty)
        else: disty = math.ceil(disty)
        
        # add the distance, mulitplied and rounded, to the current position
        self.rect.centerx += distx
        self.rect.centery += disty

        # zoom in
        if self.zoomed and self.scale < self.zoom_scale:
            self.animate_scale_and_position(self.zoom_scale)
            
        # scale up if mouse down / dragging
        elif not self.zoomed and not self.unzoom and self.mouse_down and self.scale < self.dragging_scale:
            self.animate_scale_and_position(self.dragging_scale)

        # scale down to default
        elif not self.zoomed and (self.unzoom or not self.mouse_down) and self.scale > self.default_scale:
            self.animate_scale_and_position(self.default_scale)

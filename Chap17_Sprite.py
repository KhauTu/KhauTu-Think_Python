gravity = 0.0001

class QueenSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0) # Start ball at top of its column
        self.y_velocity = 0 # with zero initial velocity

    def update(self):
        self.y_velocity += gravity # Gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity # Velocity moves the ball
        (target_x, target_y) = self.target_posn # Unpack the position
        dist_to_go = target_y - new_y_pos # How far to our floor?

        if dist_to_go < 0: # Are we under floor?
            self.y_velocity = -0.65 * self.y_velocity # Bounce
            new_y_pos = target_y + dist_to_go # Move back above floor
        self.posn = (x, new_y_pos) # to this new position.

    def draw(self, target_surface): # Same as before.
        target_surface.blit(self.image, self.posn)

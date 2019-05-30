class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def distance(self, target):
        """ Return the distance between myself and the target """
        dx = self.x - target.x
        dy = self.y - target.y
        dsquared = dx*dx + dy*dy
        result = dsquared**0.5
        return result

    def reflect_x(self):
        """ Returns a new Point,
        one which is the reflection of the point about the x-axis"""
        return Point(self.x, - self.y)

    def slope_from_origin(self):
        """  Returns the slope of the line joining the
        origin to the point """
        if self.x == 0:
            slope = "infinite"
        else:
            slope = self.y / self.x
        return slope

    def get_line_to(self, target):
        """ Return the two coefficients of y = ax + b (line through self and target)
        as a tuple of two values"""
        if (self.x - target.x) == 0:
            return "x = {0}".format(self.x)
        else:
            a = (self.y - target.y) / (self.x - target.x)
        b = self.y - a * self.x
        return "({0}, {1})".format(a, b)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

# Other statements outside the class continue below here.

p = Point(3, 4) # Instantiate an object of type Point
q = Point(5, 12) # Make a second point
r = p.halfway(q)

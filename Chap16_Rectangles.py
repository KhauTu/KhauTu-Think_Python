from Chap15 import *
import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    # Objects are mutable:
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self): # Diện tích
        return (self.width * self.height)
    
    def perimeter(self): # Chu vi
        return (2*(self.width + self.height))

    def flip(self):
        w = self.width
        h = self.height
        self.width = h
        self.height = w

    def contains(self, p):
        if (self.corner.x <= p.x < self.corner.x + self.width) and (self.corner.y <= p.y < self.corner.y + self.height):
            return True
        else:
            return False

    def collision_detect(self, rect):
        p1 = Point(rect.corner.x, rect.corner.y)
        p2 = Point(rect.corner.x + rect.width, rect.corner.y)
        p3 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
        p4 = Point(rect.corner.x, rect.corner.y + rect.height)
        return (self.contains(p1) or self.contains(p2) or self.contains(p3) or self.contains(p4))

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
# print("box: ", box)
# print("bomb: ", bomb)
'''
r = Rectangle(Point(10,5), 100, 50)
print(r)
r.grow(25, -10)
print(r)
r.move(-10, 10)
print(r)
'''
def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)
'''
p1 = Point(3, 4)
p2 = Point(3, 4)
print(same_coordinates(p1, p2))
'''
'''
import copy
p1 = Point(3, 4)
p2 = copy.copy(p1)
print(p1 is p2)
print(same_coordinates(p1, p2))
'''
'''
r = Rectangle(Point(0, 0), 10, 5)
print(r.area())
print(r.perimeter())
'''
'''
r = Rectangle(Point(100, 50), 10, 5)
print(r.width == 10 and r.height == 5)
r.flip()
print(r.width == 5 and r.height == 10)
'''
def test_suite():
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))
    g = Rectangle(Point(11, 6), 7, 7)
    test(not r.collision_detect(g))

test_suite()
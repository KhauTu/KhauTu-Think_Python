from math import sqrt
 
class Point:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
 
class Circle:
	def __init__(self, a, b, c):
		# line between a and b: s1 + k * d1
		s1 = Point((a.x + b.x)/2.0, (a.y + b.y)/2.0)
		d1 = Point(b.y - a.y, a.x - b.x)
		# line between a and c: s2 + k * d2
		s2 = Point((a.x + c.x)/2.0, (a.y + c.y)/2.0)
		d2 = Point(c.y - a.y, a.x - c.x)
		# intersection of both lines:
		# s1 + k * d1 == s2 + l * d2
		l = d1.x * (s2.y - s1.y) - d1.y * (s2.x - s1.x)
		l = l / (d2.x * d1.y - d2.y * d1.x)
		self.center = Point(s2.x + l * d2.x, s2.y + l * d2.y)
		dx = self.center.x - a.x
		dy = self.center.y - a.y
		self.radius = sqrt(dx * dx + dy * dy)
	def __repr__(self):
		return "Center: (%.2f, %.2f), Radius: %.2f" % (self.center.x, self.center.y, self.radius)
 
a = Point(9, 3) 
b = Point(8, 6) 
c = Point(0, 0) 
print(Circle(a, b, c)) 
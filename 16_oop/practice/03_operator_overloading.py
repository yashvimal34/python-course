class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point ((self.x + other.x), (self.y + other.y))
    
p1 = Point(23, 54)
p2 = Point(54, 56)

# p = p1.add(p2)
# print(p.__str__())

p3 = p1 + p2  # This is now works p1.__add__(p2)
print(p3)
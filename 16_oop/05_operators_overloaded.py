class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def print_point(self):
        return f"x is {self.x} and y is {self.y}"
    
    def __add__(self, p):
         return Point((self.x + p.x), (self.y + p.y))

p1 = Point(5, 8)
p2 = Point(8, 9)

# p = p1.sum(p2)  # Returns a new point which is sum of p1 and p2
p = p1 + p2 # We overloaded + operator by adding __add__ function
print(p.print_point())
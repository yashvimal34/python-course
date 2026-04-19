class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.1416 * self._radius * self._radius
    
c = Circle(5)
print(c.radius)
print(c.area)
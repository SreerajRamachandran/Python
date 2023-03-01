class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        self.area = self.length * self.breadth
        return self.area

    def perimeter(self):
        self.perimeter = 2 * self.length + self.breadth
        return self.perimeter

    def compare(self, other):
        if self.area == other.area:
            print(f"both are equal {self.area},{other.area}")
        elif self.area >= other.area:
            print(f"rec1 is large {self.area}")
        else:
            print(f"rec2 is large {other.area}")


rect1 = Rectangle(2, 4)
rect1.calculate_area()
rect2 = Rectangle(3, 4)
rect2.calculate_area()
print(rect1.compare(rect2))

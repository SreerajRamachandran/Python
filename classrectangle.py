class rectangle:
    area = 0
    perimeter = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width


def calc_area(self):
    self.area = self.length * self.width
    print("area is :", self.area)


def __it__(self, second):
    if self.area < second.area:
        return True
    else:
        return False


length1 = int(input("length1"))
width1 = int(input("width1"))

length2 = int(input("length2"))
width2 = int(input("width2"))
obj1 = rectangle(length1, width1)
obj2 = rectangle(length2, width2)
#obj1.calc_area()
#obj2.calc_area()
if obj1 < obj2:
    print("rectangle2 is large")
else:
    print("1 is large")

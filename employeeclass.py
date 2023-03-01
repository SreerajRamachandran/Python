class Employee:
    def __init__(self, empno, name, designation):
        self.empno = empno
        self.name = name
        self.designation = designation


class Qualification(Employee):
    def __init__(self, empno, name, designation, ugmark, pgmark, experience):
        super().__init__(empno, name, designation)
        self.ugmark = ugmark
        self.pgmark = pgmark
        self.experience = experience


class salary(Qualification):
    def __init__(self, empno, name, designation, ugmark, pgmark, experience):
        super().__init__(empno, name, designation, ugmark, pgmark, experience)

    def display_details(self):
        print(f"Employee no={self.empno}")
        print(f"Name={self.name}")
        print(f"Designation={self.designation}")
        print(f"PGmark={self.pgmark}")
        print(f"Ugmark={self.ugmark}")
        print(f"Experience={self.experience}")

    def compute_increment(self):
        if self.experience >= 10:
            increment = 10000
        elif self.experience >= 5:
            increment = 5000
        else:
            increment = 0

        if self.ugmark >= 80:
            increment += 5000

        if self.pgmark >= 80:
            increment += 10000

        return increment


emp1 = salary("E101", "John Doe", "Manager", 85, 90, 8)
emp1.display_details()
increment = emp1.compute_increment()
print(f"Increment: Rs. {increment}")

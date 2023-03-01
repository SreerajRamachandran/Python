class Time:

    def __init__(self, hour, minute, second):
        self.hr = hour
        self.min = minute
        self.sec = second

    def __add__(self, other):
        a_hr = self.hr + other.hr
        b_min = self.min + other.min
        c_sec = self.sec + other.sec
        if c_sec >= 60:
            b_min = c_sec % 60
            c_sec = b_min + c_sec // 60
        if b_min >= 60:
            a_hr = b_min % 60
            b_min = a_hr + b_min // 60
        print(f"total time = {a_hr} hrs : {b_min} min : {c_sec} sec")


t1 = Time(3,23,45)
t2 = Time(5,56,57)
t1 + t2

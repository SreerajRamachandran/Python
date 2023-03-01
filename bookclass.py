class Time:
    def __init__(self, hour, minute, second):
        self.hr = hour
        self.min = minute
        self.sec = second

    def __add__(self, other):
        total_hr = self.hr + other.hr
        total_min = self.min + other.min
        total_sec = self.sec + other.sec
        if total_sec > 60:
            total_min = total_min + total_sec // 60
            total_sec = total_sec % 60
        if total_min > 60:
            total_hr = total_hr + total_min // 60
            total_min = total_min % 60
        print(f"Total time={total_hr}hr:{total_min}min:{total_sec}sec")

t1 = Time(3, 23, 45)
t2 = Time(5, 56, 57)
total_time=t1 + t2

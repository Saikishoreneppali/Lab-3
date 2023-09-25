def add(a,b):
    return a+b
total = add(3, -1)
print(total)
import math as m
def calc_wheel_area(radius):
    area = m.pi * radius**2
    return area
wheel_radius = 0.2 # 0.2 meters
wheel_area = calc_wheel_area(wheel_radius)
print("The area of the wheel is", wheel_area)
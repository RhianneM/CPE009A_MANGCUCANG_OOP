import math

def angle_demo():
    angle = math.sin(math.pi/2)  # radians
    print(angle)  # sin(90°) = 1
    angle = math.sin(math.radians(90))  # convert degrees to radians
    print(angle)

angle_demo()

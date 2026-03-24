import math

def projectilemotion_solver(v, angle_deg):
    g = 9.8
    angle_rad = math.radians(angle_deg)
    R = (v**2 * math.sin(2*angle_rad)) / g
    h = (v**2 * (math.sin(angle_rad)**2)) / (2*g)
    return R, h

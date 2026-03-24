import math

def quadratic_solver(a, b, c, filename="quadratic_output.txt"):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"Equation: {a}x^2 + {b}x + {c}\nRoots: {x1}, {x2}\n"
        with open(filename, "a") as f:
            f.write(result + "\n")
        return x1, x2

def rightTriangle(sides):
    sides = sorted(sides)
    a, b, c = sides
    return (a**2 + b**2) == c**2
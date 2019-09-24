def angleType(m):
    if m < 90:
        return "acute"
    if m == 90:
        return "right"
    if m > 90 and m < 180:
        return "obtuse"
    if m == 180:
        return "striaght"
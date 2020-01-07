from itertools import permutations
def equationTemplate(values):
    groups = permutations(values, 4)
    for i in groups:
        print(i)
        a, b, c, d = i
        if a == b*c*d or a*b == c*d or a*b*c == d:
            return True
    return False
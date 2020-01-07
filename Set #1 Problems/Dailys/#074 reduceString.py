def reduceString(i):
    if i == "":
        return ""
    i = list(i)
    while i[0] == i[-1]:
        if len(i) <= 1:
            return ""
        i.pop(0)
        i.pop(-1)
    return "".join(i)
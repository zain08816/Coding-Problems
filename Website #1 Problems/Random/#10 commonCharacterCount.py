def commonCharacterCount(s1, s2):
    e = 0
    common = set(s1) & set(s2)
    print(common)
    for i in common:
        e += min(s1.count(i), s2.count(i))
    return e
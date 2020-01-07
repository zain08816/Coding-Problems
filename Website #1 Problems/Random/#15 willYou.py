def willYou(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    if loved and (not beautiful or not young):
        return True
    return False
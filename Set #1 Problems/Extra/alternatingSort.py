from collections import deque
def alternatingSort(a):
    a = deque(a)
    b = []
    
    for i in range(len(a)):
        if i%2 == 0:
            b.append(a.popleft())
        else:
            b.append(a.pop())

    return all(i < j for i, j in zip(b, b[1:])) 
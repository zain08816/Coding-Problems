def josephusProblem(n, k):
    if (n == 1):
        return 1
    else:
        return (josephusProblem(n-1, k) + k - 1) % n + 1
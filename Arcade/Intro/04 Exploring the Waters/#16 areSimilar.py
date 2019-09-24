def areSimilar(a, b):
    return sorted(b)==sorted(a) and sum([j!=k for j,k in zip(a,b)])<=2
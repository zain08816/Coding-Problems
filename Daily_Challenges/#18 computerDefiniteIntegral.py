from scipy.integrate import quad

def computeDefiniteIntegral(l, r, p):
    def f(x):
        out = 0
        for i in range(len(p)):
            out += p[i]*x**(i)
        return out
    print(f(2))
    integral = quad(f, l, r)
    return integral[0]
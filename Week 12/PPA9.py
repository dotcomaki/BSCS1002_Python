'''
Question's too long
'''

def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]

def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))

def h(x):
    return x ** 0.5

def pearson(X, Y):
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    num = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    den = (sum((X[i] - mean_X) ** 2 for i in range(n)) * sum((Y[i] - mean_Y) ** 2 for i in range(n))) ** 0.5
    return num / den

X = [float(x) for x in input().split()]
Y = [float(y) for y in input().split()]
print(f'{pearson(X, Y):.2f}')

def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)


def p(n, k):
    return f(n) / f(n - k)


def c(n, k):
    return p(n, k) / f(k)


# print(c(4, 2))
# print(p(4, 2))

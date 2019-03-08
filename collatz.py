from functools import reduce


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def collatz(n):
    if n == 1:
        return [1]
    elif even(n):
        return [n] + collatz(n // 2)
    elif odd(n):
        return [n] + collatz(n*3 + 1)


def compose2(f, g):
    return lambda x: f(g(x))


def compose(*functions):
    
    def id(x):
        return x
    
    return reduce(compose2, functions, id)


def collatz_pair(n):
    return collatz(n), n


def fst(x):
    return x[0]


collatz_pair_fst_len = compose(len, fst, collatz_pair)


if __name__ == '__main__':
    MAX = 5
    xs = range(1, MAX + 1)
    ys = map(collat_pair_fst_len, xs)
    for y in ys: print(y)

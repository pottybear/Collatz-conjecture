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


def head(x):
    return x[0]


def len_head_pair(xs):
    return len(xs), head(xs)


collatz_len_head_pair = compose(len_head_pair, collatz)


if __name__ == '__main__':
    MAX = 5
    xs = range(1, MAX + 1)
    ys = map(collatz_len_head_pair, xs)
    for y in ys: print(y)

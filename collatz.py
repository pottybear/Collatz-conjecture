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


def head(x):
    return x[0]


def len_head_pair(xs):
    return len(xs), head(xs)


collatz_len_head_pair = compose2(len_head_pair, collatz)


input_int = compose2(int, input)


if __name__ == '__main__':
    MAX = input_int('')
    xs = range(1, MAX+1)
    ys = map(collatz_len_head_pair, xs)
    print(max(ys))

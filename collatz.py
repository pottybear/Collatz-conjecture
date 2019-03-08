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


if __name__ == '__main__':
    input_int = compose(int, input)
    collatz_print = compose(print, collatz)
    
    n = input_int('')
    collatz_print(n)

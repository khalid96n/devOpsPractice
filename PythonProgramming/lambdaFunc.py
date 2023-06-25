def addition(a, b, c): return print(a+b+c)


addition(10, 20, 3)


def add1(n):
    return lambda a: a+n


newadd = add1(2)

print(newadd(4))

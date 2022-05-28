# stores in memory
def create_cubbes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

# doesn't store in memory, more memory efficient
def create_cubes_gen(n):
    for x in range(n):
        yield x**3

# memory efficient
def gen_fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

def simple_gen():
    for x in range(3):
        yield x

str = 'hello'

if __name__ == "__main__":
    for x in create_cubes_gen(10):
        print(x)

    # can still cast to a list
    cubes = list(create_cubes_gen(10))
    print(cubes)

    for x in gen_fib(15):
        print(x)

    for number in simple_gen():
        print(number)

    g = simple_gen()
    print(next(g))
    print(next(g))
    print(next(g))

    iter_s = iter(str)
    print(next(iter_s))

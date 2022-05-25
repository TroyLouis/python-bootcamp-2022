my_nums = [1,2,3,4,5]

def square(num):
    return num**2

def check_even(num):
    return num % 2 == 0

square = lambda num: num ** 2

evens = lambda num: num % 2 == 0

if __name__ == "__main__":
    print(list(map(square,my_nums)))
    print(list(filter(check_even, my_nums)))
    print(square(5))
    print(list(filter(lambda num: num % 2 == 0,my_nums)))

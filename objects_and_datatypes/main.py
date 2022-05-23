def integers():

    addition = 2 + 1
    print(addition)

    subtraction = 5 - 1
    print(subtraction)

    modulo = 5 % 3
    print(modulo)

    multiplication = 2 * 2
    print(multiplication)

    division = 9 / 5
    print(division)

    four_squared = 4 ** 2
    print(four_squared)

def variable_assignment():
    cat = "cat"
    a = 7

    print(a * 5)
    print((cat + " ") * 5)

def strings():
    #strings are immutable
    #start, stop, step for slicing

    hello = "hello world"
    random_string = "Hello \nmy \nname \nis \nTroy."
    print(hello)
    print(random_string)

    print(hello[0])
    print(hello[:3])
    print(hello[5:])

    lower = 'troy'
    upper = 'TROY'

    print(f'{lower} is lowercase until we call upper(), then it is {lower.upper()}.')
    print(f'{upper} is uppercase until we call lower(), then it is {upper.lower()}.')

    print(hello.split())

def lists():
    my_list = ['A',7,'bee', 'jam']
    print(my_list)

    my_list.append("Troy")
    print(my_list)

    my_list.pop()
    print(my_list)

    item = my_list.pop(2)
    print(item)
    print(my_list)

    new_list = [1, 9, 6, 15, 2]
    new_list.sort() # occurs in place
    print(new_list)
    new_list.reverse()
    print(new_list)


if __name__ == "__main__":

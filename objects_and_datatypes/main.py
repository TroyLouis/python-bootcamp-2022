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
    print(new_list[2:])

def dict():
    my_dict = {'troy': 900, 'greg': 222}
    print(my_dict['troy'])

    my_dict['troy'] = 50
    print(my_dict['troy'])

    my_dict['Sarah'] = 500
    print(my_dict)

    my_dict['Tracy'] = (1,2)
    print(my_dict['Tracy'])
    print(my_dict['Tracy'][1])

    new_dict = {'a': 100, 'b': 200, 'c': 300}
    print(new_dict.keys())
    print(new_dict.values())
    print(new_dict.items())
    print(new_dict.pop('a'))
    print(new_dict)

def tuples():
    #immutable
    t = (2, 4, 5, 5, 5, 5)
    print(t[-1])
    print(t.count(5))
    print(t.index(4))

def sets():
    #unordered unique elements
    set1 = set()
    print(type(set1))
    set1.add(500)
    set1.add(501)
    set1.add(501) #doesn't throw error but doesn't add it
    print(set1)

    my_list = [1,2,3,4,5,5,5,5,6,6,6,7,8,9,0,1,1,1]
    my_set = set(my_list)
    print(my_set)

def bool():

    print(1 > 2)
    print('a' == 'b')
    print('a' == 'a')
    print(5 > -2)

def io():
    my_file = open('myfile.txt')

if __name__ == "__main__":
    io()
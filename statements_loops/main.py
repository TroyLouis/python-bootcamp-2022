def if_func():
    location = "home"

    if location == "home":
        print(f'I am at {location}.')
    else:
        print("Not Home")

def while_loop():
    my_list = [1,2,3,4,5,6,7]
    even_list = []
    for number in my_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

def tuple_unpack():
    my_list = [(1,2),(3,4),(5,6)]
    for a,b in my_list:
        print(a)

def dict():
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    for key in d:
        print(key)
    for value in d.values():
        print(value)

    for key,value in d.items():
        print(type(key))
        print(type(value))
        print(key,value)

def iteration():
    x = 0
    while x < 5:
        print(x)
        x += 1
    else:
        print(f'x is not less than {x}')

def break_pass_continue():
    x = [1,2,3,5,9,55]
    for number in x:
        if number > 3:
            continue
        elif number > 8:
            break
        else:
            print(number)

def ranges():
    for num in range(5,21,3):
        print(num)

    count = [1,2,3,4,5,6,7]
    index = 0
    for number in count:
        print(f'The number is {number} at {index}.')
        index += 1

    for index,number in enumerate(count):
        print(index,number)

def operators():
    d = {'key': 123}
    print(123 in d.values())
    print('key' in d)

def list_comprehension():
    my_list = [num for num in range(0,11)]
    print(my_list)

    list_2 = [num * 3 for num in range(0,10) if num%2==0]
    print(list_2)

    temperatures = [23,32, 85, 65, 41, 10]
    cel_to_f = [((9/5)*temp + 32) for temp in temperatures]
    print(cel_to_f)

    #not very readable
    big_list = [x*y for x in [2,4,6] for y in [1,10,100]]
    print(big_list)

if __name__ == "__main__":
    list_comprehension()

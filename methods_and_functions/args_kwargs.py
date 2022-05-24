def myfunc(*args):
    print(args)
    for number in args:
        print(number)

def kwarg_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f'My favorite fruit is {kwargs["fruit"]}.')

def arg_kwarg(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like {args[0]} {kwargs["food"]}.')

def pick_even(*args):
    evens = []
    for number in args:
        if number % 2 == 0:
            evens.append(number)
    return evens

def skyline(word):
    sky = ''
    for i in range(0, len(word)):
        if i % 2 == 0:
            sky += word[i].upper()
        else:
            sky += word[i].lower()

    return sky

if __name__ == "__main__":
    print(skyline('hamster'))
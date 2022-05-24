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

if __name__ == "__main__":
    arg_kwarg(10,20,30,fruit='orange',bat='yes',food='hotdog')
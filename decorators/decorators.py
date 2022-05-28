def hello(name="Troy"):
    print("hello() executed")

    def greet():
        return '\t greet() inside hello'

    def welcome():
        return '\t welcome() inside hello'

    print(greet())
    print(welcome())
    print("end of hello()")

def cool():
    def super_cool():
        return "I am super cool"
    return super_cool

def new_decorator(original_function):
    def wrap_func():
        print('Some extra code before original function')
        original_function()
        print("Extra code, after the original function!")

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

@new_decorator
def func_decorated():
    print("I want to be decorated!")

if __name__ == "__main__":
    decorated_func = new_decorator(func_needs_decorator)
    decorated_func()

    func_needs_decorator()

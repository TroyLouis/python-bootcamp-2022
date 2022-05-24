def say_hello():
    print("hello")

def say_name(name='Troy'):
    print(f'{name}')

def add_nums(num1,num2):
    return num1 + num2

def check_even_list(num_list):
    evens = []
    odds = []
    for number in num_list:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    return (evens,odds)

if __name__ == "__main__":
    print(check_even_list([1,2,3,4,5,6,7,8,9]))

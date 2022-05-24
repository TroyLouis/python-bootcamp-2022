import random

def random_number(num1=0,num2=1000):
    return random.randint(num1,num2)

def check_divisible_5(number):
    return number % 5 == 0


if __name__ == "__main__":
    number = random_number()
    print(f'{number} divisible by 5: {check_divisible_5(number)}')
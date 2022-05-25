import math

def vol(rad):
    # Gets the volume of a sphere
        return (4/3 * math.pi * (rad ** 3))

def ran_check(num,low,high):
    #Check whether a numbber is in a range
    rng = list(range(low,high+1))
    if num in rng:
        return True
    return False

def unique_list(lst):
    #takes a list returns unique values in list
    return set(lst)

unique = lambda lst: set(lst)

def multiply(lst):
    total = 1
    for item in lst:
        total *= item
    return total

def palindrome(s):
    # Returns True if word is a Palindrome
    lst = list(s)
    for index in range(0,len(s)//2):
        if lst[index] == lst[-index-1]:
            pass
        else:
            return False
    return True

palindrome = lambda pal: pal == pal[::-1]

if __name__ == "__main__":
    print(vol(2))
    print(ran_check(100,1,100))
    print(unique_list([1,1,1,1,1,2,2,2,2,0]))
    print(unique([1,1,1,2,3,4,5,6,7,8,8]))
    print(multiply([1,1,1,5,6]))
    print(palindrome('1ssawawass1'))
    print(palindrome('1ssawabwass1'))
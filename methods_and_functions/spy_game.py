def spy_game(numbers):
    """
    :param numbers: list of numbers
    :return: True if '007' in order within list of numbers
    """
    for num in range(0,len(numbers)):
        if numbers[num] == 0:
            if numbers[num+1] == 0:
                print(numbers[num + 2])
                if numbers[num+2] == 7:
                    return True

if __name__ == "__main__":
        print(spy_game([1,2,3,4,5,6,0,0,3,7,3,0,0,5,7,0,0,4]))
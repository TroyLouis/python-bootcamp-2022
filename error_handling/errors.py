def error():
    try:
        #this throws an error because it's read only
        f = open('error_test_file.txt','r')
        f.write("write a line")
    except TypeError:
        print("There was a type error!")
    except OSError:
        print("OS Error")
    except:
        print("All other exceptions")
    finally:
        print("Always runs at the end")

def ask_int():
    while True:
        try:
            result = int(input("Type a number: "))
        except:
            print("That's not a number.")
            continue
        else:
            print(f'Thanks for typing {result}.')
            break
        finally:
            print("End of try/except")

def fail():
    for i in ['a',4,'c']:
        try:
            print(f'{i}^2 = {i ** 2}.')
        except:
            print(f'{i} is not a number.')
            continue
        finally:
            print("End of try/except")

if __name__ == "__main__":
    error()
    ask_int()
    fail()
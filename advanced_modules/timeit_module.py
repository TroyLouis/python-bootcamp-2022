import time
import timeit as t

def func(n):
    return [str(num) for num in range(n)]
print(func(10))

def func_2(n):
    return list(map(str,range(n)))
print(func_2(10))

start_time = time.time()
result = func(1000000)
end_time = time.time()
elapsed = end_time - start_time
print(elapsed)

start_time = time.time()
result = func_2(1000000)
end_time = time.time()
elapsed = end_time - start_time
print(elapsed)

stmt = '''
func(100)
'''

setup = '''
def func(n):
    return [str(num) for num in range(n)]
'''
#print(t.timeit(stmt,setup,number=1000000))

stmt = '''
func2(100)
'''

setup = '''
def func2(n):
    return [str(num) for num in range(n)]
'''
#print(t.timeit(stmt,setup,number=1000000))

if __name__ == "__main__":
    pass
import math, random
value = 3.45

print(math.floor(value))
print(math.ceil(value))
print(round(4.5))
print(round(5.5))
print(math.pi)
print(math.e)
print(math.inf)
print(math.log(100,10))
print(math.degrees(math.pi/2))
print(random.randint(1,500))
#print(random.seed(101))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

mylist = list(range(0,20))
print(random.choice(mylist))

#sample with replacement
print(random.choices(population=mylist,k=10))

#sample without replacement
print(random.sample(population=mylist,k=10))

print(mylist)
random.shuffle(mylist)
print(mylist)

#random floating point
print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))


if __name__ == "__main__":
    pass
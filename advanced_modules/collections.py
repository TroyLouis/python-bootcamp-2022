from collections import Counter, defaultdict

mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
mylist2 = [1,1,1,1, "a",'a',"a"]
word = 'asdfasdfasdfasdfasdfasdfasdf'
sentence = 'how many times does many appear in this sentence.'

d = {'a': 10}
# makes all default dict values 0
d1 = defaultdict(lambda: 0)

if __name__ == "__main__":
    print(Counter(mylist))
    print(Counter(mylist2))
    print(Counter(word))
    print(Counter(sentence.split()))
    c = Counter(word)
    print(c.most_common(2))
    print(d['a'])
    print(d1['wrong'])

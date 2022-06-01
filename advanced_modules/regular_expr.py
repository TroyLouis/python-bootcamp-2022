import re
text = "The agent's phone number is 404-333-4321. Call the phone!"
pattern = 'phone'
match = re.search(pattern,text)

#print(match.span())
#print(match.start(),match.end())

matches = re.findall('phone',text)
#print(len(matches))

for match in re.finditer('phone',text):
    print(match.group(), match.span())

phone = 'My pone number is 407-666-5940.'

number = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',phone)
print(number.group())

number1 = re.search(r'\d{3}-\d{3}-\d{4}', phone)
print(number1.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(phone_pattern, phone)
#indexing for group() starts at 1 not 0
print(result.group(1))

if __name__ == "__main__":
    pass
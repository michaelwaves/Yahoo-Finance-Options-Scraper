'''num1 = float(input("enter first number"))
op = input("enter operator")
num2 = float(input("enter second number"))

def calculate(num1, op, num2):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1-num2)
    elif op == '*':
        print(num1*num2)
    else:
        print("sorry that's not an operator") 

calculate(num1, op, num2)

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "April": "April",
    "May": "May",
    "Jun": "June",
}

print(monthConversions["Jun"])

i = 1
while i <= 10:
    print(i)
    i += 1

print("loop done")


print('i love keyboard shortcuts')
list = ['apples', 'oranges','banana']
for i in range(len(list)):
    print(list[i])

list2 = ['vaseline','baby lotion','baby formula', 'diapers', 'turtles','webcam', 'waterbottle', 'book', 'hand sanitizer']
for i in range(len(list2)):
    if list2[i][0] == 'b':
        print(list2[i])


print(2**3)
def exponent(base, exponent):
    result = 1
    for index in range(exponent):
        result = result * base
    return result

print(exponent(3,6))
print(exponent(3, 'six')) 

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for i in row:
        print(i)

def translate_giraffe(phrase):
    translation=''
    for i in phrase:
        if i in 'AEIOUaeiou':
            translation = translation + 'g'
        else:
            translation = translation + i
    return translation

print(translate_giraffe('banana'))'''

from cgitb import text
import email
import re
#regex text matching
text_to_search = '''
abcedefhijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ & * + > { } [ ] \ ()

905-787-8968
365-366-8643
416-895-1898

coryems.com

Mr. Schafer
Mr Smith
Ms Davis
Mr. T
Mrs. Robinson

 '''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
sentence = 'Start a sentence and bring it to an end 123'

urls = '''
https://www.google.com
https://coryems.com
http://youtube.com
https://www.nasa.com'''
#pattern = re.compile(r'[2-4]\d\d.\d\d\d.\d\d\d\d') #compiles only phone numbers beginning with 2 3 or 4
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
#matches = pattern.finditer(text_to_search)
#matches = pattern.finditer(urls)

#for match in matches:
    #print(match.group(3))


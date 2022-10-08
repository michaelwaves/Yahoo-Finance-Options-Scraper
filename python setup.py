import sys
print(sys.version)
print(sys.executable)

def greet(person):
    greeting = 'hello, {}'.format(person)
    return greeting

print(greet('world'))
print(greet('michael'))


### @export "part0"

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

### @export "part1"

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

### @export "part2"

import mystuff
mystuff.apple()

### @export "part3"

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

### @export "part4"

import mystuff

mystuff.apple()
print(mystuff.tangerine)

### @export "part5"

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

### @export "part6"

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


### @export "part7"

thing = MyStuff()
thing.apple()
print(thing.tangerine)

### @export "part8"

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)


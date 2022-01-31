

x = 78
x = "john"
y = 5 + 6j
z = True




name, age, isGirl = ("simran", 20, True)
print(name, age, isGirl)

print(type(name))
print(type(age))
print(type(isGirl))

c = 8 + 7j
d = 8.9
lst = [7, 8, 9, 10]
tp = (7, 8, 9, 10)
st = {7, 8, 9, 10}
dt = {"name":"simran", "age":20, isGirl:True}

print(type(c))
print(type(d))
print(type(lst))
print(type(tp))
print(type(st))
print(type(dt))


# This is a single line comment

'''
This is a multi-line comment
this is actually a multiline string,
which has not yet been assigned to any variable
And python treats then as comments
'''

print("\n\n\n")


f = 89.20           
i = int(f)          # 89

s = "567"           
i = int(s)          # 567

n = 90              
nf = float(n)       # 90.0
ns = str(n)         # "90"


'''

Here, int() float() str() complex() etc.
are called "constructor functions" of the respective datatypes

'''

'''

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

'''

print((6 < 7) and (6 > 8))      # False
print((6 < 7) or (6 > 8))       # True
print(not (6 < 7))              # False

n1, n2 = (50, 40)

print(~n1, ~n2)     # bitwise NOT

print(n1 & n2)      # bitwise AND
print(n1 | n2)      # bitwise OR
print(n1 ^ n2)      # bitwise XOR

print(n1 >> 3)      # right shift by 3 position
print(n2 << 1)      # left shift by 1 position

'''

n1 = 50 in binary is: (0011 0010)
n2 = 40 in binary is: (0010 1000)

~n1 => ~(0011 0010)     ~n2 => ~(0010 1000)
    =>  (1100 1101)         =>  (1101 0111)
    =>  -51                 =>  -41

n1 & n2
    0011 0010 -> 50
&   0010 1000 -> 40
-------------
    0010 0000 -> 32

n1 | n2
    0011 0010 -> 50
|   0010 1000 -> 40
-------------
    0011 1010 -> 58

n1 ^ n2
    0011 0010 -> 50
^   0010 1000 -> 40
-------------
    0001 1010 -> 26

50        = ...0000 0000(0011 0010)
(50 >> 3) = ......0 0000(0000 0110)010
          = 6

40        =     (0010 1000)0000 0000...
(40 << 1) = (001 0100 0000)
          = 80

'''




# Single line String
# Within single quotes or double quotes
a = "hello"
b = 'hello'

# Multiline Strings
# within triple single quotes or triple double quotes
a = """hello
there"""
b = '''hello
there'''

# Using single quote inside double quote is possible and vice-versa
a = "Hello 'world' how art thou"

# To use same quote inside as that of the surrounding quote
a = "Hello \"world\" how art thou"




# using Strings as arrays (0-based indexing)
name = "sandeep"        
print(len(name))        # 7
print(name[2])          # n

# presence/absence of a given substring
txt = "The best things in life are free!"
print("free" in txt)        # True
print("best" not in txt)    # False


txt = "Simran"

'''
                S   i   m   r   a   n
+ve index:      0   1   2   3   4   5
-ve index:     -6  -5  -4  -3  -2  -1

'''

txt[4]              #---> "a"
txt[-4]             #---> "m"

txt[1:4]            #---> "imr"
txt[1:-1]           #---> "imra"
txt[-5:-3]          #---> "im"

txt[:3]             #---> "Sim"
txt[3:]             #---> "ran"



# Uppercase and Lowercase:
txt = "Hello! World"
print(txt.upper())                                                      # HELLO! WORLD
print(txt.lower())                                                      # hello! world

# trim white spaces at the start and end:
txt = "    Hello! World  "
print(txt.strip())                                                      # Hello! World

# replace a substring with another substring:
txt = "Hello! World"
print(txt.replace("Wo", "abcd"))                                        # Hello! abcdrld

# Split a string based on a given delimiter(space by default):
txt = "appleFTmangoFTbanana"
print(txt.split("FT"))                                                  # ['apple', 'mango', 'banana']




a = "Sandeep"
b = "Auddy"
c = a + b       # "SandeepAuddy"


n = -45.6
c = 4 + 6j
s = "abc"

res = str(n) + str(c) + s # "-45.6(4+6j)abc"


print(c)
print(res)


person1, person2 = ("Chintu", "Chinki")
n1, n2 = (14, 13)

# Method-1 : Using format() method
txt = "I am {name} and I am {age} years old"
txt1 = txt.format(name = person1, age = n1)
txt2 = txt.format(name = person2, age = n2)
print(txt1)
print(txt2)

# Method-2 : Using f-strings
txt1 = f"I am {person1} and I am {n1} years old"
txt2 = f"I am {person2} and I am {n2} years old"
print(txt1)
print(txt2)
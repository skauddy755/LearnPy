# this is a single line comment


'''
udisdsd
dsdsdd
'''

from pickle import BINBYTES


print('Hello\nworld to \'sandeep\' ok')

# variables
x = 78
x = 90.9
x = 3 + 7j
print(x)

y = 'A'
y = 'simran'
print(y)

isCold = True
print(isCold)

#=================================================
x, y, z = (34, "simran", True)
print(x, y, z)

# ================================================
x = 755
y = str(x)
print(y)

s = "611"
num = int(s)

# print(y + num)

# =================================================================================================
s1 = 'my age is '
n = 21
print(s1 + str(n))
# ===============
s = "sandeep"
s = 2**3
print(s)
# ====================

print(9 / 2)
print(9 // 2)  #---> quotient
print(9 % 2) #-->remainder

fruit = "banana"
for i in range(len(fruit)):
    print(fruit[i])

b = "Hello, World!"
print(b[-5:-1])

a = [45, -2, 8, 9, 100, 90]

a.sort()
a.reverse()

print(a)


# ==============================================
# string methods:
# a.upper()
# a.lower()
# a.strip()
# a.split(" ")
# a.replace("H", "G")

someone = "terrorist"
role = 36

txt = "My name is {s1} and i am not a {s2}"
print(txt.format(s1 = someone, s2 = role))

someone = "Khan"
role = 36
txt1 = f"My name is {someone} and i am not a {role}"
print(txt1)
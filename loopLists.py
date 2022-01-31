# LOOPING THROUGH LIST:
# =============================================================

arr = [67, 45, 100, 300, 400, 611, 755]
# for loop (for each loop):
for x in arr:
    print(x)
# can it be used to change the elements?
for x in arr:
    x = 2000
    print(x)
print(arr)
# Ans = No


# for loop (using index):
# ----------------------------------
# range(a, b, step) integers  from a(inlu) to b(exclu) with step
# range(a, b) integers from a(inlu) to b(exclu)
# range(n) integers from 0 to n(exclu)

r = range(4, 10)
for i in r:
    print(i)
print(type(r))

r = range(0, len(arr))
for i in r:
    print(arr[i])

r = range(0, len(arr), 2)
for i in r:
    print(arr[i])


# while loop:
i = 0
while i < len(arr):
    print(arr[i])
    i = i + 1


# SORT LISTS:
# ====================================
dup = []
dup.extend(arr)

arr.sort()
print(arr)
arr.sort(reverse = True)
print(arr)

dup.sort()
dup.reverse()
print(dup)

# ====================================
# Copy arr to dup using append():
dup = []
for i in range(len(arr)):
    dup.append(arr[i])
print(dup)

# Copy arr to dup using extend():
dup = []
dup.extend(arr)
print(dup)

# copy using library method copy():
dup = arr.copy()
print(arr)

# JOIN lists:
# ======================================
a = [4, 5, 6]
b = [67, 71]
c = [100, 200]
x = a + b + c
print(x)

a.extend(b)
a.extend(c)
print(a)

z = a*2
print(z)

# LIST COMPREHENSION:
# ======================================


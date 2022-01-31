# Lists:

fruits = ["apple", "mango", True, 34, 3+4j, 90.62]
print(fruits)

# length of list:
n = len(fruits) # 6
# len() is a general command and can be used for lists, dict, tuple, strings ...

# Accessing elements of a list:
# fruits[a:b] will return a new list containing the elements from index a(inclu) to index b(exclu)
someFruits = fruits[2:4] # [True, 34]
someFruits = fruits[:4] # ["apple", "mango", True, 34]
someFruits = fruits[4:] # [3+4j, 90.62]

# index >= 0 (count from start),
# index < 0 (count from end)
singleFruit = fruits[3] # True
singleFruit = fruits[-2] # 3+4j

# changing values:
fruits[3] = "cherry"
fruits[1:4] = ["guava", 67]

# Adding alements:
# ----------------------------------------------------
thislist = ["apple", "banana", "cherry"]

# insert an element at some specified index:
thislist.insert(2, "watermelon")
print(thislist)

# insert an element at the end:
thislist.append("orange")
print(thislist)

# insert an entire list/tuple/set/dict at the end:
thislist.extend(fruits)
thislist.extend((4, 5, 7))
thislist.extend({4, 6, 8})

# Removing Elements:
# -----------------------------------------------------
arr = [4, 5, 6, 4, 4, 5]

# specify values (only the first occurence of the value is removed at a time)
arr.remove(4)
print(arr)

# specify the index to be deleted (if nothing is specifed then last index is removed) -> (len(arr) - 1)
arr.pop(2)
print(arr)

# deletes the 1st index
del arr[1]
print(arr)

# deletes the entire list variable
del arr
print(arr) # error: 404 arr does not exist

# does not delete the variable, but empties the list
arr.clear()
print(arr) # no errr : []
print(len(arr)) # 0






'''
Bubble sort:
------------
5 4 6 1
4 5 6 1, 4 5 6 1, 4 5 1 6
4 5 1 6, 4 1 5 6
1 4 5 6

colums 1+2+3+4+...(n-1) = n(n-1)/2

n*(n-1)/2
O(n^2)

'''
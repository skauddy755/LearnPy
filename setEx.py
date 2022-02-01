s = {7, 6, 6, -1, 5}
print(s)

arr = [5, 6, 6, 7, 5]
s1 = set(arr)
print(s1)

brr = list(s1)
print(brr)

s = {5, 6, -1}
s.add(3)
s.add(9)
print(s)


s1 = {"google", "ms", "appul"}
s2 = {"banana", "appul", "cherry"}

s1.update(s2)        #-> s1 gets changed
s3 = s1.union(s2)    #-> s1 does not get changed, rather a third set is created

s1.intersection_update(s2)
s3 = s1.intersection(s2)

s1.symmetric_difference_update(s2)
s3 = s1.symmetric_difference(s2)
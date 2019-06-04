**Write python program to define below lists and add y at the end of x\
		x = [1,2,3]\
		y = [4,5,6]\
		# Your code here\
		print(x)\
		# [1, 2, 3, [4, 5, 6]]**    
```
x=[1,2,3]
y=[4,5,6]
x.append(y)
print(x)
```  
  
**Write python program to define below lists and add elements of y at the end of x\
		x = [1,2,3]\
		y = [4,5,6]\
		# Your code here\
		print(x)\
		# [1, 2, 3, 4, 5, 6]**
```
x=[1,2,3]
y=[4,5,6]
x.extend(y)
print(x)
```

**Define a list and make a copy of it into another variable.**
```
l=[10,11,9]
p=l.copy()
print(p)
```

**Write command to count number of elements of x that have 2 as value.\
		x = [1,2,3,2,3,4]**
```
x=[1,2,3,2,3,4]
print(x.count(2))
```

**Write command to find index of 2 in below list.\
		x = [1,2,3,2,3,4]**
```
x=[1,2,3,2,3,4]
print(x.index(2))
```
	
**Write command to insert 10 as 2nd element in below list.\
		x = [1,2,3,2,3,4]**
```
x=[1,2,3,2,3,4]
x.insert(2,10)
print(x)
```
	
**Write command to reverse elements of below list.\
		x = [1,2,3,2,3,4]**
```
x=[1,2,3,2,3,4]
x.reverse()
print(x)
```

**Write command to sort elements of below list.\
		x = [1,2,3,2,3,4]**
```
x=[1,2,3,2,3,4]
x.sort()
print(x)
```

**Write a python program to remove a element from list after checking if element exists in another list.\
    Example:\
    l1 = [1,2,3]\
    l2 = [3,4,5]\
    Remove elements from l1 that are in l2.**
```
l1=[1,2,3]
l2=[3,4,5]
s1=set(l1)
s2=set(l2)
print(list(s1.difference(s2)))
```

**Write a python program to print count of each unique value in a list.**
```
x=[1,2,3,2,3,4]
s=set(x)
for i in s:
  print(i,':',x.count(i))
```

**Write a python program to build a new list with all even numbers from first list such that even numbers should be deleted from the first list and only odd numbers should remain in first list. All the even numbers should be displayed in a new list.**
```
x=[1,2,3,2,3,4]
e=[]
for i in x:
  if i%2==0:
    x.remove(i)
    e.append(i)
print(x)
print(e)
```

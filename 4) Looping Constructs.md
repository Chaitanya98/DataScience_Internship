
**Write a python program to check whether a given number is Odd or Even.**
```
x=int(input('Enter a number:'))
if x%2==0:
  print(x,' is even')
else:
  print(x,' is odd')
```

**Write a program to check whether a given number is prime or not.**
```
n=int(input('Enter a number:'))
c=0
for i in range(2,n):
  if n%i==0:
    c+=1
if c==0:
  print(n,'is prime')
else:
  print(n,'is not a prime')
```

**Write a python program to print all prime numbers between 1 and 100.**
```
for n in range(2,100):
  c=0
  for i in range(2,n):
    if n%i==0:
      c+=1
  if c==0:
    print(n)
```

**Write a python program to print the Fibonacci sequence.**
```
n=int(input("Enter the no. of Fibonacci terms:"))
n1=0
n2=1
print(n1)
print(n2)
c=2
while True:
  n3=n1+n2
  print(n3)
  c+=1
  n1=n2
  n2=n3
  if c==n:
    break
```

**Write a python program to transpose a arbitrary 3x3 matrix.**
```
matrix=[[1,2,3],[4,5,6],[7,8,9]]
trans=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    trans[j][i]=matrix[i][j]
print(trans)
```

**Write a python program to multiply two matrices.**
```
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[7,8,9],[4,5,6],[1,2,3]]
r=[[0,0,0],[0,0,0],[0,0,0]]
if len(A[0])==len(B):
  for i in range(0,3):
    for j in range(0,3):
      for k in range(0,3):
        r[i][j]=r[i][j]+A[i][k]*B[k][j]
print(r)
```

**Write a python Program to Find the Sum of the Series: 1 + 1/2 + 1/3 + ….. + 1/N .**
```
n=int(input("Enter the value of N:"))
x=0
for i in range(1,n+1):
  x+=1/i
print(x)
```

**Write a Python Program to Merge Two Lists and Sort it.**
```
l1=[20,12,98,95,93,23,10]
l2=[1,8,30,10,26]
l=l1+l2
l.sort()
print(l)
```

**Write a Python Program to Find the Second Largest Number in a List Using Bubble Sort.**
```
a=[12,23,36,92,20,98,100,10,6,87]
for j in range(len(a)):
  for i in range(len(a)-1):  
    if a[i]>a[i+1]:
      a[i],a[i+1]=a[i+1],a[i]
print(a[len(a)-2])
```

**Write a Python Program to Find the Cumulative Sum of a List where the ith Element of new list is the Sum of the First i Elements From The Original List.\
Input : [1,2,3,4,5]\
output: [1,2,6,10,15]**
```
a=[20,98,6,54,91,23,10]
b=[]
x=0
for i in range(len(a)):
  x+=a[i]
  b.append(x)
print(b)
```

**Write a Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.**
```
l=[81,96,25,31]
m=[]
for i in range(len(l)):
  sq=l[i]*l[i]
  c=(l[i],sq)
  m.append(c)
print(m)
```

**Write a python program to build a dictionary with keys as unique list values, values as number of times key is repeating in list.**
```
a=[1,1,2,2,3,4,3,5,4,6,6,9,1,2,5,7,6]
b={}
c=set(a)
for i in c:
  b[i]=a.count(i)
print(b)
```

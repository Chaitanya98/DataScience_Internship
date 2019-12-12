def addkv(**kwargs):
  sum=0
  for i in kwargs:
    sum+=kwargs[i]
  return sum
  
print(addkv(n1=8,n2=26,n3=69,n4=10))

def addvkv(*kargs,**kwargs):
  sum=0
  for i in kargs:
    sum+=i
    
  for i in kwargs:
    sum+=kwargs[i]
    
  return sum
  
print(addvkv(8,9,10,n3=7,n1=2))

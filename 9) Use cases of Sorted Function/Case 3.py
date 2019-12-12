def lsort(e):
  if type(e).__name__=='int':
    return 1000000000 + e 
  if type(e).__name__=='str':
    return 2000000000 + len(e) 
  if type(e).__name__=='list':
    return 3000000000 + len(e) 
  if type(e).__name__=='dict':
    return 4000000000 + len(e) 
    
l=[1,'a',[1,2], 2, 'ab', 'xyz', {'a':1, 'b':2}, [1,2,3,4]]
print(sorted(l,key=lsort))

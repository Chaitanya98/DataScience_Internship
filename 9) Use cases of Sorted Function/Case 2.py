def madd(row):
  sum=0
  for i in row:
    sum+=i
  return sum
  
l=[[1, 2, 3], [4, 5, 6], [1, 2, 1], [1, 3, 4]]
print(sorted(l,key=madd))

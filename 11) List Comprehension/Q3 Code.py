def factors(n):
  return [i for i in range(2,int(n/2)+1) if n%i==0]
print([i for i in range(100) if len(factors(i))==0])

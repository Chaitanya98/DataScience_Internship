def factors(n):
  return [i for i in range(2,int(n/2)+1) if n%i==0]
print(factors(100))

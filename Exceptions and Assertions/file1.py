def getAge():
  age=None
  for i in range(5):
    try:
      age=int(input('Enter age:'))
      print("Age:",age)
    except:
      print("Invalid input. Re-enter:")
    
    if age!=None:
        break
  else:
    print("Incorrect input. Try later")
    
  return age 

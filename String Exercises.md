**Write command to get first 10 chracters of a string**.
```
  print('FCBarcelona'[:10])
```  
**Write command to get last 10 chracters of a string.**
```
  print('FCBarcelona'[-10:])
```
**Write command to count number of times 'a' is occuring in 'abcdabcd'**
```
  print('abcdabcd'.count('a'))
```  
**Write command to get first occurance of 'a' in  'abcdabcd'**
```
  print('abcdabcd'.index('a'))
```
**Write command to get last occurance of 'a' in  'abcdabcd'**
```
  print('abcdabcd'.rindex('a'))
```
**Write a command to add space between each of the characters in 'abcdef'**
```
  print(" ".join('abcdef'))
```  
**Write a program to get a string and a character as user inputs, and check, if string starts and/or ends with character passed as parameter also.**
```
  s=input('Enter a string:')
  c=input('Enter a character:')
  if s.startswith(c):
    print("Character starts with",c)
  else:
    print("Character doesn't start with",c)
  if s.endswith(c):
    print("Character ends with",c)
  else:
    print("Character doesn't end with",c)
```
**Write a command to add spaces around a string passed as parameter to make string 20 characters long and make text center aligned.**
**Example: if 'abc' is input, output is '       abc         ' **
```
  st='FCBarcelona'
  print(st.center(20))
```
**Write a command to convert sentence passed as parameter to Title case.**
```
  print('messi is the greatest of all time'.title())
```  
**Write a command to remove spaces at the begining and ending of a string passed as parameter.**
```
  print("    Messi is the GOAT   ".strip())
```  
**Write a command to convert string passed as parameter to lower case.**
```
  print("kjdbdkdfn".lower())
```  
**Write a command to convert string passed as parameter to upper case.**
```
  print("kjdbdkdfn".upper())
```
**Write a program to get 3 parameters : \
	1. A string and \
	2. A part of the string to be replaced \
	3. A string to replace the part \
	as user inputs, and replace all occurances of from char/string with to char/string and print updated string.\
  Example: \
  			1st Param: abcdefgh \
			2nd Param: abc\
			3rd Param: xyz\
			Output: xyzdefgh**
```
  st=input('Enter a string:')
  stpres=input('Enter the part to be replaced:')
  strep=input('Enter the part to replace it with:')
  print(st.replace(stpres,strep))
```	
**Write a program that takes below as parameters:\
		1. A integer\
		2. length
	Exercise1: Trim spaces around string passed as paramter and pads spaces on left 
	Exercise2: If user entered non numeric value, keep asking user to enter valid integer as input until proper integer is given as input.\
	Example:\
			1st Param: 123\
			2nd param: 10\
		<pre>	Output: "       123"** </pre>
```			
  while True:
    a=input("Enter a string:")
    if a.isnumeric():
      break
    else:
      print("Enter a numeric string only")
  l=int(input("Enter total length:"))
  print(a.strip().rjust(l))
```

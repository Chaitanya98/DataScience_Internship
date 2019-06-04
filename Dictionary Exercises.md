**Question 1:\
d1 = {1:"one", 2:"two"}\
d2 = {2:"two", 3:"three", 4:"four"}\
Identify keys that are only in d1, d2\
Identify keys that are common between d1 and d2.\
(Onlu use loops and sets.)**

```
s1=set()
s2=set()
d1={1:"one",2:"two"}
d2={2:"two",3:"three",4:"four"}
for i in d1.keys():
  s1.add(i)
print("Keys in d1:",s1)
for i in d2.keys():
  s2.add(i)
print("Keys in d2:",s2)
print("Keys common in d1 & d2:",s2.intersection(s1))
```

**Question 2:\
d1 = {"name":"John", "city":"Mumbai", "Profession":"IT"}\
d2 = {"name":"John", "city":"Delhi", "Age":30}\
Update d1 with values from d2.\
After update d1 should look like below:\
d1 = {"name":"John", "city":"Delhi", "Age":30, , "Profession":"IT"}**

```
d1 = {"name":"John", "city":"Mumbai", "Profession":"IT"}
d2 = {"name":"John", "city":"Delhi", "Age":30}
d1.update(d2)
print(d1)
```

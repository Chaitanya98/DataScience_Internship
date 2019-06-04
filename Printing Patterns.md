**Write a python program to print Full Triangle Pyramid pattern using star. Take height of triangle as command line parameter.**
```
h=6
for i in range(1,h+1):
  print(' '*(h-i)+'*'*(i*2-1))
```

**Write a python program to print double sided stair-case pattern.**
```
                 *   * 
                 *   * 
             *   *   *   * 
             *   *   *   * 
         *   *   *   *   *   * 
         *   *   *   *   *   * 
     *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   * 
 *   *   *   *   *   *   *   *   *   * 
 *   *   *   *   *   *   *   *   *   * 
```

```
h=int(input("Enter the number of stairs:"))
for i in range(1,h+1):
  print(' '*(2*(h-i))+'* '*(i*2))
  print(' '*(2*(h-i))+'* '*(i*2))
```

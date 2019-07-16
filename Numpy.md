**Create a 3x3 Numpy Array for below data with int32 as data type.
nl = [[1,2,3],[4,5,6],[7,8,9]]**

    import numpy as np 

    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    print(nl)
    
**Write a expression using slicing to get below.
[[1,2],[4,5]]**
    
    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    print(nl[:2,:2])

**Write an expression to add a new row to nl to make it look like below.
nl should look like below after change 
[[1,2,3],[4,5,6],[7,8,9], [10,11,12]]**

    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    nl=np.append(nl,[[10,11,12]],axis=0)
    print(nl)
    
**Write an expression to add a new column to nl to make it look like below.
nl should look like below after change 
[[1,2,3,101],[4,5,6,201],[7,8,9, 301], [10,11,12, 401]]**

    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    nl=np.append(nl,[[10,11,12]],axis=0)
    nl=np.append(nl,[[101],[201],[301],[401]],axis=1)
    print(nl)
    
**Write an expression to add [[100,200,300,4000]] to every element of nl to get below outcome.<br>
[[101,202,303,4101]<br>
,[104,205,306,4201]<br>
,[107,208,309, 4301]<br>
,[110,211,312, 4401]]**

    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    nl=np.append(nl,[[10,11,12]],axis=0)
    nl=np.append(nl,[[101],[201],[301],[401]],axis=1)

    print(nl+[[100,200,300,4000]])

**Write an expression to split nl from above into two even size 2x4 arrays.<br>
First array should have <br>
[[101,202,303,4101]<br>
,[104,205,306,4201]<br>
Second Array should have<br>
[[107,208,309, 4301]<br>
,[110,211,312, 4401]]**

    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    nl=np.append(nl,[[10,11,12]],axis=0)
    nl=np.append(nl,[[101],[201],[301],[401]],axis=1)

    nl=nl+[[100,200,300,4000]]

    n1,n2=np.vsplit(nl,2)
    print(n1,"\n\n",n2)

**Write an expression to split nl from above into two even size 4x2 arrays.<br>
First array should have <br>
[[101,202]<br>
,[104,205]<br>
,[107,208]<br>
,[110,211]]<br>
Second Array should have<br>
[[303,4101]<br>
,[306,4201]<br>
,[309, 4301]<br>
,[312, 4401]]**

    nl=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='int32')
    nl=np.append(nl,[[10,11,12]],axis=0)
    nl=np.append(nl,[[101],[201],[301],[401]],axis=1)

    nl=nl+[[100,200,300,4000]]

    n1,n2=np.hsplit(nl,2)
    print(n1,"\n\n",n2)


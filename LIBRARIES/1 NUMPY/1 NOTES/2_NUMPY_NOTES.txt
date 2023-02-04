
⟫⇛                            NUMPY                                         ⇚⟪

⟫⇛ ARRAY Attributes :

1. ndim ==> To get dimension of the arrays
2. shape ==> To get the shape of the array
3. size ==> To get size of the array which is nothing but number of elements.
4. dtype ==> To get data type of array elements
5. itemsize ==> The size of each array element in bytes

eg -1:
a=np.array([10,20,30,40])

a.ndim ==> 1
a.shape ==>(4,)
a.size ==>4
a.dtype ==> int 32
a.itemsize ==> 4








======================================================================================================================================

In python we have data types like int, float,complex,bool,str etc.
But , numpy has some extra data types in addition to these types. we can represent data types by using
a single character also.
1.i ==> integer (int8,int16,int32,int64)
2.b ==> boolean
3.u ==> unsigned integer(uint8,uint16,uint32,uint64)
4.f ==> float(float16,float3,float64)
5.c ==> complex(complex64,complex128)
6.s ==> String
7.U ==> Unicode string
8.M ==> datetime


int8 ==>
The value will be represented by Using 8 bits .
The range of values : -128 to 127 


int16 ==>
The value will be represented by Using 8 bits .
The range of values : -32768 to 32767 

int32 ==>
The value will be represented by Using 8 bits .
The range of values : -2147483648 to 2147483648

int64 ==>
The value will be represented by Using 8 bits .
The range of values : -9223372036854775808 to 9223372036854775808

Note:
1. By default int means int32
2. By default float means float64

Note: int8 requires less memory than int32 type

import numpy as np
a=np.array([10,20,30,40])
import sys
print(sys.getsizeof(a))          ==>128
a=np.array([10,20,30,40],dtype='int8')
print(sys.getsizeof(a))          ==>116



-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

How to check the data type of an array ? 

By Using dtype attribute.
eg: 

import sys
import numpy as np
a = np.array([10, 20, 30, 40])
print(a.dtype)              ==>int32
a = np.array([10.5, 20.6, 30, 40])
print(a.dtype)              ==>float64

-------------------------------------------------------------------------------

How to create array with required data type ?
by using dtype argument.
a = np.array([10, 20, 30, 40],dtype='i8')
print(a.dtype)              ==>int64
a = np.array([10, 20, 30, 40],dtype='int8')
print(a.dtype)              ==>int8
a = np.array([10, 20, 30, 40],dtype='i')
print(a.dtype)              ==>int32

Note: if  the array element unable to convert into our specified type, then we will get error.

-------------------------------------------------------------------------------
a = np.array(['a', 20, 30, 40],dtype=int)

ValueError                                Traceback (most recent call last)
Cell In [5], line 1
----> 1 a = np.array(['a', 20, 30, 40],dtype=int)

ValueError: invalid literal for int() with base 10: 'a'

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

How to convert the type of existing array ?
In general we can USe astype() function.

option 1 ==>
a = np.array([10, 20, 30, 40])
print(a.dtype)   ==>int32
b= a.astype('float64')
print(b)         ==> [10. 20. 30. 40.]
b.dtype          ==>dtype('float64')

Note: By Using the corresponding data type function also, we can convert the type
of the array.

option 2 ==>
a = np.array([10, 20, 30, 40])
print(a.dtype) ==>  int32
c=np.float64(a)
print(c)       ==>  [10. 20. 30. 40.]
c.dtype        ==>  dtype('float64')



a = np.array([10, 20, 30, 40])
print(a.dtype)
x=np.bool_(a)
print(x)
x.dtype

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------





















































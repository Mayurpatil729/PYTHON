⟫⇛                           OOPS                                     ⇚⟪

1. In Python every thing is an object. To create objects we required some Model or Plan or Blue 
    print, which is nothing but class.
2. We can write a class to represent properties (attributes) and actions (behaviour) of object.
3. Properties can be represented by variables
4.Actions can be represented by Methods.


⟫⇛ CLASS IS AN BLUEPRINT/PLAN/MODEL/DESIGN FOR AN OBJECT.
⟫⇛ OBJECT IS A PYSICAL EXITETANCE OF A CLASS.

SYNTAX:

class name_of_class:        //class name starts with capital letter in oops
    '''doc string''''
    properties (variables)
    actions (methods)

How to create object in python:
    reference variable = classname()
    eg :   s1 = Student()

Every object has properties and behaviour.
-------------------------------------------
1. Properties(data) are specified by Variables
2. Behaviour can be specified by Methods

3 Types of variables:
-----------------------------------------------------
1. Instance variables (Object level variables)
2. Static Variables (Class level variables)
3. Local Variables (Methed level variables)

3 Types of Methods:
------------------------------------
1. Instance Methods
2. Class methods
3. static methods

==> Functions which are defined in class is called as Methods.

⟫⇛ Reference variable can be used to refer objects.
⟫⇛ By using reference vaFiab1e, we can invoke functionlaity of object.
⟫⇛ For a single object, there may a chance of multiple references.
⟫⇛ purpose of reference variable is we can access members/variables of objecs

The variable which can be used to refer object.
By using this reference variable we can operate object i.e by
using reference variable we can access variables and methods.




------------------------------------------------------------------------
⟫⇛ Self variable
------------------------------------------------------------------------
1. self is a reference variable, which is always pointing to current object.
Within the python class, to access current object, we can use self.
2.The first argument to the constructor is always self.
The first argument to the instance method is always self.
We are not required to provide value for self variable, PVm itself will provide
value.
3. We can use self always within the class only.
Inside constructor, we can use self to declare object related variables(instance
variables)
4. self is not a keyword. We can use any name like delf/kelf etc.l
   But it is recommended to use self.



------------------------------------------------------------------------
⟫⇛ Constructor
------------------------------------------------------------------------
1. Constructor is a special method.
2. The name of the constructor is always
    __init__()
3. We are not required to call constructor explicitly.
   automatically when we are creating an object.
4. per object, constructor will be executed only once.
   It will be executed
5. The main purpose of constructor is to declare and initialize instance variables
    __init__ means initialization
6. Constructor should take atleast one argument (atleast self)
7. Within the python class constructor is optional. If we are not providing
   constructor default constructor will be provided by PVM.
8. We can call constructor explicitly, then it will be executed just like a normal
   method. and new object won't be created.
9. constructor/method overloading not possible in python.
   If we are trying to declare multiple constructors, PVM will always consider 
   only last constructor













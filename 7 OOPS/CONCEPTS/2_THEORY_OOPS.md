<!-- @format -->

## 3 Types Variables

1. Instance Variables/Object level Variables
2. Static Variables/Class level variables.
3. Local Variables/Method Level Variables.

---

1. Instance Variables:

---

1.If the value of a variable is varied from object to object, such type of variables
are caned instance variables/ object level variables. 2. For every object a separate copy will be created.
3.In general we can define instance variables inside constructor by using self .1

2. Static Variables

---

If the value of a variable is not varied from object to object then it is not
recommended to declared that variable as instance variable. static variables/class
level variables.

In the case of instance variables, for every object a separate copy.
But in the case of static variables, a single copy will be created and shared to every object of that class
static variables should be declread within the class directly.

3. Local Variables

---

To meet temporary requirements of the programmer, we can declare variables directly
inside a method.

## Types of Methods

1. Instance Method
2. Class method
3. Static Method

## 1.Instance Method :

If we are accessing instance variables
(whether we are using static and local variables or not)
the first argument to the instance method should be self.which is the reference variable to the current object.
If we are using atleast one instance variable (whether using static variables or
not)-->instance method
If we are not using atleast one instance variable--->class method or static method.
If we are not using any instance variable, but we are using static I
variables --> class method.

If we are not using any instance variable and any static variable, then this method
no way related to object and class and it is general utility method, we have to
declare such method as static method .

cls-->reference variable to the class object.

The first argument to the instance method: self, which is pointing to current object
The first argument to the class method: cls, which is pointing to corresponding
class object.
instance method--> no decorator
class method--> @classmethod
static method ---> @staticmethod

## Various places to declare instance variables:

1. Inside constructor by using self.
2. Inside instance method by using slef.
3. Outside of the class by using object reference.

## How to Access Instance Variables:

Within the class by using self
Outside of the class by using object reference.

## How to delete instance variables:

within the class:
del self. variablesname

outside of the class:
del objectreference. variablename


# 🧠 **OOPS (Object-Oriented Programming System)**

### 🔹 1. In Python, **everything is an object**.

To create objects, we need a **model or plan or blueprint**, which is called a **class**.

### 🔹 2. We can write a **class** to represent the **properties (attributes)** and **actions (behavior)** of an object.

### 🔹 3. 🧾 Properties can be represented by **variables**.

### 🔹 4. 🛠️ Actions can be represented by **methods**.

---

## 🧰 CLASS & OBJECT 🔁

> 🏗️ **Class** is a **blueprint / plan / model / design** for an object.
> 🧍‍♂️ **Object** is the **physical existence** of a class.

---

## 🧾 **SYNTAX** of Class:

```python
class ClassName:          # Class name starts with capital letter in OOPs
    '''doc string'''
    # properties (variables)
    # actions (methods)
```

---

## 🎯 **How to create an object in Python:**

```python
reference_variable = ClassName()
# Example:
s1 = Student()
```

---

### 🧍 Every object has:

1. **Properties (data)** → specified by **variables**
2. **Behavior (actions)** → specified by **methods**

---

## 🧪 **Types of Variables:**

1. 📌 **Instance Variables** – Object-level variables
2. 📌 **Static Variables** – Class-level variables
3. 📌 **Local Variables** – Method-level variables

---

## 🧪 **Types of Methods:**

1. 🔁 **Instance Methods**
2. 🏷️ **Class Methods**
3. 🧷 **Static Methods**

> ✅ **Functions defined inside a class are called Methods.**

---

## 🔗 **Reference Variable:**

* 🧭 A **reference variable** is used to refer to objects.
* 🧠 Using it, we can invoke object functionality.
* 🔁 A single object may have **multiple references**.
* 🎯 It allows access to the **members/variables of the object**.

✍️ The variable used to refer to an object is the **reference variable**.
Using it, we can operate on the object — i.e., access its **variables and methods**.

---

## 🤳 **Self Variable**

---

### 🔹 1. `self` is a **reference variable** that always points to the **current object**.

Within a class, we use `self` to access the current object.

### 🔹 2. The **first argument** to the **constructor** and **instance method** is always `self`.

We do **not need to pass** it manually — Python's Virtual Machine (**PVM**) provides it automatically.

### 🔹 3. We use `self` **only within the class** to declare object-related variables (**instance variables**).

### 🔹 4. `self` is **not a keyword** — we can use any name like `delf`, `kelf`, etc.,

but it is **recommended to use `self`** for clarity.

---

## 🏗️ **Constructor**

---

### 🔹 1. Constructor is a **special method**.

### 🔹 2. The name of the constructor is always `__init__()`.

### 🔹 3. We do **not need to call it explicitly** — it is invoked **automatically** when creating an object.

### 🔹 4. Per object, the constructor is **executed only once**.

### 🔹 5. The **main purpose** of the constructor is to **declare and initialize instance variables**.

The name `__init__` implies **initialization**.

### 🔹 6. A constructor should take **at least one argument** (i.e., `self`).

### 🔹 7. The constructor is **optional**. If not provided, the **PVM provides a default constructor**.

### 🔹 8. We **can call a constructor explicitly**, but it will behave like a **normal method** (won't create a new object).

### 🔹 9. ❌ **Constructor/Method Overloading is NOT possible** in Python.

If multiple constructors are declared, the **PVM only considers the last one**.

---

# 🧩 BASIC ANALOGY FOR CLARITY

```
🔹 Class      : Cast / Mold
🔹 Attributes : Car Properties → Color, Engine
🔹 Methods    : Car Features → Open Door, Start Engine
🔹 Object     : Car (the final product made from mold)
```

---

## 🧵 Programming Paradigms in Python:

### 1️⃣ **Procedural Programming**

Traditional, step-by-step instruction-based code.

### 2️⃣ **OOPs – Object-Oriented Programming**

🧠 A way of **organizing code** using **blueprints (classes)** to represent **real-world entities**
(e.g., student, car, house). These help in:

* Creating **objects** (instances of those entities)
* Defining their **attributes and behaviors**

---

## 📘 Recap:

* 🧱 **Class** = Blueprint/template
* 🧍 **Object** = Instance created from the blueprint
* 🧾 **Attributes** = Properties (variables)
* 🛠️ **Methods** = Behavior (functions inside the class)

---


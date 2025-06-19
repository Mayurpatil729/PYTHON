
# 🧮 **3 Types of Variables in OOPs**

### 1️⃣ Instance Variables / Object-Level Variables

### 2️⃣ Static Variables / Class-Level Variables

### 3️⃣ Local Variables / Method-Level Variables

---

## 🔹 1. **Instance Variables**

---

📌 If the value of a variable **varies from object to object**, such variables are called **instance variables** or **object-level variables**.
📌 For **every object**, a **separate copy** of the variable will be created.
📌 Generally, we define instance variables **inside the constructor** using `self`.

```python
def __init__(self):
    self.name = "Mayur"
```

---

## 🔹 2. **Static Variables**

---

📌 If the value of a variable **does not vary from object to object**, then it is **not recommended** to declare it as an instance variable.
📌 These are called **static variables** or **class-level variables**.

🧠 In the case of:

* **Instance variables** → each object has its **own copy**.
* **Static variables** → a **single copy** is created and **shared among all objects** of the class.

📌 Static variables should be **declared within the class directly**, outside any method.

```python
class Student:
    college_name = "IIT"  # static variable
```

---

## 🔹 3. **Local Variables**

---

📌 To meet **temporary requirements**, programmers can declare **variables directly inside a method**.
📌 These variables are known as **local variables** and their scope is **limited to the method** in which they are defined.

```python
def show():
    message = "Hello"  # local variable
```

---

# 🧪 **Types of Methods**

---

### 1️⃣ Instance Method

### 2️⃣ Class Method

### 3️⃣ Static Method

---

## 🔹 1. **Instance Method**

---

🧠 If we are accessing **instance variables** (whether we are using static or local variables or not), it should be an **instance method**.
📌 The **first argument** must be `self` — a **reference variable to the current object**.

✅ Conditions:

* If at least **one instance variable** is used → it's an **instance method**.
* If **no instance variable** is used but **static variables** are → it's a **class method**.
* If **neither instance nor static variables** are used → it's a **static method** (general utility).

---

## 🏷️ **Method Decorators & References**

---

| Method Type     | Decorator       | First Argument  |
| --------------- | --------------- | --------------- |
| Instance Method | *No decorator*  | `self` (object) |
| Class Method    | `@classmethod`  | `cls` (class)   |
| Static Method   | `@staticmethod` | *None*          |

🧠 `cls` → reference variable to the **class object**.
🧠 `self` → reference variable to the **current object**.

---

## 📍 **Various Places to Declare Instance Variables**

---

1. Inside constructor using `self`
2. Inside instance method using `self`
3. Outside the class using **object reference**

---

## 🔎 **How to Access Instance Variables**

---

* **Within the class** → using `self`
* **Outside the class** → using **object reference**

---

## ❌ **How to Delete Instance Variables**

---

* **Within the class**

```python
del self.variable_name
```

* **Outside the class**

```python
del object_reference.variable_name
```

---


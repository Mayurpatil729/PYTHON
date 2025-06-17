
## 🧠 **What is a Decorator in Python?**

> A **decorator** is a special function in Python that **modifies or extends the behavior of another function** without changing its actual code.

It’s like **wrapping a gift box** — you don’t change what’s inside, but you can decorate it, label it, or wrap it beautifully from outside.

---

## ⚙️ **How Do Decorators Work?**

* In Python, functions are **first-class objects**, meaning they can be:

  * Passed as arguments
  * Returned from other functions
  * Assigned to variables

### 🔁 A decorator:

* **Takes a function as input**
* **Defines a wrapper function** (to add behavior before/after the original function)
* **Returns the wrapper**

### 🧩 Syntax:

```python
@decorator_name
def my_function():
    pass
```

This is the same as:

```python
my_function = decorator_name(my_function)
```

---

## ✅ **Example (Without Code)**

Suppose you have a function that adds two numbers.
You want to **log the time** it was called — without changing the function code.

→ Use a **decorator** that logs before and after the original function runs.

---

## ⭐ **Advantages of Decorators**

| Benefit                      | Description                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------ |
| ✅ **Code Reusability**       | You can apply the same decorator to many functions.                            |
| ✅ **Separation of Concerns** | Keep extra logic (like logging, timing, validation) outside the main function. |
| ✅ **Cleaner Code**           | No need to repeat setup/cleanup logic inside every function.                   |
| ✅ **Extensibility**          | Easy to add new behavior to existing functions without touching them.          |
| ✅ **Useful in Frameworks**   | Widely used in Flask, Django, FastAPI, etc.                                    |

---

## ⚠️ **Disadvantages of Decorators**

| Limitation                | Description                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| ❌ **Can be confusing**    | New learners may find decorators and closures hard to read/understand. |
| ❌ **Debugging is harder** | Wrapping functions can make stack traces harder to follow.             |
| ❌ **Loss of metadata**    | Function name/docstring may be lost unless you use `functools.wraps`.  |

---

## 🧠 When to Use Decorators?

* **Logging**
* **Timing a function**
* **Authentication/authorization (e.g., in web apps)**
* **Input validation**
* **Caching/memoization**
* **Pre- and post-processing**


---
### Function Decorators:
-  Decorator is a function which can take a function as argument and extend its functionality and returns modified function with extended functionality.
- The main objective of decorator functions is we can extend the functionality of existing functions without modifies that function.


### Decorator Chaining
- We can define multiple decorators for the same function and all these decorators will form Decorator Chaining.

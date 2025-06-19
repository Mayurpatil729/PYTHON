<!-- @format -->

# Setting up a Python Virtual Environment and Installing Dependencies

This guide will walk you through setting up a virtual environment, configuring it with the `ipykernel` package, and managing dependencies using a `requirements.txt` file.

## Prerequisites

- Ensure you have `conda` installed. You can download it from [Anaconda's official website](https://www.anaconda.com/products/distribution) or install `Miniconda` for a lightweight alternative.
- Make sure `pip` is installed.

---

## Steps to Set Up the Environment

### 1. Create a Virtual Environment

Run the following command to create a virtual environment in the current directory:

```bash
conda create -p .venv python=3.12
```

This command creates a virtual environment with Python 3.12 in a folder named `.venv` within your project directory.

### 2. Activate the Virtual Environment

Activate the virtual environment using the following command:

- **Linux/MacOS**:
  ```bash
  source activate ./.venv
  ```
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

### 3. Install `ipykernel`

Once the virtual environment is active, install the `ipykernel` package to enable the environment to be used as a Jupyter kernel:

```bash
pip install ipykernel
```

### 4. Create a `requirements.txt` File

If you want to manage your dependencies, create a `requirements.txt` file in the project directory. This file should list all the packages your project depends on. For example:

```
ipykernel
numpy
pandas
```

### 5. Install Dependencies from `requirements.txt`

To install all dependencies listed in the `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

---

## Notes

- To deactivate the virtual environment, run:
  ```bash
  conda deactivate
  ```
- To delete the virtual environment, simply remove the `.venv` directory:
  ```bash
  rm -rf .venv
  ```
  _(Use `del .venv` on Windows)_

## Additional Resources

- [Conda Documentation](https://docs.conda.io/en/latest/)
- [pip Documentation](https://pip.pypa.io/en/stable/)

With this setup, you are ready to develop and run Python projects in an isolated environment.

---

### Core Python:

1. Language Fundamentals
2. Operators
3. Input and Output Statements
4. Flow Control
5. String Data Type
6. List Data Structure
7. Tuple Data Structure
8. Set Data Structure
9. Dict Data Structure
10. Functions
11. Modules
12. Packages

---

### Advanced Python:

1. OOPs (Object-Oriented Programming)
2. Exception Handling
3. File Handling
4. Serialization
5. Regular Expressions and Web Scraping
6. Multi-threading
7. Python Database Connectivity (PDBC)
8. Decorators
9. Generators
10. Logging Module
11. Assertions
12. NumPy
13. Pandas
14. Unit Testing

---

### Python Full Stack web developer :

15. Django
16. UI Technologies
17. Django Rest Framework (DRF)

---

Microsoft Python Certification :
Core Python + File Handling+Exception Handling

---

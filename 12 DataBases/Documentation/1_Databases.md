### Python Database Programming (PDBC) Notes

---

#### 1. **Storage Areas**
As part of applications, data like customer information, billing information, and call logs need to be stored. Python applications generally require two types of storage areas:

- **Temporary Storage Areas**: Data is stored temporarily (e.g., Python objects like List, Tuple, Dictionary). Once the program execution completes, these objects are destroyed, and data is lost.
  
  **Examples**: 
  - Lists
  - Tuples
  - Dictionaries
  
  **Characteristics**:
  - Stored in memory (RAM).
  - Data is destroyed after program execution.
  
- **Permanent Storage Areas (Persistent Storage Areas)**: Data is stored permanently in file systems, databases, data warehouses, or Big Data technologies.
  
  **Examples**:
  - File Systems
  - Databases (e.g., MySQL, Oracle, SQLite)
  - Big Data technologies
  
#### 2. **Temporary Storage Areas**
- **Memory-Based Storage**: Python objects like Lists, Tuples, and Dictionaries.
- **Volatile**: Data is lost after program completion.

#### 3. **Permanent Storage Areas**
Also known as **Persistent Storage Areas**, where data is stored permanently.

- **File Systems**:
  - **Best for storing small amounts of data**.
  - **Limitations**:
    1. Cannot store large amounts of data.
    2. No query language support (complex operations).
    3. No security features.
    4. Lack of mechanisms to prevent data duplication (inconsistent data).
  
- **Databases**:
  - Overcome the limitations of file systems by providing structured storage.
  - **Advantages**:
    1. Support for **huge amounts of information**.
    2. **Query language support** (e.g., SQL) for easier database operations.
    3. Data security (username and password required).
    4. Data stored in tables with constraints to prevent duplication (e.g., Primary Keys, Unique Keys).
  
  - **Limitations**:
    1. Cannot store extremely large data (e.g., Terabytes).
    2. Limited to **structured data** (tabular/relational data) and cannot handle **semi-structured** (e.g., XML) or **unstructured** data (e.g., video, audio).
  
  - **Advanced Storage Solutions**: To handle these limitations, advanced storage like **Big Data** and **Data Warehouses** are used.

#### 4. **Python Database Programming (PDBC)**
Python can interact with databases using SQL commands to perform operations like creating tables, inserting, updating, deleting, and selecting data.

- **SQL**: The language used to interact with databases.
  
#### 5. **Python Database Modules**
Python provides separate modules to connect to various databases:

- **cx_Oracle**: For connecting to Oracle databases.
- **pymssql**: For connecting to Microsoft SQL Server.
- **sqlite3**: For working with SQLite databases.
- **MySQLdb**: For connecting to MySQL databases.


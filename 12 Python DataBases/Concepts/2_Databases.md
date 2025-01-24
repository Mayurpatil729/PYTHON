### Python Database Programming (PDBC)  

#### **Standard Steps for Python Database Programming**:

1. **Import Database Module**:
   ```python
   import cx_Oracle
   ```

2. **Establish Connection**:
   Use the `connect()` function to create a connection object.
   ```python
   con = cx_Oracle.connect('username/password@host')
   ```

3. **Create Cursor Object**:
   Use the `cursor()` method to create a cursor object for executing SQL queries.
   ```python
   cursor = con.cursor()
   ```

4. **Execute SQL Queries**:
   - **execute(query)**: Executes a single SQL query.
   - **executemany(query, params)**: Executes a parameterized query.
   - **executescript(sqlqueries)**: Executes multiple SQL queries separated by a semicolon.

   Example:
   ```python
   cursor.execute("SELECT * FROM employees")
   ```

5. **Commit or Rollback**:
   - **commit()**: Save changes to the database (for `INSERT`, `UPDATE`, `DELETE`).
   - **rollback()**: Roll back changes if necessary.
   ```python
   con.commit()
   ```

6. **Fetch Results** (for `SELECT` queries):
   - **fetchone()**: Fetches one row.
   - **fetchall()**: Fetches all rows as a list.
   - **fetchmany(n)**: Fetches the first `n` rows.

   Example:
   ```python
   data = cursor.fetchall()
   for row in data:
       print(row)
   ```

7. **Close Resources**:
   Close the cursor and connection when done.
   ```python
   cursor.close()
   con.close()
   ```

#### **Important Methods**:
- `connect()`
- `cursor()`
- `execute()`
- `executemany()`
- `executescript()`
- `commit()`
- `rollback()`
- `fetchone()`
- `fetchall()`
- `fetchmany()`
- `close()`

These methods apply universally across most databases (e.g., Oracle, MySQL, SQLite).
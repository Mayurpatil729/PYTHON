import cx_Oracle

try:
    con=cx_Oracle.connect("")
    query="create table employees(eno number,ename varchar2(10),esal number(10,20))"
    query="drop table employees"
    query="insert into employees values(100,'Mayur',1000,'shirpur'')"
    records=[(200,'Sunny',2000,'Mumbai'),(300,'Bunny',3000,'Hyd'),(400,'chinny',400,'chennai')]
    cursor.executemany(query,records)
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Table created successfully")
    print("Record Inserted successfully")
    
    
    # cursor=con.cursor()
    # while True:
    #     eno=int(input('Enter Employee Number : '))
    #     ename=input("Enter employee Name : ")
    #     esal=float(input('Enter Employee Salary: '))
    #     eaddr=input("Enter Employee Address: ")
    #     query="insert into employees values(%d,'%s','%f','%s')"
    # cursor.execute(query %(eno,ename,esal,eaddr))
    # con.commit()
    # print("Record Inserted Successfully")
    
except cx_Oracle.DatabaseError as e:
    print("There is problem with db: ",e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        
        
        
        
        
        

        
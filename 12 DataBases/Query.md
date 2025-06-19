
"create table employees(eno number,ename varchar2(10),esal number(10,20))"

drop table employees

"insert into employees values(100,'Mayur',1000,'shirpur'')"


executemany()

query="insert into employees values(:eno,:ename,:esal,:eaddr)"
records=[(200,'Sunny',2000,'Mumbai'),(300,'Bunny',3000,'Hyd'),(400,'chinny',400,'chennai')]
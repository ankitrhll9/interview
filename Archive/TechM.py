[2:38 PM] Nikhil Gopalrao Sontakke
There is csv file with 

";" delimiter, 

without header, 

1) read csv file in spark by providing schema (empid, empname, dept, salary, join_date).

2) split the empname to generate firstname , middlename and lastname. Use delimiter (" "). 

3) Display the second max salaried employee's data for each department (firstname, middlename, lastname, empid, dept and salary ) .

df1 = spark.read.csv("emp.csv",header=True,schema="empid int,empname string,dept string,salary int,join_date string")
df2 = df1[1].split(" ")
df3 = df2.split(" ")
df3.show()

spark.sql("select * max(salary) from emp where salary not in (select max(salary) from emp) group by dept").show()


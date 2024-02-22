
-- SELECT * from employee

-- To find the manager of each employee --
-- SELECT
--     E1.EmployeeName AS EmployeeName,
--     E2.EmployeeName AS ManagerName
-- FROM
--     Employee E1
-- LEFT JOIN
--     Employee E2 ON E1.ManagerID = E2.EmployeeID;


-- Rank and Dense_rank --
-- SELECT EmployeeName, Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as ranking FROM Employee;

-- 4th highest salary
-- SELECT * FROM (
--     SELECT EmployeeName, Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as Sal_rank from employee
--     ) as derived_table WHERE Sal_rank = 4


-- MAX Salary in each department --
-- SELECT EmployeeName,Department,Salary FROM
--     (SELECT EmployeeName,Department,Salary, RANK() OVER (
--     PARTITION BY Department
--     ORDER BY Salary DESC
--     ) as max_sal FROM employee) as derived_table
--     WHERE max_sal = 1;

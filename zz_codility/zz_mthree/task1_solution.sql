/* 
department table has primary key id

employee has primary key id
         has foreign key dept_id
         has integer     salary
*/

/*
The task, if I remember it correctly, is:
Given department and employee,
give an SQL query that produces
a table with one row for each department
that hires at least one employee,
along with the number of employees the department employs,
and the sum of salaries the department pays out,
ordered by dept_id in increasing order.
*/

SELECT dept_id, COUNT(dept_id) AS _count, SUM(salary) AS sum_of_salary
  FROM department JOIN employee ON department.id = employee.dept_id
  GROUP BY dept_id
  HAVING COUNT(dept_id) > 0
  ORDER BY dept_id ASC

/*
I think
  'HAVING COUNT(dept_id) > 0'
can be omitted since JOIN is really an INNER JOIN,
but to be on the safe side, I've left it in.
*/
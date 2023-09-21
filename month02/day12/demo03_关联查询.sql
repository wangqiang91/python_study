use stu;
select  * from class,hobby;
select c.name,c.age,c.sex,h.hobby,h.price  from class c,hobby h where c.name = h.name;
select p.name,p.salary,d.dname from person p,dept d where p.dept_id = d.id and p.salary >= 20000;

-- 内连接
select p.name,p.salary,d.dname from person p INNER JOIN dept d ON p.dept_id = d.id where p.salary >= 20000;
-- 外连接-左连接
select p.name,p.salary,d.dname from person p left JOIN dept d ON p.dept_id = d.id where p.salary >= 20000;
-- 外连接-右连接
select d.dname,count(p.name) from person p right JOIN dept d ON p.dept_id = d.id GROUP BY d.dname; 


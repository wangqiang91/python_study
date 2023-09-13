use stu

select name 姓名 from class 

-- 复合排序
select * from class order by age DESC,score DESC;

use exercise
select * from books order by press_time DESC,price ASC;

select * from class where sex = "w" order by score desc limit 1 OFFSET 1 ;

-- 子查询：
select * from (select * from class where sex = "w") w where score > 60;
select * from class where score > (select score from class where id = 5);






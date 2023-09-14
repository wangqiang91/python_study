use stu;
-- 聚合函数
select AVG(attack) 平均攻击力,MAX(attack),MIN(attack),SUM(attack) from sanguo;

-- 聚合分组 
select country,AVG(attack)  from sanguo where gender = "男" GROUP BY country;

select country,gender,count(*) from sanguo group by country,gender;

select country,count(gender)  from sanguo where gender = "男" GROUP BY country ORDER BY COUNT(gender) DESC LIMIT 1

select country,AVG(attack)  from sanguo GROUP BY country HAVING AVG(attack) > 250;

select country,COUNT(*) 男性英雄数量 from sanguo where gender = "男" GROUP BY country HAVING COUNT(*) >2 ORDER BY COUNT(*) DESC;

-- 去除重复的数据
select DISTINCT country from sanguo;
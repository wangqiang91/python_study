use exercise

select * from books where price >= 30 and price < 40;
select * from books where press = "人民教育";
select * from books where author = "老舍" and press = "中国文学";
select * from books where comment != "";
select bname,price from books where price > 60;
select * from books where author in ("鲁迅","矛盾")

update books set price = 45 where bname = "呐喊";
alter Table books ADD press_time date after price;
UPDATE books set press_time = "2018-10-1" where author = "老舍";
UPDATE books set press_time = "2020-1-1" where press = "中国文学" and author != "老舍";
UPDATE books set press_time = "2019-10-1" where press_time is NULL;
update books set price = price+5 where author = "鲁迅";
delete from books where price>70 or price < 40;

use stu
create table sanguo(
id int primary key auto_increment,
name varchar(30),
gender enum('男','女'),
country enum('魏','蜀','吴'),
attack smallint,
defense tinyint
);


insert into sanguo
values (1, '曹操', '男', '魏', 256, 63),
       (2, '张辽', '男', '魏', 328, 69),
       (3, '甄姬', '女', '魏', 168, 34),
       (4, '夏侯渊', '男', '魏', 366, 83),
       (5, '刘备', '男', '蜀', 220, 59),
       (6, '诸葛亮', '男', '蜀', 170, 54),
       (7, '赵云', '男', '蜀', 377, 66),
       (8, '张飞', '男', '蜀', 370, 80),
       (9, '孙尚香', '女', '蜀', 249, 62),
       (10, '大乔', '女', '吴', 190, 44),
       (11, '小乔', '女', '吴', 188, 39),
       (12, '周瑜', '男', '吴', 303, 60),
       (13, '吕蒙', '男', '吴', 330, 71);
select * from sanguo where country = "蜀" order by attack DESC;
update sanguo set attack = 300 where country = "吴" and attack > 300 limit 2;
select name 姓名,attack 攻击力 from sanguo where country = "魏" and attack >200;
select * from sanguo order by attack desc,defense;
select * from sanguo where name like "___";
select * from sanguo where country = "魏" ORDER BY defense desc limit 2 OFFSET 1;
select * from sanguo where gender = "女" and attack > 180 or (gender = "男" and attack < 250);
select * from sanguo where gender = "女" and attack > 180 UNION 
select * from sanguo where gender = "男" and attack < 250;
select * from sanguo where attack > (select attack from sanguo where country = "魏" order by attack DESC limit 1)  and country = "蜀"

use exercise;
select author,AVG(price)  from books GROUP BY author;
select press,COUNT(*) from books GROUP BY press;
select press_time,MAX(price),MIN(price)  from books GROUP BY press_time;
select press,AVG(price) from books GROUP BY press HAVING MAX(price)  > 50 ORDER BY AVG(price) DESC

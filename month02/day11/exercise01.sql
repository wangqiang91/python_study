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
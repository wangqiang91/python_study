use exercise;
delimiter $$
create function func01_books01(name1 VARCHAR(30),name2 VARCHAR(30)) returns float
BEGIN
return (select price from books where bname = name1) - (select price from books where bname = name2);
end $$
delimiter ;

select func01_books01("骆驼祥子","边城");
select func01_books01("边城","骆驼祥子");

drop Function func01_books;

delimiter !!
create procedure change_price()
BEGIN
    update books SET price = price+5 where press_time >= "2020-01-01";
    update books set price = price * 0.8 where press_time < "2020-01-01";
    select * from books order by price desc;
END !!
delimiter ;
call change_price();

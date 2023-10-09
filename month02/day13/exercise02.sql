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
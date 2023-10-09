use stu;
delimiter !!
create procedure pro01()
BEGIN
update class set score = 96 where id = 1;
select * from class order by score;
END !!
delimiter ;
call pro03();
-- 使用in入参，可以直接填入对应数据，也可以使用变量，数值不会随函数改变而改变；
delimiter $$
create procedure proce_in(in num int)
BEGIN
    select num;
    set num = 100;
    select num;
END $$
delimiter ;

set @n = 1;
call proce_in(@n);
select @n;
-- 使用out入参，一定要填入变量，且变量会随着函数改变而改变；
delimiter $$
create procedure proce_out(out num int)
BEGIN
    select num;
    set num = 100;
    select num;
END $$
delimiter ;

set @n = 1;
call proce_out(@n);
select @n;
set global log_bin_trust_function_creators=TRUE;
use stu
-- 定义一个函数
DELIMITER $$
CREATE Function func01() returns int 
BEGIN
    return(SELECT score from class order by score desc limit 1);
END $$
DELIMITER ;

SELECT func01();
select * from class where score >= func01();

delimiter //
create Function func02(uid1 int,uid2 int) returns int
BEGIN
declare val1 float;
declare val2 float default 0;
set val1 = (select score from class where id = uid1);
select score from class where id = uid2 into val2;
return val1 - val2;
end //
delimiter ;
select func02(4,6)

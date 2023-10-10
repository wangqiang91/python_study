-- 分支选择if语句：
-- if 条件 then
--     语句块
-- elif 条件 then
--         语句块
-- else
--     语句块
-- end if;
use stu;
delimiter !!
create procedure proc_add_score(in name1 varchar(5))
BEGIN
    declare s char DEFAULT "o";
    set s = (select sex from class where name = name1);
    if s = "o" then
        update class set score = score+3 where name = name1;
    else
        update class set score = score + 2 where name = name1;
    end if;
END !!
delimiter ;

call proc_add_score("王三欢");

-- case分支语句：
-- case [变量]
--     when 条件 then
--         语句；
--     when 条件 THEN
--         语句；
--     ....
--      else
--          语句；
-- END case;

delimiter ##
create procedure pro_t1(in name1 varchar(30))
BEGIN
    declare val1 varchar(5) default "o";
    set val1 = (select sex from class where name = name1);
    case val1
        when "w" THEN
            select "女孩子";
        when "m" THEN
            select "he is a boy";
        ELSE
            select "sorry i do not know";
    end case;
END ##
delimiter ;
call pro_t1("王大强");


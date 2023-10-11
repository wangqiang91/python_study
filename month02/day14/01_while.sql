use stu;
delimiter !!
create procedure proc_t2()
begin
    declare var int default 1;
    while var < 5 DO
        select * from class where id = var;
        set var = var+1;
    end while;
END !!
delimiter ;

CALL proc_t2();


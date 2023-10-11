use exercise;
delimiter $$
create procedure change_price03(in bname1 varchar(30))
BEGIN
    DECLARE author1 VARCHAR(30);
    DECLARE press1 VARCHAR(30);
    set author1 = (select author from books where bname = bname1);
    set press1 = (select press from books where bname = bname1);
    if author1 = "鲁迅" then
        update books set comment = "鲁迅" where bname = bname1;
    end if;   
    case press1
        when "中国文学" THEN
            update books set price= price+5 where bname = bname1;
        when "机械工业" THEN
            update books set price= price-2 where bname = bname1;
        when "人民教育" THEN
            update books set price= price+3 where bname = bname1;
    end case;
END $$
delimiter ;
call change_price02();

delimiter !!
create procedure total_price(in n int)
BEGIN
    declare i int default 0;
    declare total_price float default 0;
    while i < n do
        set total_price = total_price + (select price from books ORDER BY price desc limit 1 OFFSET i );
        set i = i+1;
    end while;
    select total_price "总价";
END !!
delimiter ;
call total_price(3);
select price from books ORDER BY price DESC;
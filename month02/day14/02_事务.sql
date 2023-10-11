use stu;
begin;
update class set score = 107 where id = 1;
select * from class;
-- DELETE from class where id = 6;
ROLLBACK;
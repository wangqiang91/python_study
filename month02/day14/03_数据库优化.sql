show engines;  --查看系统中的引擎

alter table XXX engine = myisam; --修改引擎

-- sql语句检测工具；
use stu;
explain select score from class where id = 3  \G;

-- 复制表及表数据；
create table good_stu select * from class where score > 70;
select * from good_stu;

create DATABASE stu_bak;

drop database stu_bak;


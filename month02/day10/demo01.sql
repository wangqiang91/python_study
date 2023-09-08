-- 查看现有的数据库
show DATABASEs;
use school
select DATABASE()
-- 删除数据库
drop database 

use stu
create table student(
    name char(20),
    age TINYINT,
    sex ENUM("男","女"),
    height float
)
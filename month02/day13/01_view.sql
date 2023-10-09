use stu;

-- 单表构建视图
create or REPLACE VIEW class_view as select name,age,score from class where score >= 80;

-- 多表构建视图:可以正常查询，但不能删除数据，修改数据时只能修改一张表的值，不能同时修改两张表的数据；
CREATE or REPLACE VIEW class_hobby_view as select class.name,class.score,hobby.hobby,hobby.price from class,hobby where class.name = hobby.name;

show full TABLEs in stu;
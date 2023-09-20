use stu;
CREATE TABLE dept (
    id int PRIMARY KEY auto_increment,
    dname VARCHAR(50) not null);
insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');
CREATE TABLE person (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(32) NOT NULL,
  age tinyint unsigned,
  salary decimal(8,2),
  dept_id int
) ;
insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);

alter table person add FOREIGN KEY (dept_id) REFERENCES dept(id);

SHOW CREATE TABLE person;
show index from person;

alter Table person DROP FOREIGN KEY person_ibfk_1;

alter Table person add FOREIGN KEY (dept_id) REFERENCES dept(id) on delete CASCADE on update CASCADE;

update dept set id = 7 where id = 3;

alter Table person add FOREIGN KEY (dept_id) REFERENCES dept(id) on delete set NULL on update set NULL;

update dept set id = 3 where id = 7;

-- 多对多的关系
CREATE table athlete(
  id int AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(30),
  age TINYINT NOT NULL,
  country VARCHAR(30) NOT NULL
);
create Table sports(
  id int PRIMARY KEY AUTO_INCREMENT,
  sport VARCHAR(30) NOT NULL
);
CREATE Table athlete_sports (
  id int PRIMARY key AUTO_INCREMENT,
  aid int,
  sid int,
  FOREIGN KEY (aid) REFERENCES athlete(id),
  FOREIGN KEY (sid) REFERENCES sports(id)
);
ALTER Table athlete_sports add rangking int after sid;


-- 查看现有的数据库
show DATABASEs;
use school
select DATABASE()
-- 删除数据库
drop database 

use stu
create table student(
    id int,
    name char(20),
    age TINYINT,
    sex ENUM("男","女"),
    height float
)

create  TABLE class(
    id int UNSIGNED PRIMARY KEY  AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL ,
    age TINYINT UNSIGNED ,
    sex ENUM("m","w"),
    score FLOAT UNSIGNED DEFAULT '0' 
)

CREATE Table hobby(
    id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    hobby SET("sing","dance","draw") NOT NULL,
    level VARCHAR(30) COMMENT "初始评级",
    price DECIMAL(7,2),
    remark TEXT
)

DESC hobby

SHOW CREATE TABLE class

DROP Table student

CREATE DATABASE exercise  DEFAULT CHARACTER SET utf8
use exercise
CREATE TABLE books(
    id INT PRIMARY KEY AUTO_INCREMENT,
    bname VARCHAR(30) NOT NULL,
    author VARCHAR(30) DEFAULT "",
    press VARCHAR(30) DEFAULT "",
    price DECIMAL(5,2) UNSIGNED DEFAULT '0',
    `comment` TEXT
)


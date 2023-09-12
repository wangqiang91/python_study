use stu

update class set age = 18,score=92 where name = "王三强"

alter Table hobby ADD phone CHAR(11) after price

alter Table hobby MODIFY phone VARCHAR(20)

alter Table hobby CHANGE phone tel VARCHAR(20) DEFAULT "13052256000"

create table marathon(
    id int primary key auto_increment,
    athlete VARCHAR(32),
    birthday DATE,
    r_time TIMESTAMP COMMENT "报名时间",
    performance time
)

INSERT into marathon VALUES(3,"亚拉索","1992-7-12","2023-08-10 9:32:24","2:40:20")

select * from marathon where performance < "2:30:00"

alter Table marathon MODIFY r_time DATETIME DEFAULT now() COMMENT "报名时间"
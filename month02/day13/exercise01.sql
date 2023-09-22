use exercise;
create table class(
    cid int primary key auto_increment,
    caption char(4) not null);
                  
create table teacher(
    tid int primary key auto_increment,
    tname varchar(32) not null);
                    
create table student(
    sid int primary key auto_increment,
    sname varchar(32) not null,
    gender enum('male','female','others') not null default 'male',
    class_id int,
    foreign key(class_id) references class(cid) 
    on update cascade on delete cascade);
                    
create table course(cid int primary key auto_increment,
    cname varchar(16) not null,
    teacher_id int,
    foreign key(teacher_id) references teacher(tid)
    on update cascade on delete cascade);
                   
create table score(sid int primary key auto_increment,
    student_id int,
    course_id int,
    number int(3) not null,
    foreign key(student_id) references student(sid)
    on update cascade on delete cascade,
    foreign key(course_id) references course(cid)
    on update cascade on delete cascade);

insert into class(caption) values('三年一班'),('三年二班'),('三年三班');
insert into teacher(tname) values('魏老师'),('祁老师'),('小泽老师');
insert into student(sname,gender,class_id) values('钢蛋','female',1),('铁锤','female',1),('山炮','male',2),('彪哥','male',3),('虎子','male',3),('妞妞','female',2),('建国','male',2);
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100),(3,2,78),(4,3,66),(2,3,78),(5,2,77),(6,1,84),(7,1,79),(5,3,80),(3,1,59);


select p1.tid,p1.tname,COUNT(p2.cname) from teacher p1 left join course p2 on p1.tid = p2.teacher_id GROUP BY p1.tid;
select p1.cid,p1.cname,MAX(p2.number) 最高分,MIN(p2.number) 最低分 from course p1 left join score p2 on p1.cid = p2.course_id
GROUP BY p1.cid;
select s.student_id,t.sname,AVG(s.number)  from score s left join student t on s.student_id = t.sid GROUP BY s.student_id HAVING AVG(s.number) > 85;
select s.student_id,s.course_id,s.number,t.sname from score s 
left join student t on s.student_id = t.sid 
where s.course_id = 2 and s.number > 80;
select s.course_id,c.cname,COUNT(*) from score s left join course c on c.cid = s.course_id group by s.course_id;
select s.student_id,d.sname,c.caption,AVG(s.number) from score s
left join student d on s.student_id = d.sid
left join class c on d.class_id = c.cid
GROUP BY s.student_id;

select p1.sid,p1.sname,p2.caption,AVG(p3.number) from student p1
left join class p2 on p1.class_id = p2.cid
left JOIN score p3 on p1.sid = p3.student_id
GROUP BY p1.sid;


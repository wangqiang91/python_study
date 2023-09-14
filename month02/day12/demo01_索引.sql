use stu;
CREATE Table index_test(
    id int AUTO_INCREMENT,
    name VARCHAR(30),
    PRIMARY KEY (id),
    UNIQUE nameindex(name)
)
desc index_test
show create table index_test
show index from class

CREATE  INDEX age on class(age)

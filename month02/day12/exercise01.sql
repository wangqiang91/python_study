use exercise;
create Table user (
    id int PRIMARY KEY auto_increment,
    username VARCHAR(50),
    password VARCHAR(30),
    tel char(18)
);
CREATE Table circle_friend(
    id int PRIMARY KEY auto_increment,
    pic VARCHAR(200),
    content TEXT,
    set_time datetime,
    address VARCHAR(50),
    uid int,
    foreign key (uid) REFERENCES user(id)
);
create Table like_comment(
    id int PRIMARY KEY auto_increment,
    cid int,
    `like` BIT DEFAULT 0,
    `comment` VARCHAR(500),
    uid int,
    foreign key (cid) REFERENCES circle_friend(id),
    FOREIGN key (uid) REFERENCES user(id)
);

CREATE Table author(
    id int PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(20) NOT NULL,
    sex ENUM("男","女")
);
CREATE Table press(
    id int PRIMARY KEY AUTO_INCREMENT,
    press_name VARCHAR(20) NOT NULL,
    address VARCHAR(50)
);
CREATE Table book(
    id int primary key auto_increment,
    name VARCHAR(20),
    price DECIMAL(5,2),
    `comment` TEXT COMMENT "图书的描述",
    press_time DATETIME,
    aid int,
    pid int,
    FOREIGN KEY (aid) REFERENCES author(id),
    FOREIGN KEY (pid) REFERENCES press(id) on delete set NULL on update set NULL
);

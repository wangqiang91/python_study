-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: stu
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `athlete`
--

DROP TABLE IF EXISTS `athlete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `athlete` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `age` tinyint NOT NULL,
  `country` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `athlete`
--

LOCK TABLES `athlete` WRITE;
/*!40000 ALTER TABLE `athlete` DISABLE KEYS */;
/*!40000 ALTER TABLE `athlete` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `athlete_sports`
--

DROP TABLE IF EXISTS `athlete_sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `athlete_sports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `aid` int DEFAULT NULL,
  `sid` int DEFAULT NULL,
  `rangking` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `aid` (`aid`),
  KEY `sid` (`sid`),
  CONSTRAINT `athlete_sports_ibfk_1` FOREIGN KEY (`aid`) REFERENCES `athlete` (`id`),
  CONSTRAINT `athlete_sports_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `sports` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `athlete_sports`
--

LOCK TABLES `athlete_sports` WRITE;
/*!40000 ALTER TABLE `athlete_sports` DISABLE KEYS */;
/*!40000 ALTER TABLE `athlete_sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` tinyint unsigned DEFAULT NULL,
  `sex` enum('m','w','o') CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `score` float unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `age` (`age`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'王大欢',16,'w',103),(2,'王大强',18,'m',85),(3,'王二欢',19,'w',90),(4,'王三欢',17,'o',68),(5,'王二强',20,'m',77),(6,'王三强',18,'m',92);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `class_hobby_view`
--

DROP TABLE IF EXISTS `class_hobby_view`;
/*!50001 DROP VIEW IF EXISTS `class_hobby_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `class_hobby_view` AS SELECT 
 1 AS `name`,
 1 AS `score`,
 1 AS `hobby`,
 1 AS `price`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `class_view`
--

DROP TABLE IF EXISTS `class_view`;
/*!50001 DROP VIEW IF EXISTS `class_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `class_view` AS SELECT 
 1 AS `name`,
 1 AS `age`,
 1 AS `score`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dept` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept`
--

LOCK TABLES `dept` WRITE;
/*!40000 ALTER TABLE `dept` DISABLE KEYS */;
INSERT INTO `dept` VALUES (1,'技术部'),(2,'销售部'),(3,'市场部'),(4,'行政部'),(5,'财务部'),(6,'总裁办公室');
/*!40000 ALTER TABLE `dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `good_stu`
--

DROP TABLE IF EXISTS `good_stu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `good_stu` (
  `id` int unsigned NOT NULL DEFAULT '0',
  `name` varchar(30) NOT NULL,
  `age` tinyint unsigned DEFAULT NULL,
  `sex` enum('m','w','o') CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `score` float unsigned DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `good_stu`
--

LOCK TABLES `good_stu` WRITE;
/*!40000 ALTER TABLE `good_stu` DISABLE KEYS */;
INSERT INTO `good_stu` VALUES (1,'王大欢',16,'w',103),(2,'王大强',18,'m',85),(3,'王二欢',19,'w',90),(5,'王二强',20,'m',77),(6,'王三强',18,'m',92);
/*!40000 ALTER TABLE `good_stu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hobby`
--

DROP TABLE IF EXISTS `hobby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hobby` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `hobby` set('sing','dance','draw') NOT NULL,
  `level` varchar(30) DEFAULT NULL COMMENT '初始评级',
  `price` decimal(7,2) DEFAULT NULL,
  `tel` varchar(20) DEFAULT '13052256000',
  `remark` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hobby`
--

LOCK TABLES `hobby` WRITE;
/*!40000 ALTER TABLE `hobby` DISABLE KEYS */;
INSERT INTO `hobby` VALUES (1,'王大欢','sing,dance','A',36800.00,NULL,'兴趣爱好的描述呀呀呀嘿'),(2,'王二欢','sing','B',16800.00,NULL,'兴趣爱好的描述呀呀呀呀'),(3,'TEST01','sing','C',66800.00,NULL,'兴趣爱好的描述呀呀呀呀'),(4,'TEST02','draw','C',26800.00,NULL,''),(5,'王大强','draw','A',6800.00,NULL,''),(6,'王二强','dance,draw','A',62800.00,NULL,'');
/*!40000 ALTER TABLE `hobby` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_test`
--

DROP TABLE IF EXISTS `index_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `index_test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nameindex` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_test`
--

LOCK TABLES `index_test` WRITE;
/*!40000 ALTER TABLE `index_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `index_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marathon`
--

DROP TABLE IF EXISTS `marathon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marathon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `athlete` varchar(32) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `r_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '报名时间',
  `performance` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marathon`
--

LOCK TABLES `marathon` WRITE;
/*!40000 ALTER TABLE `marathon` DISABLE KEYS */;
INSERT INTO `marathon` VALUES (1,'拉斐尔','1990-12-20','2023-08-06 14:30:50','02:15:20'),(2,'凯奇','1994-07-12','2023-09-10 09:35:24','02:10:20'),(3,'亚拉索','1992-07-12','2023-08-10 09:32:24','02:40:20');
/*!40000 ALTER TABLE `marathon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint unsigned DEFAULT NULL,
  `salary` decimal(8,2) DEFAULT NULL,
  `dept_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'Lily',29,20000.00,2),(2,'Tom',27,16000.00,1),(3,'Joy',30,28000.00,1),(4,'Emma',24,8000.00,4),(5,'Abby',28,17000.00,NULL),(6,'Jame',32,22000.00,NULL);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo`
--

DROP TABLE IF EXISTS `sanguo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sanguo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  `country` enum('魏','蜀','吴') DEFAULT NULL,
  `attack` smallint DEFAULT NULL,
  `defense` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo`
--

LOCK TABLES `sanguo` WRITE;
/*!40000 ALTER TABLE `sanguo` DISABLE KEYS */;
INSERT INTO `sanguo` VALUES (1,'曹操','男','魏',256,63),(2,'张辽','男','魏',328,69),(3,'甄姬','女','魏',168,34),(4,'夏侯渊','男','魏',366,83),(5,'刘备','男','蜀',220,59),(6,'诸葛亮','男','蜀',170,54),(7,'赵云','男','蜀',377,66),(8,'张飞','男','蜀',370,80),(9,'孙尚香','女','蜀',249,62),(10,'大乔','女','吴',190,44),(11,'小乔','女','吴',188,39),(12,'周瑜','男','吴',300,60),(13,'吕蒙','男','吴',300,71);
/*!40000 ALTER TABLE `sanguo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sports`
--

DROP TABLE IF EXISTS `sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sport` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sports`
--

LOCK TABLES `sports` WRITE;
/*!40000 ALTER TABLE `sports` DISABLE KEYS */;
/*!40000 ALTER TABLE `sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `class_hobby_view`
--

/*!50001 DROP VIEW IF EXISTS `class_hobby_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `class_hobby_view` AS select `class`.`name` AS `name`,`class`.`score` AS `score`,`hobby`.`hobby` AS `hobby`,`hobby`.`price` AS `price` from (`class` join `hobby`) where (`class`.`name` = `hobby`.`name`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `class_view`
--

/*!50001 DROP VIEW IF EXISTS `class_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `class_view` AS select `class`.`name` AS `name`,`class`.`age` AS `age`,`class`.`score` AS `score` from `class` where (`class`.`score` >= 80) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-12 17:54:51

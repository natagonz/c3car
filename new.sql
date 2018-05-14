-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: c3carwash
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounting`
--

DROP TABLE IF EXISTS `accounting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(300) DEFAULT NULL,
  `location` varchar(300) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `cashier` varchar(200) DEFAULT NULL,
  `pakets` blob,
  `customer` varchar(200) DEFAULT NULL,
  `member` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting`
--

LOCK TABLES `accounting` WRITE;
/*!40000 ALTER TABLE `accounting` DISABLE KEYS */;
INSERT INTO `accounting` VALUES (13,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-10 10:40:22','k1','€]q.','DK 456 RI','-'),(14,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-11 19:02:11','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1509 MS','-'),(15,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-11 19:03:03','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1378 UT','-'),(17,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-12 14:52:57','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 511 LA','-'),(18,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-12 16:33:18','k1','€]q.','DK 1682 KU','-'),(19,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-13 10:51:28','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1582 OH','-'),(20,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-13 12:19:02','k1','€]qX\0\0\0Free ladies driver (nonlift)qa.','DK 746 KR','-'),(21,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-13 12:28:14','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1597 SJ','-'),(22,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-13 13:47:42','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1981 AI','-'),(23,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-13 14:47:41','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1287 KZ','-'),(24,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-13 14:47:48','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1989 NN','-'),(25,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-13 15:57:02','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1030 COD','-'),(26,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-14 08:25:15','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 985 BH','-'),(27,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-14 10:13:23','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 708 FO','-'),(28,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-14 10:32:27','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 874 AT','-'),(29,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-14 10:32:42','k1','€]q.','','-'),(30,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-14 15:53:08','k1','€]qX\0\0\0Free ladies driver (nonlift)qa.','DK 1042 DE','-'),(31,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-16 09:41:57','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 248 KD','-'),(32,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-16 13:45:47','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 952 KU','-'),(33,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-16 16:36:20','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','Dk 333 lo','-'),(34,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-16 16:36:30','k1','€]q.','DK1VD','-'),(35,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-17 09:06:16','k1','€]q.','Avanza','-'),(36,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-17 09:06:23','k1','€]qX\0\0\0Cling reguler (lift)qa.','Avanza','-'),(37,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-17 10:44:51','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1009 DG','-'),(38,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-17 16:48:37','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','B 1185 NOI','-'),(39,'Pembayaran dari customer','Batubulan',180000,'Income','2018-04-18 09:43:12','k1','€]qX\0\0\0Cling Premium ( lift )qa.','DK 1217 BQ','-'),(40,'Pembayaran dari customer','Batubulan',180000,'Income','2018-04-18 09:49:08','k1','€]qX\0\0\0Cling Premium ( lift )qa.','DK 1217 BQ','-'),(41,'Pembayaran dari customer','Batubulan',240000,'Income','2018-04-18 09:49:47','k1','€]q(X\0\0\0Cling reguler (lift)qX\0\0\0Cling Premium ( lift )qe.','DK 1217 BQ','-'),(42,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-18 10:10:35','k1','€]q.','DK 1217 BQ','-'),(43,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-18 10:19:21','k1','€]q.','','-'),(44,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-18 10:25:57','k1','€]qX\0\0\0Cling reguler (lift)qa.','B 279 UNI','-'),(45,'Pembayaran dari customer','Batubulan',180000,'Income','2018-04-18 13:55:37','k1','€]qX\0\0\0Cling Premium ( lift )qa.','DK 1226UV','-'),(46,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-20 08:23:20','k1','€]qX \0\0\0Free voucher asuransi (non lift)qa.','DK 1217 BQ','-'),(47,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-20 16:05:46','k1','€]q.','DK1VD','-'),(48,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-20 16:09:08','k1','€]q.','','-'),(49,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-20 16:09:22','k1','€]q.','Dk 1379 IV','Cuci + lift + Vacum'),(50,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-24 09:07:25','k1','€]qX\0\0\0Free ladies premium washqa.','DK 631 IN','-'),(51,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-26 16:36:57','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1937 WH','-'),(52,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-27 09:13:45','k1','€]q.','Dk 1379 IV','Cuci + lift + Vacum'),(53,'Pembayaran dari customer','Batubulan',600000,'Income','2018-04-27 15:20:38','k1','€]qX\n\0\0\0Poles bodyqa.','DK 1310 LI','-'),(54,'Pembayaran dari customer','Batubulan',35000,'Income','2018-04-27 16:51:08','k1','€]qX\0\0\0Cling reguler expresqa.','DK 1982 OR','-'),(55,'Pembayaran dari customer','Batubulan',60000,'Income','2018-04-27 16:51:12','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1009 DG','-'),(56,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-30 08:47:23','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1217 BQ','-'),(57,'Pembayaran dari customer','Batubulan',0,'Income','2018-04-30 13:15:00','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1226 UV','-'),(58,'Pembayaran dari customer','Batubulan',600000,'Income','2018-05-01 13:19:38','k1','€]qX\n\0\0\0Poles bodyqa.','DK 1252 LS','-'),(59,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-02 15:00:32','k1','€]q.','Dk 1379 IV','Cuci + lift + Vacum'),(60,'Pembayaran dari customer','Batubulan',60000,'Income','2018-05-03 09:29:39','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1526 UM','-'),(61,'Pembayaran dari customer','Batubulan',70000,'Income','2018-05-03 09:50:33','k1','€]q(X\0\0\0Cling reguler (lift)qX\0\0\0Oli plastikqe.','DK 1526 UM','-'),(62,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-04 09:28:40','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1217 BQ','-'),(63,'Pembayaran dari customer','Batubulan',60000,'Income','2018-05-04 16:02:10','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1336 DZ','-'),(64,'Pembayaran dari customer','Batubulan',1810000,'Income','2018-05-05 10:19:59','k1','€]q(X\0\0\0Cling reguler (lift)qX#\0\0\0Anti karat lantai. ( atas & bawah )qX\"\0\0\0Free voucher asuransi premium washqe.','DK 1276 FA','-'),(65,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-05 10:21:18','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1276 FA','-'),(66,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-05 13:54:27','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1706 OK','-'),(67,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-05 16:55:52','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','AD 8671 IU','-'),(68,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-05 16:56:01','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1111 KO','-'),(69,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-05 16:56:05','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1466 KS','-'),(70,'Pembayaran dari customer','Batubulan',60000,'Income','2018-05-07 10:36:16','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 963 QS','-'),(71,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-07 15:47:27','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1823 IS','-'),(72,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-07 15:47:33','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','W 675 RZ','-'),(73,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-07 16:14:08','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 672 KM','-'),(74,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-08 10:05:42','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','B 1691 UJL','-'),(75,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-08 14:21:28','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1467 KQ','-'),(76,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-09 08:54:12','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1455 KR','-'),(77,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-09 11:39:13','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1922 IV','-'),(78,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-09 14:45:11','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1104 FT','-'),(79,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-09 14:45:13','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 8704 FI','-'),(80,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-09 15:41:46','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1787 MH','-'),(81,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-09 15:51:34','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1811 KQ','-'),(82,'Pembayaran dari customer','Batubulan',60000,'Income','2018-05-09 16:01:06','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1718 KU','-'),(83,'Pembayaran dari customer','Batubulan',60000,'Income','2018-05-10 09:57:27','k1','€]qX\0\0\0Cling reguler (lift)qa.','DK 1009 DG','-'),(84,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 10:00:46','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1105 CR','-'),(85,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 10:44:08','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1787 PG','-'),(86,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 11:18:40','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 716 BL','-'),(87,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 13:14:17','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1937 UM','-'),(88,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 13:44:48','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1702 ON','-'),(89,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 14:50:19','k1','€]q.','Dk 1379 IV','Cuci + lift + Vacum'),(90,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 15:51:14','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1319 FU','-'),(91,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-10 16:51:01','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1849 KW','-'),(92,'Pembayaran dari customer','Batubulan',35000,'Income','2018-05-11 09:45:46','k1','€]qX\0\0\0Cling reguler expresqa.','DK 1982 OR','-'),(93,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-11 11:27:37','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1393 KI','-'),(94,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-11 11:27:40','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1338 DM','-'),(95,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-11 13:23:08','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1287 KZ','-'),(96,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-11 14:24:13','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1445 MS','-'),(97,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-11 15:56:40','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1445 MF','-'),(98,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-11 15:56:42','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 922 KY','-'),(99,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 14:10:50','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 836 KS','-'),(100,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 14:11:00','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1309 LA','-'),(101,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 14:11:03','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 769 AK','-'),(102,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 14:11:05','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1519 KO','-'),(103,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 15:32:15','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1535 BU','-'),(104,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 15:32:18','k1','€]qX\0\0\0Free ladies premium washqa.','DK 746 KR','-'),(105,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-12 16:01:49','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','B 1383 CFS','-'),(106,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-14 14:06:57','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1528 SE','-'),(107,'Pembayaran dari customer','Batubulan',0,'Income','2018-05-14 14:29:17','k1','€]qX\"\0\0\0Free voucher asuransi premium washqa.','DK 1217 BQ','-');
/*!40000 ALTER TABLE `accounting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `mobil` varchar(100) DEFAULT NULL,
  `plat` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `paket` varchar(200) DEFAULT NULL,
  `tambahan` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `owner` int(11) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `payment` varchar(200) DEFAULT NULL,
  `treatment` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (22,'Epik','','0812345678','Xenia','DK 456 RI','Out','regular',NULL,NULL,'2018-04-10 08:53:33',0,44,'Batubulan','Lunas','-'),(23,'Mr. Gede Kertayasa Putra','','','Toyota avanza','DK 1378 UT','Out','regular',NULL,NULL,'2018-04-11 17:17:35',0,44,'Batubulan','Lunas','-'),(24,'Mr. I Nyoman Ladri','','085205871183','Suzuki APV','DK 1509 MS','Out','regular',NULL,NULL,'2018-04-11 17:19:08',0,44,'Batubulan','Lunas','-'),(29,'Yudi','bossssku@gmail.com','085737652288','Karimun','Dk 333 lo','Out','regular',NULL,NULL,'2018-04-12 23:55:05',0,1,'Batubulan','Lunas','-'),(30,'Mr. Gatot','beranda77@gmail.com','087761712147','Ayla','DK 1582 OH','Out','regular',NULL,NULL,'2018-04-13 10:50:38',60000,44,'Batubulan','Lunas','-'),(31,'Mrs.Sukma','','085237199789','Agya','DK 746 KR','Out','regular',NULL,NULL,'2018-04-13 12:13:26',0,44,'Batubulan','Lunas','-'),(32,'Mr. I Putu Subagia','','082144912300','Honda BRV','DK 1597 SJ','Out','regular',NULL,NULL,'2018-04-13 12:25:23',0,44,'Batubulan','Lunas','-'),(33,'Mr. Putu Agus Marciyasa','','081294038179','Honda Jazz','DK 1981 AI','Out','regular',NULL,NULL,'2018-04-13 12:28:42',0,44,'Batubulan','Lunas','-'),(34,'Mr. Winarta Lesmana Handrea','','','Mitsubishi Xpander','DK 1989 NN','Out','regular',NULL,NULL,'2018-04-13 14:45:13',0,44,'Batubulan','Lunas','-'),(35,'Mr. Dewa Ketut Suparta','','081337129966','Avanza','DK 1287 KZ','Out','regular',NULL,NULL,'2018-04-13 14:46:28',0,44,'Batubulan','Lunas','-'),(36,'PT. Aerotrans Service Indonesia','','','Toyota Innova','DK 1030 COD','Out','regular',NULL,NULL,'2018-04-13 15:56:42',0,44,'Batubulan','Lunas','-'),(37,'test','','','yaris','DK1VD','Out','regular',NULL,NULL,'2018-04-13 19:17:35',0,44,'Batubulan','Lunas','-'),(38,'Mr. Ida bagus oka','','081236792966','Ayla','DK 985 BH','Out','regular',NULL,NULL,'2018-04-14 08:23:46',60000,44,'Batubulan','Lunas','-'),(39,'','','','','','Out','regular',NULL,NULL,'2018-04-14 09:10:00',0,44,'Batubulan','Lunas','-'),(40,'Mr. Jatiawan','','08123958264','Yaris','DK 708 FO','Out','regular',NULL,NULL,'2018-04-14 10:12:29',60000,44,'Batubulan','Lunas','-'),(41,'Mrs. Linda Ong','','082237659875','Suzuki X-over','DK 874 AT','Out','regular',NULL,NULL,'2018-04-14 10:32:05',0,44,'Batubulan','Lunas','-'),(42,'Mrs. Sukma','','085237199789','APV','DK 1042 DE','Out','regular',NULL,NULL,'2018-04-14 15:52:31',0,44,'Batubulan','Lunas','-'),(43,'Mr. Angga','','081236229779','Honda Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-04-14 16:36:42',180000,44,'Batubulan','Lunas','-'),(44,'Mr. Wayan Sutama','','082144871111','Nissan Atena','DK 248 KD','Out','regular',NULL,NULL,'2018-04-16 09:32:25',0,44,'Batubulan','Lunas','-'),(45,'Mr. Ketut Wirawan','','082147931075','Xenia','DK 952 KU','Out','regular',NULL,NULL,'2018-04-16 13:45:02',0,44,'Batubulan','Lunas','-'),(46,'Mr. Wayan','','081999618123','DK 1379 IF','Avanza','Out','regular',NULL,NULL,'2018-04-17 09:04:36',0,44,'Batubulan','Lunas','-'),(47,'Mr. Wayan','','081999618123','DK 1379 IV','Avanza','Out','regular',NULL,NULL,'2018-04-17 09:05:00',60000,44,'Batubulan','Lunas','-'),(48,'Mr. Komang','','082247072034','Ertiga','DK 1009 DG','Out','regular',NULL,NULL,'2018-04-17 10:44:05',60000,44,'Batubulan','Lunas','-'),(49,'Mr. Agus Suanjaya','','','Mazda 2','B 1185 NOI','Out','regular',NULL,NULL,'2018-04-17 14:13:11',0,44,'Batubulan','Lunas','-'),(50,'Mr. Angga','','081236229779','Honda Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-04-18 09:45:28',0,44,'Batubulan','Lunas','-'),(51,'Mr. Angga','','081236229779','Honda Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-04-18 09:47:49',240000,44,'Batubulan','Lunas','-'),(52,'Mr. Angga','','081236229779','Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-04-18 09:48:40',180000,44,'Batubulan','Lunas','-'),(53,'','','','','','Out','regular',NULL,NULL,'2018-04-18 10:13:08',0,44,'Batubulan','Lunas','-'),(54,'Mr. Agung Asmara','','081337336388','Fortuner','B 279 UNI','Out','regular',NULL,NULL,'2018-04-18 10:24:39',60000,44,'Batubulan','Lunas','-'),(55,'Mr. Yoga','','081936567877','Daihatsu Xenia ','DK 1226UV','Out','regular',NULL,NULL,'2018-04-18 13:54:09',180000,51,'Batubulan','Lunas','-'),(56,'Mr. Angga','','082145779977','Honda Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-04-20 08:17:59',0,44,'Batubulan','Lunas','-'),(57,'test','','','crv','DK1VD','Out','regular',NULL,NULL,'2018-04-20 09:14:54',0,47,'Batubulan','Lunas','-'),(58,'','','','','','Out','regular',NULL,NULL,'2018-04-20 09:16:19',0,44,'Batubulan','Lunas','-'),(59,'Wayan suardana','Cegongboy@gmail.com','081999618123','Avanza','Dk 1379 IV','Out','vip',NULL,NULL,'2018-04-20 10:58:21',0,9,'Batubulan','Lunas','Cuci + lift + Vacum'),(60,'Mrs. Candra','','081320269999','Grand vitara','DK 631 IN','Out','regular',NULL,NULL,'2018-04-24 09:06:56',0,44,'Batubulan','Lunas','-'),(61,'Mr. Agud suastika','','08123560870','Agya','DK 1937 WH','Out','regular',NULL,NULL,'2018-04-26 16:19:42',60000,44,'Batubulan','Lunas','-'),(62,'Wayan suardana','Cegongboy@gmail.com','081999618123','Avanza','Dk 1379 IV','Out','vip',NULL,NULL,'2018-04-27 08:58:37',0,9,'Batubulan','Lunas','Cuci + lift + Vacum'),(63,'Bapak Nyoman ','','08123974407','Avanza','DK 1310 LI','Out','regular',NULL,NULL,'2018-04-27 10:44:35',600000,44,'Batubulan','Lunas','-'),(64,'Mr. Markus','','087780833390','Ayla','DK 1982 OR','Out','regular',NULL,NULL,'2018-04-27 16:21:08',35000,44,'Batubulan','Lunas','-'),(65,'Mr. Komang Sukarta','','082247072034','Ertiga','DK 1009 DG','Out','regular',NULL,NULL,'2018-04-27 16:45:19',60000,44,'Batubulan','Lunas','-'),(66,'Mr. Angga','','082145779977','Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-04-30 08:43:09',0,44,'Batubulan','Lunas','-'),(67,'Mr. Yoga','','081936567877','Xenia','DK 1226 UV','Out','regular',NULL,NULL,'2018-04-30 11:48:58',0,44,'Batubulan','Lunas','-'),(68,'Mr. Agung Alit','','081338283685','Avanza','DK 1252 LS','Out','regular',NULL,NULL,'2018-05-01 13:18:01',600000,44,'Batubulan','Lunas','-'),(69,'Wayan suardana','Cegongboy@gmail.com','081999618123','Avanza','Dk 1379 IV','Out','vip',NULL,NULL,'2018-05-02 13:51:38',0,9,'Batubulan','Lunas','Cuci + lift + Vacum'),(70,'Mr. Dek Can','','081246458731','APV','DK 1526 UM','Out','regular',NULL,NULL,'2018-05-03 09:20:03',60000,44,'Batubulan','Lunas','-'),(71,'Mr. Dek Can','','081246458731','APV','DK 1526 UM','Out','regular',NULL,NULL,'2018-05-03 09:49:50',70000,44,'Batubulan','Lunas','-'),(72,'Mr. Angga','','082145779977','Honda Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-05-04 09:27:48',0,44,'Batubulan','Lunas','-'),(73,'Mr.  Baihaqi','','081916276962','Avanza','DK 1336 DZ','Out','regular',NULL,NULL,'2018-05-04 16:00:08',60000,44,'Batubulan','Lunas','-'),(74,'Asoka Mas','','','Toyota Avanza','DK 1276 FA','Out','regular',NULL,NULL,'2018-05-05 10:16:14',1810000,44,'Batubulan','Lunas','-'),(75,'Asoka Mas','','','Toyota Avanza','DK 1276 FA','Out','regular',NULL,NULL,'2018-05-05 10:21:02',0,44,'Batubulan','Lunas','-'),(76,'Pan Pasifik','','',' Toyota Avanza','DK 1706 OK','Out','regular',NULL,NULL,'2018-05-05 13:41:21',0,44,'Batubulan','Lunas','-'),(77,'Pan Pasifik','','','HRV','AD 8671 IU','Out','regular',NULL,NULL,'2018-05-05 14:31:32',0,44,'Batubulan','Lunas','-'),(78,'ABDA','','','Honda HRV','DK 1111 KO','Out','regular',NULL,NULL,'2018-05-05 16:06:59',0,44,'Batubulan','Lunas','-'),(79,'Cakrawala Proteksi','','','Toyota avanza','DK 1466 KS','Out','regular',NULL,NULL,'2018-05-05 16:17:56',0,44,'Batubulan','Lunas','-'),(80,'Mr. kadek juni antara','','08124663457','INNOVA','DK 963 QS','Out','regular',NULL,NULL,'2018-05-07 09:47:01',60000,44,'Batubulan','Lunas','-'),(81,'RAKSA','','','Honda HRV','W 675 RZ','Out','regular',NULL,NULL,'2018-05-07 14:28:59',0,44,'Batubulan','Lunas','-'),(82,'MAG ','','','Hyundai','DK 1823 IS','Out','regular',NULL,NULL,'2018-05-07 15:37:53',0,44,'Batubulan','Lunas','-'),(83,'BCA','','','Honda CRV','DK 672 KM','Out','regular',NULL,NULL,'2018-05-07 16:04:58',0,44,'Batubulan','Lunas','-'),(84,'pribadi','','','pajero sport hitam','B 1691 UJL','Out','regular',NULL,NULL,'2018-05-08 10:05:08',0,51,'Batubulan','Lunas','-'),(85,'JASINDO','','','Luxio','DK 1467 KQ','Out','regular',NULL,NULL,'2018-05-08 13:17:10',0,44,'Batubulan','Lunas','-'),(86,'WAHANATATA','','','Suzuki Swift ST','DK 1455 KR','Out','regular',NULL,NULL,'2018-05-09 08:33:02',0,44,'Batubulan','Lunas','-'),(87,'JASINDO','','','Toyota Innova','DK 1922 IV','Out','regular',NULL,NULL,'2018-05-09 10:59:25',0,44,'Batubulan','Lunas','-'),(88,'JETWINGS','','','Bus','DK 8704 FI','Out','regular',NULL,NULL,'2018-05-09 14:33:10',0,44,'Batubulan','Lunas','-'),(89,'JASINDO','','','Honda Brio','DK 1104 FT','Out','regular',NULL,NULL,'2018-05-09 14:40:01',0,44,'Batubulan','Lunas','-'),(90,'Astra','','','Toyota Agya','DK 1787 MH','Out','regular',NULL,NULL,'2018-05-09 15:37:53',0,51,'Batubulan','Lunas','-'),(91,'Pribadi','','','Kia Sportage','DK 1811 KQ','Out','regular',NULL,NULL,'2018-05-09 15:49:00',0,51,'Batubulan','Lunas','-'),(92,'Putu Wijaya','','087860250935','Ertiga','DK 1718 KU','Out','regular',NULL,NULL,'2018-05-09 15:59:57',60000,51,'Batubulan','Lunas','-'),(93,'Mr. Komang','','082247072034','Suzuki Ertiga','DK 1009 DG','Out','regular',NULL,NULL,'2018-05-10 09:07:20',60000,44,'Batubulan','Lunas','-'),(94,'PT. Asuransi Umum BCA','','','Honda Mobilio','DK 1105 CR','Out','regular',NULL,NULL,'2018-05-10 09:54:50',0,44,'Batubulan','Lunas','-'),(95,'ASTRA','','','Sigra','DK 1787 PG','Out','regular',NULL,NULL,'2018-05-10 10:35:34',0,44,'Batubulan','Lunas','-'),(96,'ASTRA','','','Splash','DK 716 BL','Out','regular',NULL,NULL,'2018-05-10 11:17:34',0,44,'Batubulan','Lunas','-'),(97,'AXA','','','Splash','DK 1937 UM','Out','regular',NULL,NULL,'2018-05-10 13:13:04',0,44,'Batubulan','Lunas','-'),(98,'ASTRA','','','Avanza','DK 1702 ON','Out','regular',NULL,NULL,'2018-05-10 13:43:45',0,44,'Batubulan','Lunas','-'),(99,'Wayan suardana','Cegongboy@gmail.com','081999618123','Avanza','Dk 1379 IV','Out','vip',NULL,NULL,'2018-05-10 14:07:00',0,9,'Batubulan','Lunas','Cuci + lift + Vacum'),(100,'MAG ','','','Suzuki Ertiga','DK 1319 FU','Out','regular',NULL,NULL,'2018-05-10 15:48:04',0,44,'Batubulan','Lunas','-'),(101,'AXA','','','Kia Rio','DK 1849 KW','Out','regular',NULL,NULL,'2018-05-10 16:36:45',0,44,'Batubulan','Lunas','-'),(102,'Mr. Marcus','','','Ayla','DK 1982 OR','Out','regular',NULL,NULL,'2018-05-11 09:43:10',35000,44,'Batubulan','Lunas','-'),(103,'Pribadi','','','Karimun','DK 1393 KI','Out','regular',NULL,NULL,'2018-05-11 11:11:13',0,44,'Batubulan','Lunas','-'),(104,'Cakrawala Proteksi','','','Kia Sedona Hitam','DK 1338 DM','Out','regular',NULL,NULL,'2018-05-11 11:27:18',0,51,'Batubulan','Lunas','-'),(105,'Mr. Dewa Ketut Suparta','','089691449672','Avanza','DK 1287 KZ','Out','regular',NULL,NULL,'2018-05-11 13:12:54',0,44,'Batubulan','Lunas','-'),(106,'BCA','','','Honda Mobilio','DK 1445 MS','Out','regular',NULL,NULL,'2018-05-11 14:20:41',0,44,'Batubulan','Lunas','-'),(107,'PT. Bess Central Insurance','','','Honda Mobilio','DK 1445 MF','Out','regular',NULL,NULL,'2018-05-11 14:29:06',0,44,'Batubulan','Lunas','-'),(108,'ASTRA','','','Calya','DK 922 KY','Out','regular',NULL,NULL,'2018-05-11 15:15:25',0,44,'Batubulan','Lunas','-'),(109,'MITSUI','','','Hyundai','DK 836 KS','Out','regular',NULL,NULL,'2018-05-12 09:48:04',0,44,'Batubulan','Lunas','-'),(110,'ASTRA','','','Sigra','DK 1309 LA','Out','regular',NULL,NULL,'2018-05-12 09:57:56',0,44,'Batubulan','Lunas','-'),(111,'Pribadi','','','Suzuki X-over','DK 769 AK','Out','regular',NULL,NULL,'2018-05-12 10:12:28',0,44,'Batubulan','Lunas','-'),(112,'Pribadi','','','Avanza','DK 1519 KO','Out','regular',NULL,NULL,'2018-05-12 13:19:19',0,44,'Batubulan','Lunas','-'),(113,'BCA','','','Toyota Alphard','DK 1535 BU','Out','regular',NULL,NULL,'2018-05-12 15:16:55',0,44,'Batubulan','Lunas','-'),(114,'Mrs. Sukma','','085237199789','Agya','DK 746 KR','Out','regular',NULL,NULL,'2018-05-12 15:25:54',0,44,'Batubulan','Lunas','-'),(115,'Astra','','','Nissan march','B 1383 CFS','Out','regular',NULL,NULL,'2018-05-12 15:57:35',0,51,'Batubulan','Lunas','-'),(116,'Mr. Angga','','082145779977','Honda Mobilio','DK 1217 BQ','Out','regular',NULL,NULL,'2018-05-14 08:17:51',0,44,'Batubulan','Lunas','-'),(118,'JASINDO','','','Suzuki Ertiga','DK 1528 SE','Out','regular',NULL,NULL,'2018-05-14 13:30:42',0,44,'Batubulan','Lunas','-');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_paket`
--

DROP TABLE IF EXISTS `booking_paket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booking_paket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `paket_id` int(11) DEFAULT NULL,
  `paket_name` varchar(200) DEFAULT NULL,
  `paket_price` int(11) DEFAULT NULL,
  `paket_discount` int(11) DEFAULT NULL,
  `paket_after` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_paket`
--

LOCK TABLES `booking_paket` WRITE;
/*!40000 ALTER TABLE `booking_paket` DISABLE KEYS */;
INSERT INTO `booking_paket` VALUES (1,1,21,'test',80000,10,72000),(2,2,21,'test',80000,10,72000),(3,5,1,'Premium carwash ( lift )',180000,50,90000),(4,13,28,'Poles Body',600000,65,210000),(5,14,27,'Poles Body',600000,55,270000),(6,15,27,'Poles Body',600000,55,270000),(7,16,9,'Vacum',20000,0,20000),(8,16,11,'Anti karat casis',600000,55,270000),(9,16,13,'Anti karat lantai',2400000,55,1080000),(10,18,1,'Premium carwash ( lift )',180000,50,90000),(11,18,26,'Poles body',600000,0,600000),(12,19,1,'Premium carwash ( lift )',180000,50,90000),(13,20,2,'Premium carwash ( nonlift )',125000,50,62500),(14,23,29,'Free voucher asuransi (non lift)',125000,100,0),(15,24,29,'Free voucher asuransi (non lift)',125000,100,0),(16,27,29,'Free voucher asuransi (non lift)',125000,100,0),(17,28,1,'Cling Premium ( lift )',180000,50,90000),(18,28,31,'Free voucher asuransi (non lift)',35000,100,0),(19,29,39,'Free voucher asuransi (non lift)',35000,100,0),(20,30,22,'Cling reguler (lift)',60000,0,60000),(21,31,36,'Free ladies driver (nonlift)',35000,100,0),(22,32,39,'Free voucher asuransi (non lift)',35000,100,0),(23,33,39,'Free voucher asuransi (non lift)',35000,100,0),(24,34,39,'Free voucher asuransi (non lift)',35000,100,0),(25,35,39,'Free voucher asuransi (non lift)',35000,100,0),(26,36,39,'Free voucher asuransi (non lift)',35000,100,0),(27,38,22,'Cling reguler (lift)',60000,0,60000),(28,40,22,'Cling reguler (lift)',60000,0,60000),(29,41,39,'Free voucher asuransi (non lift)',125000,100,0),(30,42,36,'Free ladies driver (nonlift)',125000,100,0),(31,43,1,'Cling Premium ( lift )',180000,0,180000),(32,44,39,'Free voucher asuransi (non lift)',125000,100,0),(33,45,39,'Free voucher asuransi (non lift)',125000,100,0),(34,47,22,'Cling reguler (lift)',60000,0,60000),(35,48,22,'Cling reguler (lift)',60000,0,60000),(36,49,39,'Free voucher asuransi (non lift)',125000,100,0),(37,51,22,'Cling reguler (lift)',60000,0,60000),(38,51,1,'Cling Premium ( lift )',180000,0,180000),(39,52,1,'Cling Premium ( lift )',180000,0,180000),(40,54,22,'Cling reguler (lift)',60000,0,60000),(41,55,1,'Cling Premium ( lift )',180000,0,180000),(42,56,39,'Free voucher asuransi (non lift)',125000,100,0),(43,60,36,'Free ladies premium wash',180000,100,0),(44,61,22,'Cling reguler (lift)',60000,0,60000),(45,63,29,'Poles body',600000,0,600000),(46,64,23,'Cling reguler expres',35000,0,35000),(47,65,22,'Cling reguler (lift)',60000,0,60000),(48,66,39,'Free voucher asuransi premium wash',180000,100,0),(49,67,39,'Free voucher asuransi premium wash',180000,100,0),(50,68,29,'Poles body',600000,0,600000),(51,70,22,'Cling reguler (lift)',60000,0,60000),(52,71,22,'Cling reguler (lift)',60000,0,60000),(53,71,26,'Oli plastik',10000,0,10000),(54,72,39,'Free voucher asuransi premium wash',180000,100,0),(55,73,22,'Cling reguler (lift)',60000,0,60000),(56,74,22,'Cling reguler (lift)',60000,0,60000),(57,74,24,'Anti karat lantai. ( atas & bawah )',2500000,30,1750000),(58,74,39,'Free voucher asuransi premium wash',180000,100,0),(59,75,39,'Free voucher asuransi premium wash',180000,100,0),(60,76,39,'Free voucher asuransi premium wash',180000,100,0),(61,77,39,'Free voucher asuransi premium wash',180000,100,0),(62,78,39,'Free voucher asuransi premium wash',180000,100,0),(63,79,39,'Free voucher asuransi premium wash',180000,100,0),(64,80,22,'Cling reguler (lift)',60000,0,60000),(65,81,39,'Free voucher asuransi premium wash',180000,100,0),(66,82,39,'Free voucher asuransi premium wash',180000,100,0),(67,83,39,'Free voucher asuransi premium wash',180000,100,0),(68,84,39,'Free voucher asuransi premium wash',180000,100,0),(69,85,39,'Free voucher asuransi premium wash',180000,100,0),(70,86,39,'Free voucher asuransi premium wash',180000,100,0),(71,87,39,'Free voucher asuransi premium wash',180000,100,0),(72,88,39,'Free voucher asuransi premium wash',180000,100,0),(73,89,39,'Free voucher asuransi premium wash',180000,100,0),(74,90,39,'Free voucher asuransi premium wash',180000,100,0),(75,91,39,'Free voucher asuransi premium wash',180000,100,0),(76,92,22,'Cling reguler (lift)',60000,0,60000),(77,93,22,'Cling reguler (lift)',60000,0,60000),(78,94,39,'Free voucher asuransi premium wash',180000,100,0),(79,95,39,'Free voucher asuransi premium wash',180000,100,0),(80,96,39,'Free voucher asuransi premium wash',180000,100,0),(81,97,39,'Free voucher asuransi premium wash',180000,100,0),(82,98,39,'Free voucher asuransi premium wash',180000,100,0),(83,100,39,'Free voucher asuransi premium wash',180000,100,0),(84,101,39,'Free voucher asuransi premium wash',180000,100,0),(85,102,23,'Cling reguler expres',35000,0,35000),(86,103,39,'Free voucher asuransi premium wash',180000,100,0),(87,104,39,'Free voucher asuransi premium wash',180000,100,0),(88,105,39,'Free voucher asuransi premium wash',180000,100,0),(89,106,39,'Free voucher asuransi premium wash',180000,100,0),(90,107,39,'Free voucher asuransi premium wash',180000,100,0),(91,108,39,'Free voucher asuransi premium wash',180000,100,0),(92,109,39,'Free voucher asuransi premium wash',180000,100,0),(93,110,39,'Free voucher asuransi premium wash',180000,100,0),(94,111,39,'Free voucher asuransi premium wash',180000,100,0),(95,112,39,'Free voucher asuransi premium wash',180000,100,0),(96,113,39,'Free voucher asuransi premium wash',180000,100,0),(97,114,36,'Free ladies premium wash',180000,100,0),(98,115,39,'Free voucher asuransi premium wash',180000,100,0),(99,116,39,'Free voucher asuransi premium wash',180000,100,0),(100,117,39,'Free voucher asuransi premium wash',180000,100,0),(101,118,39,'Free voucher asuransi premium wash',180000,100,0);
/*!40000 ALTER TABLE `booking_paket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gallery`
--

DROP TABLE IF EXISTS `gallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gallery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_name` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gallery`
--

LOCK TABLES `gallery` WRITE;
/*!40000 ALTER TABLE `gallery` DISABLE KEYS */;
/*!40000 ALTER TABLE `gallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location` varchar(200) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Batubulan',0);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_payment`
--

DROP TABLE IF EXISTS `member_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) DEFAULT NULL,
  `owner` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_payment`
--

LOCK TABLES `member_payment` WRITE;
/*!40000 ALTER TABLE `member_payment` DISABLE KEYS */;
INSERT INTO `member_payment` VALUES (1,1000000,'yudi pande','2018-03-07 22:01:31'),(2,1500000,'yudi pande','2018-03-07 22:02:39'),(3,3500000,'yudi pande','2018-03-07 22:03:39'),(4,3500000,'yudi pande','2018-03-08 04:33:42'),(5,1000000,'yudi pande','2018-03-08 11:05:32'),(6,1500000,'yudi pande','2018-03-08 11:06:40'),(7,1000000,'yudi pande','2018-03-08 11:50:28'),(8,1500000,'Wayan suardana','2018-03-08 12:01:12'),(9,3500000,'yudi pande','2018-03-08 12:05:22'),(10,3500000,'k1','2018-03-11 18:24:39'),(11,1000000,'yudi pande','2018-03-15 10:09:00'),(12,1000000,'k1','2018-03-18 06:42:39'),(13,1500000,'Marketing','2018-04-02 16:51:48'),(14,3500000,'Kurnia','2018-04-05 12:45:58'),(15,1500000,'gungis','2018-04-05 12:46:00'),(16,3500000,'dayu','2018-04-05 12:46:25'),(17,1000000,'indah','2018-04-05 15:57:16'),(18,1500000,'Kurnia','2018-04-06 14:28:48'),(19,3500000,'dayu','2018-04-06 14:29:28'),(20,1000000,'fivi','2018-04-06 14:29:28'),(21,1000000,'tets','2018-04-12 21:28:09'),(22,1000000,'tets','2018-04-12 21:29:41'),(23,3500000,'Kurnia','2018-04-20 15:36:08'),(24,3500000,'fivi','2018-04-20 15:42:10'),(25,3500000,'fivi','2018-04-21 11:10:49'),(26,3500000,'yudi pande','2018-05-06 21:22:18');
/*!40000 ALTER TABLE `member_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paket`
--

DROP TABLE IF EXISTS `paket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `discount` int(11) DEFAULT NULL,
  `after` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paket`
--

LOCK TABLES `paket` WRITE;
/*!40000 ALTER TABLE `paket` DISABLE KEYS */;
INSERT INTO `paket` VALUES (1,'Cling Premium ( lift )',180000,'umum',0,180000),(2,'Cling Premium expres',125000,'umum',0,125000),(9,'Vacum',20000,'regular',30,14000),(17,'Anti karat casis',600000,'vip',50,300000),(19,'Anti karat lantai. ( atas & bawah )',2500000,'vip',50,1250000),(22,'Cling reguler (lift)',60000,'umum',0,60000),(23,'Cling reguler expres',35000,'umum',0,35000),(24,'Anti karat lantai. ( atas & bawah )',2500000,'umum',30,1750000),(25,'Anti karat casis',600000,'umum',30,420000),(26,'Oli plastik',10000,'umum',0,10000),(27,'Lift',50000,'regular',30,35000),(28,'Poles Body',600000,'vip',50,300000),(29,'Poles body',600000,'umum',0,600000),(30,'Kerak body (logo)',300000,'umum',0,300000),(31,'Kerak kaca',250000,'umum',0,250000),(32,'Vacum',20000,'umum',0,20000),(33,'Wax cling',100000,'umum',0,100000),(34,'Cling komplit  (cuci lift, casis, lantai bawah, poles,kerak kaca&body, wax ) ',1500000,'umum',0,1500000),(36,'Free ladies premium wash',180000,'umum',100,0),(38,'Free member (Lift)',180000,'umum',100,0),(39,'Free voucher asuransi premium wash',180000,'umum',100,0),(42,'Kerak kaca',250000,'regular',30,175000),(43,'Kerak body (logo)',300000,'regular',30,210000),(44,'Poles body',600000,'regular',30,420000),(45,'Wax cling',100000,'regular',30,70000),(46,'Anti karat casis',600000,'regular',30,420000),(47,'Anti karat lantai. ( atas & bawah )',2500000,'regular',30,1750000),(48,'Wax cling',100000,'vip',50,50000),(49,'Kerak kaca',250000,'vip',50,125000),(50,'Kerak body (logo)',300000,'vip',50,150000),(51,'Vacum',20000,'vip',50,10000),(52,'Oli plastik',10000,'regular',30,7000),(53,'Oli plastik',10000,'vip',50,5000),(54,'Cling Premium ( lift )',180000,'vip',50,90000),(55,'Cling Premium ( nonlift )',125000,'vip',50,62500),(56,'Cling komplit (lift, casis, lantai bawah, poles,kerak kaca&body, wax ) ',1500000,'vip',50,750000),(57,'Cling Premium ( lift )',180000,'regular',30,126000),(58,'Cling Premium ( nonlift )',125000,'regular',30,87500),(59,'Cling komplit (lift, casis, lantai bawah, poles,kerak kaca&body, wax ) ',1500000,'regular',30,1050000),(60,'wet look painting by sikken',4000000,'umum',0,4000000),(61,'medical engine',550000,'umum',0,550000),(62,'wet look painting by sikken',4000000,'regular',30,2800000),(63,'medical engine',550000,'regular',30,385000),(64,'wet look painting by sikken',4000000,'vip',50,2000000),(65,'medical engine',550000,'vip',50,275000);
/*!40000 ALTER TABLE `paket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `mobil` varchar(100) DEFAULT NULL,
  `plat` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `renew` datetime DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `member` varchar(200) DEFAULT NULL,
  `paket` varchar(200) DEFAULT NULL,
  `marketing` varchar(200) DEFAULT NULL,
  `treatment` varchar(200) DEFAULT NULL,
  `birth` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'yudi pande','bossssku@gmail.com','sha256$NBIqOjbp$2f8ceeedb58aeca524ce48bc75d1f8c740c6c4a3327842261d60f90471acdb7a','superuser',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'Yudi','Yudi@gmail.com','sha256$fBh2dGe2$7ecb0a9c936b6421e152b6a0730e110d8ed44d6a8d9a0f188f1a5eb912d74e4a','user',NULL,NULL,NULL,'user',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL),(9,'Wayan suardana','Cegongboy@gmail.com','sha256$uYsjk4SE$498b588bc2fcbedc9b3079d6eb7bd4d77f03d2ae544b797694d140cb787d354f','member','081999618123','Avanza','Dk 1379 IV','aktif','2018-03-08 04:33:42','2018-09-04 00:00:00',NULL,'vip','paket3','yudi pande','Cuci + lift + Vacum','1988-09-19 00:00:00'),(19,'Wayan suardana','Cegongboy1@gmail.com','sha256$24ewjm5u$6774c290f1d4fbd1d3660fc2e34d84e83d078fa918fe6e390cdfc4467fa8586d','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(30,'Marketing','marketing@marketing.com','sha256$Wjb22RLU$5ce28fbf3fc88017c9e5804387b55b92c9a406c36915ea38d61126b141e5a974','marketing',NULL,NULL,NULL,'pending',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(31,'member 1','member@member.com','sha256$SzeWhFTI$5bdc0bfecf0db11cae6f62da392eee432940519e53fd5c8b1d3ce10b5767f1ba','member','081237311255','Honda HRV','DK 111 RA','aktif','2018-04-02 16:51:48','2018-07-01 00:00:00',NULL,'regular','paket2','Marketing','Cuci + lift + Vacum','1982-04-23 00:00:00'),(32,'gungis','gungistrisanjiwani@yahoo.com','sha256$c4IS5DRL$e5b2c94cb954883f69d1d0c5681117113ea74c96bb3de5bc8fce47e3aadb1fd5','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(33,'dayu','Dayudyah4@gmail.com','sha256$BlakYeyP$896bae0c5e9f61cfb288feb38e0ac576814cdff72b9bf5995510469a34a4dfaa','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(34,'Kurnia','Dewik741@gmail.com','sha256$uy5g9MJi$d8e4ea1ee85d3114b19f204b8ae2f8d9d132139a4ccb4a7681ec56364af51723','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(35,'kiki','kikiagnes1996@gmail.com','sha256$4JS0HA5V$41b61eae4f8c995d4f7c187442758c95de18e17b3de31aeae0854d95309de875','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(36,'indah','indahputu996@gmail.com','sha256$uaRPNQod$af00202d07ea4252291afa5846bda0ae4220437d93737c36b3fb8562fc85eb8e','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(37,'Yudi','Marketing@gmail.com','sha256$Wd3lry4c$676366d9679712d3c6c0d973cfa0a099f05a26325a0a9c0d56cfe121d12eb3c6','marketing',NULL,NULL,NULL,'pending',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(38,'yudi','eriktea23@yahoo.co.id','sha256$WFoiJmIA$85f66dd78a122796c18746f324dcdc131452d90f2f13a0abfa8646b6c2386d10','member','085737652288','agya','dk 653 pr','aktif','2018-04-05 12:45:58','2018-10-02 00:00:00',NULL,'vip','paket3','Kurnia','Cuci + lift + Vacum','2004-04-17 00:00:00'),(44,'SA1','S1@gmail.com','sha256$PvoqRAZ6$c6273b49b0456e090d0c415de889d18980abdc4ef1f0009d0fd4721d3356fd98','sa',NULL,NULL,NULL,'user',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL),(47,'Supervisor','sa@gmail.com','sha256$RIPundJD$37b598015975dbe1df5c5fd40372b8ec92c7097a99c93b7e573da4211f6d1919','sa',NULL,NULL,NULL,'user',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL),(49,'k1','k1@gmail.com','sha256$zLiHexSL$f59e9ade2ac8247eceff876da7e7ff320cc08395378218307b34bf6994cf40e6','cashier',NULL,NULL,NULL,'aktif',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL),(50,'korlap','ko1@gmail.com','sha256$KhEZgjq4$30541cafc56ef48804831acaefd23ee5b51147ea6d670abf3753fbe689c8d6e1','user',NULL,NULL,NULL,'user',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL),(51,'SA2','S2@gmail.com','sha256$D2Bq6uv1$4c1b389b14c05891c55123ce4fa74fdab63fd6f10bf6656f2da4c0eb48cc8ee2','sa',NULL,NULL,NULL,'user',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL),(52,'fivi','Agustinidwifivi@gmail.com','sha256$DBEplxJI$46281be09d4c6873eb4c97bbd9f2a6dfa789d101e62e646ce19f3feac35beb50','marketing',NULL,NULL,NULL,'aktif',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(56,'tets','test@gmail.com','sha256$gd7pZmMD$95ee5aabcaf3c3654112bbd68d4585c8efe62e3c18abfcff5262499927e5e2aa','superuser',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(57,'Test','member1@gmail.com','sha256$OuhOSX4y$d0de42f6b13844dcd1b1e84ec00742b41e0f56818752f810bd84d8368d677b1e','member','081237322555','Jazz','Ffff','aktif','2018-04-12 21:28:09','2018-10-09 00:00:00',NULL,'nonregular','paket1','tets','Cuci Non Lift','2018-04-12 00:00:00'),(58,'member2','member2@gmail.com','sha256$1jrYeL9C$8ad442d24450ac568b474075361ce7acb996b625e1ab1e2e8c37d0f6df3b17e3','member','081237322555','Jazz','6666','pending','2018-04-12 21:29:41','2018-10-09 21:29:41',NULL,'nonregular','paket1','tets','Cuci Non Lift','2018-04-12 00:00:00'),(60,'Mr. Maskup Staco','Maskup@gmail.com','sha256$en5JqrdE$f3693c13ee7e1719708e1d79aef8b9f58b32ddb1ba6955d8c56bb3ad66197cad','member','','Toyota Avanza','B 1934 PRJ','aktif','2018-04-20 15:36:08','2018-10-17 00:00:00',NULL,'vip','paket3','Kurnia','Cuci + lift + Vacum','1969-01-15 00:00:00'),(61,'Mr Rito Lakson Wahanatata','Rito@gmail.com','sha256$GjPxJEar$ca50874e5c6e6c747d1aeaada1a4cee8cf63fef2b573453a9d89c0dc654d7516','member','08123803443','Toyota innova','B 1183 SZV','aktif','2018-04-20 15:42:10','2018-10-17 00:00:00',NULL,'vip','paket3','fivi','Cuci + lift + Vacum','1969-06-25 00:00:00'),(62,'Mr Samuel Budi Mega Insurance','Samuel@gmail.com','sha256$2sgHrshp$bf0db409b528e4a95bd486defb0ae24aba9cc3cedab86cc716e74f45f1381118','member','082208238267','Innova','B 2754 SFV','aktif','2018-04-21 11:10:49','2018-10-18 00:00:00',NULL,'vip','paket3','fivi','Cuci + lift + Vacum','1964-10-05 00:00:00'),(63,'nanonano','kdsuwardana@gmail.com','sha256$xBQgLEJM$195153973ce707e87d4a2084ce6838e31c5ca3949597c603e548c4aa2956372a','member','081999020923','Xenia','Dk 1334 PC','aktif','2018-05-06 21:22:18','2018-11-02 00:00:00',NULL,'vip','paket3','yudi pande','Cuci + lift + Vacum','1990-01-26 00:00:00'),(64,'Yanik','Yanik@gmail.com','sha256$qUnFDfNz$27fb4ead85e96b3a9469d65308143fae00675d1a42ed3d7dc7fa71c388e3710c','accountant',NULL,NULL,NULL,'user',NULL,NULL,'Batubulan',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-14 23:38:43

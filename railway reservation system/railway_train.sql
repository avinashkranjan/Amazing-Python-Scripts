-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: railway
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `TNo` int(10) NOT NULL,
  `TName` varchar(20) NOT NULL,
  `TSource` varchar(20) NOT NULL,
  `TDestination` varchar(20) NOT NULL,
  `Time_of_departure_from_source` varchar(20) NOT NULL,
  `Time_of_arrival_at_destination` varchar(20) NOT NULL,
  PRIMARY KEY (`TNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES (11111,'jammu tawi exp','jammu','delhi','10:00','17:00'),(11112,'patna exp','patna','secundrabad','15:00','06:00'),(11113,'tejas exp','delhi','agra','12:45','14:00'),(11114,'sealdah exp','panaji','mumbai','10:30','12:00'),(11115,'paschim exp','kolkata','lucknow','14:00','20:00'),(11116,'tejas exp','varanasi','delhi','10:00','13:00'),(11117,'bidar exp','bidar','chennai','17:00','23:00'),(11118,'delhi exp','delhi','chennai','15:00','19:00'),(11119,'jagnath exp','jaganath','delhi','14:00','20:00'),(11120,'bangalore exp','bangalore','chennai','12:00','18:00'),(11121,'bhopal exp','bhopal','delhi','04:00','12:00'),(11122,'mysore exp','mysore','bangalore','14:00','19:00'),(11123,'chennai exp','mumbai','chennai','12:00','00:00'),(11124,'trvndrm exp','thiruvandapuram','chennai','13:00','18:00'),(11125,'calcuta exp','calcuta','delhi','15:00','00:00'),(11126,'punjab mail','amritsar','howrah','22:00','19:00'),(11127,'koimbatore exp','koimbatore','delhi','14:00','23:00'),(11128,'jamnagar vns exp','jamnagar','varanasi','16:00','20:00'),(11129,'jodhpur intercity','jodhpur','jaipu','09:00','13:00'),(11130,'prayagraj exp','prayagraj','delhi','01:00','08:00');
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-23 12:05:39

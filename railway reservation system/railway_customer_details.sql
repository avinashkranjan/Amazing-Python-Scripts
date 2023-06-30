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
-- Table structure for table `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_details` (
  `CNo` int(10) NOT NULL AUTO_INCREMENT,
  `CName` varchar(20) NOT NULL,
  `CAge` int(3) NOT NULL,
  `CGender` varchar(10) NOT NULL,
  `CPhone` varchar(15) NOT NULL,
  `CPwd` varchar(45) NOT NULL,
  PRIMARY KEY (`CNo`),
  UNIQUE KEY `CPhone_UNIQUE` (`CPhone`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_details`
--

LOCK TABLES `customer_details` WRITE;
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
INSERT INTO `customer_details` VALUES (1,'sid',12,'m','7418529635','qwerty'),(2,'sam',15,'m','7894561235','qwerty'),(3,'sameer',14,'m','7414785415','qwerty'),(4,'sumit',11,'m','7485748574','asdf'),(5,'sahil',15,'m','7894567718','asdf'),(6,'ankur',15,'m','7487487487','asdf'),(7,'ankit',14,'m','1452145214','asdf'),(8,'ronak',19,'m','6545654565','asdf'),(9,'ashu',18,'m','7878787878','qwerty'),(10,'gourav',15,'m','9658235684','qwerty'),(11,'abhijit',17,'m','7489652301','qwerty'),(12,'indramani',15,'m','1424515689','qwerty'),(13,'saif',16,'m','7482365256','qwerty'),(14,'himanshu',8,'m','4545454545','asdf'),(15,'jatin',14,'m','4141410021','asdf'),(16,'tazim',16,'m','7478963232','asdf'),(17,'devang',15,'m','7485968523','asdf'),(18,'akash',16,'m','7844521463','qwerty'),(19,'swapnil',18,'m','7441156324','qwerty'),(20,'sreyansh',16,'m','7894567418','qwerty'),(31,'rakesh',30,'m','78954120154','asdf');
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;
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

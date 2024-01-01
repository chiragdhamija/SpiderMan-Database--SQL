-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: spiderverse
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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
-- Current Database: `spiderverse`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `spiderverse` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `spiderverse`;

--
-- Table structure for table `AbilitiesSideChar`
--

DROP TABLE IF EXISTS `AbilitiesSideChar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AbilitiesSideChar` (
  `CharacterIdentifier` int NOT NULL,
  `Ability` varchar(255) NOT NULL,
  PRIMARY KEY (`CharacterIdentifier`,`Ability`),
  CONSTRAINT `AbilitiesSideChar_ibfk_1` FOREIGN KEY (`CharacterIdentifier`) REFERENCES `SideCharacter` (`CharacterIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AbilitiesSideChar`
--

LOCK TABLES `AbilitiesSideChar` WRITE;
/*!40000 ALTER TABLE `AbilitiesSideChar` DISABLE KEYS */;
INSERT INTO `AbilitiesSideChar` VALUES (1,'Supportive'),(2,'Wisdom'),(3,'Agility'),(4,'Tech-savvy'),(5,'Journalism'),(6,'Journalism'),(7,'Loyal ally');
/*!40000 ALTER TABLE `AbilitiesSideChar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AbilitiesSpiderPerson`
--

DROP TABLE IF EXISTS `AbilitiesSpiderPerson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AbilitiesSpiderPerson` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `Ability` varchar(255) NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`Ability`),
  CONSTRAINT `AbilitiesSpiderPerson_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AbilitiesSpiderPerson`
--

LOCK TABLES `AbilitiesSpiderPerson` WRITE;
/*!40000 ALTER TABLE `AbilitiesSpiderPerson` DISABLE KEYS */;
INSERT INTO `AbilitiesSpiderPerson` VALUES (1,'Superhuman strength'),(1,'Wall-crawling'),(2,'Acrobatics'),(3,'Venom Blast'),(4,'Bio-electrokinesis'),(5,'Accelerated vision'),(6,'Web creation'),(7,'Adaptive combat');
/*!40000 ALTER TABLE `AbilitiesSpiderPerson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AbilitiesVillain`
--

DROP TABLE IF EXISTS `AbilitiesVillain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AbilitiesVillain` (
  `VillainIdentifier` int NOT NULL,
  `Ability` varchar(255) NOT NULL,
  PRIMARY KEY (`VillainIdentifier`,`Ability`),
  CONSTRAINT `AbilitiesVillain_ibfk_1` FOREIGN KEY (`VillainIdentifier`) REFERENCES `Villain` (`VillainIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AbilitiesVillain`
--

LOCK TABLES `AbilitiesVillain` WRITE;
/*!40000 ALTER TABLE `AbilitiesVillain` DISABLE KEYS */;
INSERT INTO `AbilitiesVillain` VALUES (1,'Insanity'),(1,'Intelligence'),(2,'Electricity manipulation'),(3,'Mastermind'),(4,'Tentacle manipulation'),(5,'Flight'),(6,'Symbiote bonding'),(7,'Enhanced strength');
/*!40000 ALTER TABLE `AbilitiesVillain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AssociatesWith`
--

DROP TABLE IF EXISTS `AssociatesWith`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AssociatesWith` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `SideCharacterCharacterIdentifier` int NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`SideCharacterCharacterIdentifier`),
  KEY `SideCharacterCharacterIdentifier` (`SideCharacterCharacterIdentifier`),
  CONSTRAINT `AssociatesWith_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `AssociatesWith_ibfk_2` FOREIGN KEY (`SideCharacterCharacterIdentifier`) REFERENCES `SideCharacter` (`CharacterIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AssociatesWith`
--

LOCK TABLES `AssociatesWith` WRITE;
/*!40000 ALTER TABLE `AssociatesWith` DISABLE KEYS */;
INSERT INTO `AssociatesWith` VALUES (1,1),(6,1),(1,2),(7,2),(2,3),(3,4),(1,5),(4,6),(1,7);
/*!40000 ALTER TABLE `AssociatesWith` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Equipment`
--

DROP TABLE IF EXISTS `Equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Equipment` (
  `Name` varchar(255) NOT NULL,
  `Type` varchar(255) DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Equipment`
--

LOCK TABLES `Equipment` WRITE;
/*!40000 ALTER TABLE `Equipment` DISABLE KEYS */;
INSERT INTO `Equipment` VALUES ('Adapted equipment','Gear','Modified gear for identity concealment'),('Future tech','Technology','Advanced gadgets from 2099'),('Inter-dimensional travel tech','Technology','Devices for traveling across dimensions'),('Silk abilities','Powers','Silk-based powers and agility'),('Spy equipment','Gear','Tools for espionage'),('Stealth Suit','Suit','Camouflaging suit'),('Web-shooters','Gear','Devices to shoot webs');
/*!40000 ALTER TABLE `Equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FacesOffAgainst`
--

DROP TABLE IF EXISTS `FacesOffAgainst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FacesOffAgainst` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `VillainVillainIdentifier` int NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`VillainVillainIdentifier`),
  KEY `VillainVillainIdentifier` (`VillainVillainIdentifier`),
  CONSTRAINT `FacesOffAgainst_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `FacesOffAgainst_ibfk_2` FOREIGN KEY (`VillainVillainIdentifier`) REFERENCES `Villain` (`VillainIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FacesOffAgainst`
--

LOCK TABLES `FacesOffAgainst` WRITE;
/*!40000 ALTER TABLE `FacesOffAgainst` DISABLE KEYS */;
INSERT INTO `FacesOffAgainst` VALUES (1,1),(2,1),(4,1),(1,2),(6,2),(3,3),(5,4),(1,5),(7,5),(2,6);
/*!40000 ALTER TABLE `FacesOffAgainst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HeadsMission`
--

DROP TABLE IF EXISTS `HeadsMission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HeadsMission` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `MissionTitle` varchar(255) NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`MissionTitle`),
  KEY `MissionTitle` (`MissionTitle`),
  CONSTRAINT `HeadsMission_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `HeadsMission_ibfk_2` FOREIGN KEY (`MissionTitle`) REFERENCES `Mission` (`Title`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HeadsMission`
--

LOCK TABLES `HeadsMission` WRITE;
/*!40000 ALTER TABLE `HeadsMission` DISABLE KEYS */;
INSERT INTO `HeadsMission` VALUES (3,'Brooklyn Defense'),(5,'Future Crisis'),(4,'Hydra Investigation'),(7,'Identity Quest'),(2,'Multiverse Patrol'),(1,'Save NYC'),(6,'Silk\'s Secrets');
/*!40000 ALTER TABLE `HeadsMission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Hypothesis`
--

DROP TABLE IF EXISTS `Hypothesis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Hypothesis` (
  `SpiderIdentifier` int NOT NULL,
  `ResearchNote` varchar(255) NOT NULL,
  PRIMARY KEY (`SpiderIdentifier`,`ResearchNote`),
  KEY `ResearchNote` (`ResearchNote`),
  CONSTRAINT `Hypothesis_ibfk_1` FOREIGN KEY (`SpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `Hypothesis_ibfk_2` FOREIGN KEY (`ResearchNote`) REFERENCES `ResearchNotes` (`Topic`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hypothesis`
--

LOCK TABLES `Hypothesis` WRITE;
/*!40000 ALTER TABLE `Hypothesis` DISABLE KEYS */;
INSERT INTO `Hypothesis` VALUES (6,'Cindy Moon\'s heritage'),(4,'Hydra Investigation'),(2,'Multiverse Exploration'),(3,'Sensory Abilities'),(1,'Symbiote study'),(5,'Temporal Mechanics'),(7,'Web-shooter advancements');
/*!40000 ALTER TABLE `Hypothesis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Images`
--

DROP TABLE IF EXISTS `Images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Images` (
  `IMGID` int NOT NULL,
  `IMG` blob,
  PRIMARY KEY (`IMGID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Images`
--

LOCK TABLES `Images` WRITE;
/*!40000 ALTER TABLE `Images` DISABLE KEYS */;
/*!40000 ALTER TABLE `Images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MemberOf`
--

DROP TABLE IF EXISTS `MemberOf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MemberOf` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `OrganizationOrganizationIdentifier` int NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`OrganizationOrganizationIdentifier`),
  KEY `OrganizationOrganizationIdentifier` (`OrganizationOrganizationIdentifier`),
  CONSTRAINT `MemberOf_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `MemberOf_ibfk_2` FOREIGN KEY (`OrganizationOrganizationIdentifier`) REFERENCES `Organization` (`OrganizationIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MemberOf`
--

LOCK TABLES `MemberOf` WRITE;
/*!40000 ALTER TABLE `MemberOf` DISABLE KEYS */;
INSERT INTO `MemberOf` VALUES (1,1),(4,1),(7,1),(2,2),(5,2),(3,3),(6,5);
/*!40000 ALTER TABLE `MemberOf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mentors`
--

DROP TABLE IF EXISTS `Mentors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mentors` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `MentorSpiderIdentifier` int NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`MentorSpiderIdentifier`),
  KEY `MentorSpiderIdentifier` (`MentorSpiderIdentifier`),
  CONSTRAINT `Mentors_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `Mentors_ibfk_2` FOREIGN KEY (`MentorSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mentors`
--

LOCK TABLES `Mentors` WRITE;
/*!40000 ALTER TABLE `Mentors` DISABLE KEYS */;
INSERT INTO `Mentors` VALUES (3,1),(4,1),(5,1),(7,1),(6,4),(2,7);
/*!40000 ALTER TABLE `Mentors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mission`
--

DROP TABLE IF EXISTS `Mission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mission` (
  `Title` varchar(255) NOT NULL,
  `Objectives` text,
  `ResourcesUsed` text,
  `Outcome` text,
  `DimensionID` int DEFAULT NULL,
  PRIMARY KEY (`Title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mission`
--

LOCK TABLES `Mission` WRITE;
/*!40000 ALTER TABLE `Mission` DISABLE KEYS */;
INSERT INTO `Mission` VALUES ('Brooklyn Defense','Stop local crime surge','Web abilities, Stealth tactics','Restored peace in Brooklyn',1610),('Future Crisis','Prevent temporal anomalies','Future tech, Advanced suit','Averted catastrophic events',2099),('Hydra Investigation','Infiltrate Hydra operations','Spy equipment, Combat skills','Uncovered Hydra\'s plans',616),('Identity Quest','Find purpose, Fight crime','Adapted equipment, Agility','Established heroic identity',616),('Multiverse Patrol','Prevent incursions, Protect realities','Inter-dimensional travel tech','Closed dimensional breaches',65),('Save NYC','Defend city from attacks','Web-shooters, Tech gadgets','Defeated Green Goblin',616),('Silk\'s Secrets','Discover family history','Silk abilities, Investigation','Revealed hidden family history',616);
/*!40000 ALTER TABLE `Mission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Organization`
--

DROP TABLE IF EXISTS `Organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Organization` (
  `OrganizationIdentifier` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `DimensionID` int DEFAULT NULL,
  `TimeOfEstablishment` date DEFAULT NULL,
  `Objectives` text,
  `HeadquartersLocation` varchar(255) DEFAULT NULL,
  `Logo` int DEFAULT NULL,
  PRIMARY KEY (`OrganizationIdentifier`),
  KEY `image_const` (`Logo`),
  CONSTRAINT `image_const` FOREIGN KEY (`Logo`) REFERENCES `Images` (`IMGID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Organization`
--

LOCK TABLES `Organization` WRITE;
/*!40000 ALTER TABLE `Organization` DISABLE KEYS */;
INSERT INTO `Organization` VALUES (1,'S.H.I.E.L.D.',616,'1965-04-04','Protecting Earth from threats','New York',NULL),(2,'Spider Society',65,'2010-09-21','Maintaining Multiverse balance','Earth-65',NULL),(3,'Spider-Guild',1610,'1999-12-12','Training & safeguarding realities','Brooklyn',NULL),(4,'WebWatchers',2099,'2078-06-30','Time anomalies prevention','Nueva York',NULL),(5,'Arachnid Alliance',67,'1985-10-15','Uniting against threats','New York',NULL);
/*!40000 ALTER TABLE `Organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Owns`
--

DROP TABLE IF EXISTS `Owns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Owns` (
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  `Equipment` varchar(255) NOT NULL,
  PRIMARY KEY (`SpiderPersonSpiderIdentifier`,`Equipment`),
  KEY `Equipment` (`Equipment`),
  CONSTRAINT `Owns_ibfk_1` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE,
  CONSTRAINT `Owns_ibfk_2` FOREIGN KEY (`Equipment`) REFERENCES `Equipment` (`Name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Owns`
--

LOCK TABLES `Owns` WRITE;
/*!40000 ALTER TABLE `Owns` DISABLE KEYS */;
INSERT INTO `Owns` VALUES (4,'Adapted equipment'),(5,'Future tech'),(7,'Inter-dimensional travel tech'),(6,'Silk abilities'),(3,'Spy equipment'),(2,'Stealth Suit'),(1,'Web-shooters');
/*!40000 ALTER TABLE `Owns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Participant`
--

DROP TABLE IF EXISTS `Participant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Participant` (
  `MissionTitle` varchar(255) NOT NULL,
  `SpiderPersonSpiderIdentifier` int NOT NULL,
  PRIMARY KEY (`MissionTitle`,`SpiderPersonSpiderIdentifier`),
  KEY `SpiderPersonSpiderIdentifier` (`SpiderPersonSpiderIdentifier`),
  CONSTRAINT `Participant_ibfk_1` FOREIGN KEY (`MissionTitle`) REFERENCES `Mission` (`Title`) ON DELETE CASCADE,
  CONSTRAINT `Participant_ibfk_2` FOREIGN KEY (`SpiderPersonSpiderIdentifier`) REFERENCES `SpiderPerson` (`SpiderIdentifier`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Participant`
--

LOCK TABLES `Participant` WRITE;
/*!40000 ALTER TABLE `Participant` DISABLE KEYS */;
INSERT INTO `Participant` VALUES ('Save NYC',1),('Multiverse Patrol',2),('Brooklyn Defense',3),('Hydra Investigation',4),('Future Crisis',5),('Silk\'s Secrets',6),('Identity Quest',7);
/*!40000 ALTER TABLE `Participant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ResearchNotes`
--

DROP TABLE IF EXISTS `ResearchNotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ResearchNotes` (
  `Content` text,
  `Date` date DEFAULT NULL,
  `Topic` varchar(255) NOT NULL,
  PRIMARY KEY (`Topic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ResearchNotes`
--

LOCK TABLES `ResearchNotes` WRITE;
/*!40000 ALTER TABLE `ResearchNotes` DISABLE KEYS */;
INSERT INTO `ResearchNotes` VALUES ('Silk\'s Ancestral Origins','2022-12-18','Cindy Moon\'s heritage'),('Uncovering Hydra\'s Plans','2022-06-15','Hydra Investigation'),('Multiverse Theories','2023-01-10','Multiverse Exploration'),('Spider Sense Mechanism','2023-04-20','Sensory Abilities'),('Venom Symbiote Analysis','2023-08-12','Symbiote study'),('Time Travel Paradoxes','2078-07-05','Temporal Mechanics'),('Web Technology Evolution','2022-10-30','Web-shooter advancements');
/*!40000 ALTER TABLE `ResearchNotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SideCharacter`
--

DROP TABLE IF EXISTS `SideCharacter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SideCharacter` (
  `CharacterIdentifier` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `DimensionID` int DEFAULT NULL,
  `MaskName` varchar(255) DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`CharacterIdentifier`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SideCharacter`
--

LOCK TABLES `SideCharacter` WRITE;
/*!40000 ALTER TABLE `SideCharacter` DISABLE KEYS */;
INSERT INTO `SideCharacter` VALUES (1,'Mary Jane',616,'Red Rider','Female'),(2,'Aunt May',65,'Web Guardian','Female'),(3,'Anya Corazon',1610,'Spiderling','Female'),(4,'Miguel Stone',2099,'Steel Spider','Male'),(5,'J. Jonah Jameson',616,'Spider-Hater','Male'),(6,'Robbie Robertson',616,'Truth Seeker','Male'),(7,'Liz Allan',67,'Vulture\'s Ally','Female');
/*!40000 ALTER TABLE `SideCharacter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SpiderPerson`
--

DROP TABLE IF EXISTS `SpiderPerson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SpiderPerson` (
  `SpiderIdentifier` int NOT NULL AUTO_INCREMENT,
  `RealName` varchar(255) DEFAULT NULL,
  `DimensionID` int DEFAULT NULL,
  `HeroName` varchar(255) DEFAULT NULL,
  `MissionLogs` text,
  `Gender` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SpiderIdentifier`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SpiderPerson`
--

LOCK TABLES `SpiderPerson` WRITE;
/*!40000 ALTER TABLE `SpiderPerson` DISABLE KEYS */;
INSERT INTO `SpiderPerson` VALUES (1,'Peter Parker',616,'Spider-Man','Fought Green Goblin, Saved New York','Male'),(2,'Gwen Stacy',65,'Spider-Gwen','Explored Multiverse, Foiled Crimes','Female'),(3,'Miles Morales',1610,'Kid Arachnid','Trained with Peter Parker, Protected Brooklyn','Male'),(4,'Jessica Drew',616,'Spider-Woman','Investigated Hydra\'s Plans, Battled Villains','Female'),(5,'Miguel O\'Hara',2099,'Spider-Man 2099','Prevented Future Crises, Time Traveler','Male'),(6,'Cindy Moon',616,'Silk','Unraveled Family Secrets, Foiled Robberies','Female'),(7,'Ben Reilly',616,'Scarlet Spider','Sought Identity, Fought Criminals','Male');
/*!40000 ALTER TABLE `SpiderPerson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Villain`
--

DROP TABLE IF EXISTS `Villain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Villain` (
  `VillainIdentifier` int NOT NULL AUTO_INCREMENT,
  `RealName` varchar(255) DEFAULT NULL,
  `DimensionID` int DEFAULT NULL,
  `VillainName` varchar(255) DEFAULT NULL,
  `ThreatLevel` int DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`VillainIdentifier`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Villain`
--

LOCK TABLES `Villain` WRITE;
/*!40000 ALTER TABLE `Villain` DISABLE KEYS */;
INSERT INTO `Villain` VALUES (1,'Norman Osborn',616,'Green Goblin',9,'Male'),(2,'Max Dillon',616,'Electro',7,'Male'),(3,'Wilson Fisk',1610,'Kingpin',8,'Male'),(4,'Otto Octavius',1610,'Doctor Octopus',8,'Male'),(5,'Adrian Toomes',67,'Vulture',6,'Male'),(6,'Cletus Kasady',616,'Carnage',9,'Male'),(7,'Aleksei Sytsevich',1610,'Rhino',7,'Male');
/*!40000 ALTER TABLE `Villain` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03  5:21:23

-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: vue_django
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `api_admininfo`
--

DROP TABLE IF EXISTS `api_admininfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_admininfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `adm_id` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `adm_id` (`adm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_admininfo`
--

LOCK TABLES `api_admininfo` WRITE;
/*!40000 ALTER TABLE `api_admininfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_admininfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_areas`
--

DROP TABLE IF EXISTS `api_areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_areas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `aid` int NOT NULL,
  `atitle` varchar(30) NOT NULL,
  `aParent` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_areas`
--

LOCK TABLES `api_areas` WRITE;
/*!40000 ALTER TABLE `api_areas` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_building`
--

DROP TABLE IF EXISTS `api_building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_building` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `direct` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_building`
--

LOCK TABLES `api_building` WRITE;
/*!40000 ALTER TABLE `api_building` DISABLE KEYS */;
INSERT INTO `api_building` VALUES (1,'南1','南'),(2,'南2','南'),(3,'南3','南'),(4,'南4','南'),(5,'南5','南'),(6,'空管A','南'),(7,'空管B','南'),(8,'空管C','南'),(9,'北4','北'),(10,'北10','北'),(11,'北14','北'),(12,'北25','北'),(13,'北实','北');
/*!40000 ALTER TABLE `api_building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_cities`
--

DROP TABLE IF EXISTS `api_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_cities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `aid` int NOT NULL,
  `atitle` varchar(30) NOT NULL,
  `Province_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_cities_Province_id_2b930a57_fk_api_provinces_id` (`Province_id`),
  CONSTRAINT `api_cities_Province_id_2b930a57_fk_api_provinces_id` FOREIGN KEY (`Province_id`) REFERENCES `api_provinces` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=392 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_cities`
--

LOCK TABLES `api_cities` WRITE;
/*!40000 ALTER TABLE `api_cities` DISABLE KEYS */;
INSERT INTO `api_cities` VALUES (1,1,'北京市',1),(2,2,'天津市',2),(3,3,'上海市',3),(4,4,'重庆市',4),(5,5,'石家庄市',5),(6,6,'唐山市',5),(7,7,'秦皇岛市',5),(8,8,'邯郸市',5),(9,9,'邢台市',5),(10,10,'保定市',5),(11,11,'张家口市',5),(12,12,'承德市',5),(13,13,'沧州市',5),(14,14,'廊坊市',5),(15,15,'衡水市',5),(16,16,'太原市',6),(17,17,'大同市',6),(18,18,'阳泉市',6),(19,19,'长治市',6),(20,20,'晋城市',6),(21,21,'朔州市',6),(22,22,'晋中市',6),(23,23,'运城市',6),(24,24,'忻州市',6),(25,25,'临汾市',6),(26,26,'吕梁市',6),(27,27,'台北市',7),(28,28,'高雄市',7),(29,29,'基隆市',7),(30,30,'台中市',7),(31,31,'台南市',7),(32,32,'新竹市',7),(33,33,'嘉义市',7),(34,34,'台北县',7),(35,35,'宜兰县',7),(36,36,'桃园县',7),(37,37,'新竹县',7),(38,38,'苗栗县',7),(39,39,'台中县',7),(40,40,'彰化县',7),(41,41,'南投县',7),(42,42,'云林县',7),(43,43,'嘉义县',7),(44,44,'台南县',7),(45,45,'高雄县',7),(46,46,'屏东县',7),(47,47,'澎湖县',7),(48,48,'台东县',7),(49,49,'花莲县',7),(50,50,'沈阳市',8),(51,51,'大连市',8),(52,52,'鞍山市',8),(53,53,'抚顺市',8),(54,54,'本溪市',8),(55,55,'丹东市',8),(56,56,'锦州市',8),(57,57,'营口市',8),(58,58,'阜新市',8),(59,59,'辽阳市',8),(60,60,'盘锦市',8),(61,61,'铁岭市',8),(62,62,'朝阳市',8),(63,63,'葫芦岛市',8),(64,64,'长春市',9),(65,65,'吉林市',9),(66,66,'四平市',9),(67,67,'辽源市',9),(68,68,'通化市',9),(69,69,'白山市',9),(70,70,'松原市',9),(71,71,'白城市',9),(72,72,'延边朝鲜族自治州',9),(73,73,'哈尔滨市',10),(74,74,'齐齐哈尔市',10),(75,75,'鹤岗市',10),(76,76,'双鸭山市',10),(77,77,'鸡西市',10),(78,78,'大庆市',10),(79,79,'伊春市',10),(80,80,'牡丹江市',10),(81,81,'佳木斯市',10),(82,82,'七台河市',10),(83,83,'黑河市',10),(84,84,'绥化市',10),(85,85,'大兴安岭地区',10),(86,86,'南京市',11),(87,87,'无锡市',11),(88,88,'徐州市',11),(89,89,'常州市',11),(90,90,'苏州市',11),(91,91,'南通市',11),(92,92,'连云港市',11),(93,93,'淮安市',11),(94,94,'盐城市',11),(95,95,'扬州市',11),(96,96,'镇江市',11),(97,97,'泰州市',11),(98,98,'宿迁市',11),(99,99,'杭州市',12),(100,100,'宁波市',12),(101,101,'温州市',12),(102,102,'嘉兴市',12),(103,103,'湖州市',12),(104,104,'绍兴市',12),(105,105,'金华市',12),(106,106,'衢州市',12),(107,107,'舟山市',12),(108,108,'台州市',12),(109,109,'丽水市',12),(110,110,'合肥市',13),(111,111,'芜湖市',13),(112,112,'蚌埠市',13),(113,113,'淮南市',13),(114,114,'马鞍山市',13),(115,115,'淮北市',13),(116,116,'铜陵市',13),(117,117,'安庆市',13),(118,118,'黄山市',13),(119,119,'滁州市',13),(120,120,'阜阳市',13),(121,121,'宿州市',13),(122,122,'巢湖市',13),(123,123,'六安市',13),(124,124,'亳州市',13),(125,125,'池州市',13),(126,126,'宣城市',13),(127,127,'福州市',14),(128,128,'厦门市',14),(129,129,'莆田市',14),(130,130,'三明市',14),(131,131,'泉州市',14),(132,132,'漳州市',14),(133,133,'南平市',14),(134,134,'龙岩市',14),(135,135,'宁德市',14),(136,136,'南昌市',15),(137,137,'景德镇市',15),(138,138,'萍乡市',15),(139,139,'九江市',15),(140,140,'新余市',15),(141,141,'鹰潭市',15),(142,142,'赣州市',15),(143,143,'吉安市',15),(144,144,'宜春市',15),(145,145,'抚州市',15),(146,146,'上饶市',15),(147,147,'济南市',16),(148,148,'青岛市',16),(149,149,'淄博市',16),(150,150,'枣庄市',16),(151,151,'东营市',16),(152,152,'烟台市',16),(153,153,'潍坊市',16),(154,154,'济宁市',16),(155,155,'泰安市',16),(156,156,'威海市',16),(157,157,'日照市',16),(158,158,'莱芜市',16),(159,159,'临沂市',16),(160,160,'德州市',16),(161,161,'聊城市',16),(162,162,'滨州市',16),(163,163,'菏泽市',16),(164,164,'郑州市',17),(165,165,'开封市',17),(166,166,'洛阳市',17),(167,167,'平顶山市',17),(168,168,'安阳市',17),(169,169,'鹤壁市',17),(170,170,'新乡市',17),(171,171,'焦作市',17),(172,172,'濮阳市',17),(173,173,'许昌市',17),(174,174,'漯河市',17),(175,175,'三门峡市',17),(176,176,'南阳市',17),(177,177,'商丘市',17),(178,178,'信阳市',17),(179,179,'周口市',17),(180,180,'驻马店市',17),(181,181,'济源市',17),(182,182,'武汉市',18),(183,183,'黄石市',18),(184,184,'十堰市',18),(185,185,'荆州市',18),(186,186,'宜昌市',18),(187,187,'襄樊市',18),(188,188,'鄂州市',18),(189,189,'荆门市',18),(190,190,'孝感市',18),(191,191,'黄冈市',18),(192,192,'咸宁市',18),(193,193,'随州市',18),(194,194,'仙桃市',18),(195,195,'天门市',18),(196,196,'潜江市',18),(197,197,'神农架林区',18),(198,198,'恩施土家族苗族自治州',18),(199,199,'长沙市',19),(200,200,'株洲市',19),(201,201,'湘潭市',19),(202,202,'衡阳市',19),(203,203,'邵阳市',19),(204,204,'岳阳市',19),(205,205,'常德市',19),(206,206,'张家界市',19),(207,207,'益阳市',19),(208,208,'郴州市',19),(209,209,'永州市',19),(210,210,'怀化市',19),(211,211,'娄底市',19),(212,212,'湘西土家族苗族自治州',19),(213,213,'广州市',20),(214,214,'深圳市',20),(215,215,'珠海市',20),(216,216,'汕头市',20),(217,217,'韶关市',20),(218,218,'佛山市',20),(219,219,'江门市',20),(220,220,'湛江市',20),(221,221,'茂名市',20),(222,222,'肇庆市',20),(223,223,'惠州市',20),(224,224,'梅州市',20),(225,225,'汕尾市',20),(226,226,'河源市',20),(227,227,'阳江市',20),(228,228,'清远市',20),(229,229,'东莞市',20),(230,230,'中山市',20),(231,231,'潮州市',20),(232,232,'揭阳市',20),(233,233,'云浮市',20),(234,234,'兰州市',21),(235,235,'金昌市',21),(236,236,'白银市',21),(237,237,'天水市',21),(238,238,'嘉峪关市',21),(239,239,'武威市',21),(240,240,'张掖市',21),(241,241,'平凉市',21),(242,242,'酒泉市',21),(243,243,'庆阳市',21),(244,244,'定西市',21),(245,245,'陇南市',21),(246,246,'临夏回族自治州',21),(247,247,'甘南藏族自治州',21),(248,248,'成都市',22),(249,249,'自贡市',22),(250,250,'攀枝花市',22),(251,251,'泸州市',22),(252,252,'德阳市',22),(253,253,'绵阳市',22),(254,254,'广元市',22),(255,255,'遂宁市',22),(256,256,'内江市',22),(257,257,'乐山市',22),(258,258,'南充市',22),(259,259,'眉山市',22),(260,260,'宜宾市',22),(261,261,'广安市',22),(262,262,'达州市',22),(263,263,'雅安市',22),(264,264,'巴中市',22),(265,265,'资阳市',22),(266,266,'阿坝藏族羌族自治州',22),(267,267,'甘孜藏族自治州',22),(268,268,'凉山彝族自治州',22),(269,269,'贵阳市',23),(270,270,'六盘水市',23),(271,271,'遵义市',23),(272,272,'安顺市',23),(273,273,'铜仁地区',23),(274,274,'毕节地区',23),(275,275,'黔西南布依族苗族自治州',23),(276,276,'黔东南苗族侗族自治州',23),(277,277,'黔南布依族苗族自治州',23),(278,278,'海口市',24),(279,279,'三亚市',24),(280,280,'五指山市',24),(281,281,'琼海市',24),(282,282,'儋州市',24),(283,283,'文昌市',24),(284,284,'万宁市',24),(285,285,'东方市',24),(286,286,'澄迈县',24),(287,287,'定安县',24),(288,288,'屯昌县',24),(289,289,'临高县',24),(290,290,'白沙黎族自治县',24),(291,291,'昌江黎族自治县',24),(292,292,'乐东黎族自治县',24),(293,293,'陵水黎族自治县',24),(294,294,'保亭黎族苗族自治县',24),(295,295,'琼中黎族苗族自治县',24),(296,296,'昆明市',25),(297,297,'曲靖市',25),(298,298,'玉溪市',25),(299,299,'保山市',25),(300,300,'昭通市',25),(301,301,'丽江市',25),(302,302,'思茅市',25),(303,303,'临沧市',25),(304,304,'文山壮族苗族自治州',25),(305,305,'红河哈尼族彝族自治州',25),(306,306,'西双版纳傣族自治州',25),(307,307,'楚雄彝族自治州',25),(308,308,'大理白族自治州',25),(309,309,'德宏傣族景颇族自治州',25),(310,310,'怒江傈傈族自治州',25),(311,311,'迪庆藏族自治州',25),(312,312,'西宁市',26),(313,313,'海东地区',26),(314,314,'海北藏族自治州',26),(315,315,'黄南藏族自治州',26),(316,316,'海南藏族自治州',26),(317,317,'果洛藏族自治州',26),(318,318,'玉树藏族自治州',26),(319,319,'海西蒙古族藏族自治州',26),(320,320,'西安市',27),(321,321,'铜川市',27),(322,322,'宝鸡市',27),(323,323,'咸阳市',27),(324,324,'渭南市',27),(325,325,'延安市',27),(326,326,'汉中市',27),(327,327,'榆林市',27),(328,328,'安康市',27),(329,329,'商洛市',27),(330,330,'南宁市',28),(331,331,'柳州市',28),(332,332,'桂林市',28),(333,333,'梧州市',28),(334,334,'北海市',28),(335,335,'防城港市',28),(336,336,'钦州市',28),(337,337,'贵港市',28),(338,338,'玉林市',28),(339,339,'百色市',28),(340,340,'贺州市',28),(341,341,'河池市',28),(342,342,'来宾市',28),(343,343,'崇左市',28),(344,344,'拉萨市',29),(345,345,'那曲地区',29),(346,346,'昌都地区',29),(347,347,'山南地区',29),(348,348,'日喀则地区',29),(349,349,'阿里地区',29),(350,350,'林芝地区',29),(351,351,'银川市',30),(352,352,'石嘴山市',30),(353,353,'吴忠市',30),(354,354,'固原市',30),(355,355,'中卫市',30),(356,356,'乌鲁木齐市',31),(357,357,'克拉玛依市',31),(358,358,'石河子市　',31),(359,359,'阿拉尔市',31),(360,360,'图木舒克市',31),(361,361,'五家渠市',31),(362,362,'吐鲁番市',31),(363,363,'阿克苏市',31),(364,364,'喀什市',31),(365,365,'哈密市',31),(366,366,'和田市',31),(367,367,'阿图什市',31),(368,368,'库尔勒市',31),(369,369,'昌吉市　',31),(370,370,'阜康市',31),(371,371,'米泉市',31),(372,372,'博乐市',31),(373,373,'伊宁市',31),(374,374,'奎屯市',31),(375,375,'塔城市',31),(376,376,'乌苏市',31),(377,377,'阿勒泰市',31),(378,378,'呼和浩特市',32),(379,379,'包头市',32),(380,380,'乌海市',32),(381,381,'赤峰市',32),(382,382,'通辽市',32),(383,383,'鄂尔多斯市',32),(384,384,'呼伦贝尔市',32),(385,385,'巴彦淖尔市',32),(386,386,'乌兰察布市',32),(387,387,'锡林郭勒盟',32),(388,388,'兴安盟',32),(389,389,'阿拉善盟',32),(390,390,'澳门特别行政区',33),(391,391,'香港特别行政区',34);
/*!40000 ALTER TABLE `api_cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_classinfo`
--

DROP TABLE IF EXISTS `api_classinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_classinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `class_id` varchar(20) NOT NULL,
  `major_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `class_id` (`class_id`),
  KEY `api_classinfo_major_id_70bec7d8_fk_api_majorinfo_id` (`major_id`),
  CONSTRAINT `api_classinfo_major_id_70bec7d8_fk_api_majorinfo_id` FOREIGN KEY (`major_id`) REFERENCES `api_majorinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_classinfo`
--

LOCK TABLES `api_classinfo` WRITE;
/*!40000 ALTER TABLE `api_classinfo` DISABLE KEYS */;
INSERT INTO `api_classinfo` VALUES (1,'190342A',10),(2,'190342B',10);
/*!40000 ALTER TABLE `api_classinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_classroom`
--

DROP TABLE IF EXISTS `api_classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_classroom` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `capacity` int NOT NULL,
  `building_id` int NOT NULL,
  `function_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `api_classroom_building_id_027a430d_fk_api_building_id` (`building_id`),
  KEY `api_classroom_function_id_317023e9_fk_api_function_id` (`function_id`),
  CONSTRAINT `api_classroom_building_id_027a430d_fk_api_building_id` FOREIGN KEY (`building_id`) REFERENCES `api_building` (`id`),
  CONSTRAINT `api_classroom_function_id_317023e9_fk_api_function_id` FOREIGN KEY (`function_id`) REFERENCES `api_function` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_classroom`
--

LOCK TABLES `api_classroom` WRITE;
/*!40000 ALTER TABLE `api_classroom` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_classroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_classtime`
--

DROP TABLE IF EXISTS `api_classtime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_classtime` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_classtime`
--

LOCK TABLES `api_classtime` WRITE;
/*!40000 ALTER TABLE `api_classtime` DISABLE KEYS */;
INSERT INTO `api_classtime` VALUES (1,'周一1-2节'),(2,'周一3-4节'),(3,'周一5-6节'),(4,'周一7-8节'),(5,'周一9-10节'),(6,'周一11-12节'),(7,'周二1-2节'),(8,'周二3-4节'),(9,'周二5-6节'),(10,'周二7-8节'),(11,'周二9-10节'),(12,'周二11-12节'),(13,'周三1-2节'),(14,'周三3-4节'),(15,'周三5-6节'),(16,'周三7-8节'),(17,'周三9-10节'),(18,'周三11-12节'),(19,'周四1-2节'),(20,'周四3-4节'),(21,'周四5-6节'),(22,'周四7-8节'),(23,'周四9-10节'),(24,'周四11-12节'),(25,'周五1-2节'),(26,'周五3-4节'),(27,'周五5-6节'),(28,'周五7-8节'),(29,'周五9-10节'),(30,'周五11-12节'),(31,'周六1-2节'),(32,'周六3-4节'),(33,'周六5-6节'),(34,'周六7-8节'),(35,'周六9-10节'),(36,'周六11-12节'),(37,'周日1-2节'),(38,'周日3-4节'),(39,'周日5-6节'),(40,'周日7-8节'),(41,'周日9-10节'),(42,'周日11-12节');
/*!40000 ALTER TABLE `api_classtime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_collegeinfo`
--

DROP TABLE IF EXISTS `api_collegeinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_collegeinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `college_id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `college_id` (`college_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_collegeinfo`
--

LOCK TABLES `api_collegeinfo` WRITE;
/*!40000 ALTER TABLE `api_collegeinfo` DISABLE KEYS */;
INSERT INTO `api_collegeinfo` VALUES (1,1,'航空工程学院'),(2,11,'电子信息与自动化学院'),(4,3,'计算机科学与技术学院'),(5,6,'外国语学院'),(6,4,'空中交通管理学院'),(7,5,'经济与管理学院'),(8,7,'机场学院'),(9,2,'理学院'),(10,8,'法学院'),(11,9,'体育特长生'),(12,13,'飞行技术学院'),(13,60,'中欧航空工程师'),(14,80,'职业技术学院'),(15,81,'乘务学院');
/*!40000 ALTER TABLE `api_collegeinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_collegeinfo4tc`
--

DROP TABLE IF EXISTS `api_collegeinfo4tc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_collegeinfo4tc` (
  `id` int NOT NULL AUTO_INCREMENT,
  `college_id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `college_id` (`college_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_collegeinfo4tc`
--

LOCK TABLES `api_collegeinfo4tc` WRITE;
/*!40000 ALTER TABLE `api_collegeinfo4tc` DISABLE KEYS */;
INSERT INTO `api_collegeinfo4tc` VALUES (1,1,'航空工程学院'),(2,11,'电子信息与自动化学院'),(4,3,'计算机科学与技术学院'),(5,6,'外国语学院'),(6,4,'空中交通管理学院'),(7,5,'经济与管理学院'),(8,7,'机场学院'),(9,2,'理学院'),(10,8,'法学院'),(11,9,'体育特长生'),(12,13,'飞行技术学院'),(13,60,'中欧航空工程师'),(14,80,'职业技术学院'),(15,81,'乘务学院'),(16,101,'工程技术训练中心');
/*!40000 ALTER TABLE `api_collegeinfo4tc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_countries`
--

DROP TABLE IF EXISTS `api_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_countries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `aid` int NOT NULL,
  `atitle` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=241 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_countries`
--

LOCK TABLES `api_countries` WRITE;
/*!40000 ALTER TABLE `api_countries` DISABLE KEYS */;
INSERT INTO `api_countries` VALUES (1,1,'中华人民共和国'),(2,2,'阿尔巴尼亚'),(3,3,'阿尔及利亚'),(4,4,'阿富汗'),(5,5,'阿根廷'),(6,6,'阿拉伯联合酋长国'),(7,7,'阿鲁巴'),(8,8,'阿曼'),(9,9,'阿塞拜疆'),(10,10,'阿森松岛'),(11,11,'埃及'),(12,12,'埃塞俄比亚'),(13,13,'爱尔兰'),(14,14,'爱沙尼亚'),(15,15,'安道尔'),(16,16,'安哥拉'),(17,17,'安圭拉'),(18,18,'安提瓜岛和巴布达'),(19,19,'奥地利'),(20,20,'奥兰群岛'),(21,21,'澳大利亚'),(22,22,'巴巴多斯岛'),(23,23,'巴布亚新几内亚'),(24,24,'巴哈马'),(25,25,'巴基斯坦'),(26,26,'巴拉圭'),(27,27,'巴勒斯坦'),(28,28,'巴林'),(29,29,'巴拿马'),(30,30,'巴西'),(31,31,'白俄罗斯'),(32,32,'百慕大'),(33,33,'保加利亚'),(34,34,'北马里亚纳群岛'),(35,35,'贝宁'),(36,36,'比利时'),(37,37,'冰岛'),(38,38,'波多黎各'),(39,39,'波兰'),(40,40,'波斯尼亚和黑塞哥维那'),(41,41,'玻利维亚'),(42,42,'伯利兹'),(43,43,'博茨瓦纳'),(44,44,'不丹'),(45,45,'布基纳法索'),(46,46,'布隆迪'),(47,47,'布韦岛'),(48,48,'朝鲜'),(49,49,'丹麦'),(50,50,'德国'),(51,51,'东帝汶'),(52,52,'多哥'),(53,53,'多米尼加'),(54,54,'多米尼加共和国'),(55,55,'俄罗斯'),(56,56,'厄瓜多尔'),(57,57,'厄立特里亚'),(58,58,'法国'),(59,59,'法罗群岛'),(60,60,'法属波利尼西亚'),(61,61,'法属圭亚那'),(62,62,'法属南部领地'),(63,63,'梵蒂冈'),(64,64,'菲律宾'),(65,65,'斐济'),(66,66,'芬兰'),(67,67,'佛得角'),(68,68,'弗兰克群岛'),(69,69,'冈比亚'),(70,70,'刚果'),(71,71,'刚果民主共和国'),(72,72,'哥伦比亚'),(73,73,'哥斯达黎加'),(74,74,'格恩西岛'),(75,75,'格林纳达'),(76,76,'格陵兰'),(77,77,'古巴'),(78,78,'瓜德罗普'),(79,79,'关岛'),(80,80,'圭亚那'),(81,81,'哈萨克斯坦'),(82,82,'海地'),(83,83,'韩国'),(84,84,'荷兰'),(85,85,'荷属安地列斯'),(86,86,'赫德和麦克唐纳群岛'),(87,87,'洪都拉斯'),(88,88,'基里巴斯'),(89,89,'吉布提'),(90,90,'吉尔吉斯斯坦'),(91,91,'几内亚'),(92,92,'几内亚比绍'),(93,93,'加拿大'),(94,94,'加纳'),(95,95,'加蓬'),(96,96,'柬埔寨'),(97,97,'捷克共和国'),(98,98,'津巴布韦'),(99,99,'喀麦隆'),(100,100,'卡塔尔'),(101,101,'开曼群岛'),(102,102,'科科斯群岛'),(103,103,'科摩罗'),(104,104,'科特迪瓦'),(105,105,'科威特'),(106,106,'克罗地亚'),(107,107,'肯尼亚'),(108,108,'库克群岛'),(109,109,'拉脱维亚'),(110,110,'莱索托'),(111,111,'老挝'),(112,112,'黎巴嫩'),(113,113,'立陶宛'),(114,114,'利比里亚'),(115,115,'利比亚'),(116,116,'列支敦士登'),(117,117,'留尼旺岛'),(118,118,'卢森堡'),(119,119,'卢旺达'),(120,120,'罗马尼亚'),(121,121,'马达加斯加'),(122,122,'马尔代夫'),(123,123,'马耳他'),(124,124,'马拉维'),(125,125,'马来西亚'),(126,126,'马里'),(127,127,'马其顿'),(128,128,'马绍尔群岛'),(129,129,'马提尼克'),(130,130,'马约特岛'),(131,131,'曼岛'),(132,132,'毛里求斯'),(133,133,'毛里塔尼亚'),(134,134,'美国'),(135,135,'美属萨摩亚'),(136,136,'美属外岛'),(137,137,'蒙古'),(138,138,'蒙特塞拉特'),(139,139,'孟加拉'),(140,140,'秘鲁'),(141,141,'密克罗尼西亚'),(142,142,'缅甸'),(143,143,'摩尔多瓦'),(144,144,'摩洛哥'),(145,145,'摩纳哥'),(146,146,'莫桑比克'),(147,147,'墨西哥'),(148,148,'纳米比亚'),(149,149,'南非'),(150,150,'南极洲'),(151,151,'南乔治亚和南桑德威奇群岛'),(152,152,'瑙鲁'),(153,153,'尼泊尔'),(154,154,'尼加拉瓜'),(155,155,'尼日尔'),(156,156,'尼日利亚'),(157,157,'纽埃'),(158,158,'挪威'),(159,159,'诺福克'),(160,160,'帕劳群岛'),(161,161,'皮特凯恩'),(162,162,'葡萄牙'),(163,163,'乔治亚'),(164,164,'日本'),(165,165,'瑞典'),(166,166,'瑞士'),(167,167,'萨尔瓦多'),(168,168,'萨摩亚'),(169,169,'塞尔维亚,黑山'),(170,170,'塞拉利昂'),(171,171,'塞内加尔'),(172,172,'塞浦路斯'),(173,173,'塞舌尔'),(174,174,'沙特阿拉伯'),(175,175,'圣诞岛'),(176,176,'圣多美和普林西比'),(177,177,'圣赫勒拿'),(178,178,'圣基茨和尼维斯'),(179,179,'圣卢西亚'),(180,180,'圣马力诺'),(181,181,'圣皮埃尔和米克隆群岛'),(182,182,'圣文森特和格林纳丁斯'),(183,183,'斯里兰卡'),(184,184,'斯洛伐克'),(185,185,'斯洛文尼亚'),(186,186,'斯瓦尔巴和扬马廷'),(187,187,'斯威士兰'),(188,188,'苏丹'),(189,189,'苏里南'),(190,190,'所罗门群岛'),(191,191,'索马里'),(192,192,'塔吉克斯坦'),(193,193,'泰国'),(194,194,'坦桑尼亚'),(195,195,'汤加'),(196,196,'特克斯和凯克特斯群岛'),(197,197,'特里斯坦达昆哈'),(198,198,'特立尼达和多巴哥'),(199,199,'突尼斯'),(200,200,'图瓦卢'),(201,201,'土耳其'),(202,202,'土库曼斯坦'),(203,203,'托克劳'),(204,204,'瓦利斯和福图纳'),(205,205,'瓦努阿图'),(206,206,'危地马拉'),(207,207,'维尔京群岛，美属'),(208,208,'维尔京群岛，英属'),(209,209,'委内瑞拉'),(210,210,'文莱'),(211,211,'乌干达'),(212,212,'乌克兰'),(213,213,'乌拉圭'),(214,214,'乌兹别克斯坦'),(215,215,'西班牙'),(216,216,'希腊'),(217,217,'新加坡'),(218,218,'新喀里多尼亚'),(219,219,'新西兰'),(220,220,'匈牙利'),(221,221,'叙利亚'),(222,222,'牙买加'),(223,223,'亚美尼亚'),(224,224,'也门'),(225,225,'伊拉克'),(226,226,'伊朗'),(227,227,'以色列'),(228,228,'意大利'),(229,229,'印度'),(230,230,'印度尼西亚'),(231,231,'英国'),(232,232,'英属印度洋领地'),(233,233,'约旦'),(234,234,'越南'),(235,235,'赞比亚'),(236,236,'泽西岛'),(237,237,'乍得'),(238,238,'直布罗陀'),(239,239,'智利'),(240,240,'中非共和国');
/*!40000 ALTER TABLE `api_countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_course`
--

DROP TABLE IF EXISTS `api_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cou_id` varchar(10) NOT NULL,
  `name` varchar(10) NOT NULL,
  `classhour` int NOT NULL,
  `hourperweek` double NOT NULL,
  `credit` double NOT NULL,
  `betyear` int NOT NULL,
  `elective` tinyint(1) NOT NULL,
  `priority` int NOT NULL,
  `college_id` int NOT NULL,
  `function_id` int NOT NULL,
  `pre_course_id` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cou_id` (`cou_id`),
  UNIQUE KEY `name` (`name`),
  KEY `api_course_college_id_4326ad66_fk_api_collegeinfo4tc_id` (`college_id`),
  KEY `api_course_function_id_b81fa053_fk_api_function_id` (`function_id`),
  KEY `api_course_pre_course_id_5f4eb12e_fk_api_course_id` (`pre_course_id`),
  CONSTRAINT `api_course_college_id_4326ad66_fk_api_collegeinfo4tc_id` FOREIGN KEY (`college_id`) REFERENCES `api_collegeinfo4tc` (`id`),
  CONSTRAINT `api_course_function_id_b81fa053_fk_api_function_id` FOREIGN KEY (`function_id`) REFERENCES `api_function` (`id`),
  CONSTRAINT `api_course_pre_course_id_5f4eb12e_fk_api_course_id` FOREIGN KEY (`pre_course_id`) REFERENCES `api_course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_course`
--

LOCK TABLES `api_course` WRITE;
/*!40000 ALTER TABLE `api_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_function`
--

DROP TABLE IF EXISTS `api_function`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_function` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_function`
--

LOCK TABLES `api_function` WRITE;
/*!40000 ALTER TABLE `api_function` DISABLE KEYS */;
INSERT INTO `api_function` VALUES (2,'上机'),(4,'实践'),(3,'实验'),(1,'普通');
/*!40000 ALTER TABLE `api_function` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_idnumber`
--

DROP TABLE IF EXISTS `api_idnumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_idnumber` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idnumber` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idnumber` (`idnumber`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_idnumber`
--

LOCK TABLES `api_idnumber` WRITE;
/*!40000 ALTER TABLE `api_idnumber` DISABLE KEYS */;
INSERT INTO `api_idnumber` VALUES (2,'14917181571945548'),(4,'170330892782658340'),(1,'869558921083808000'),(3,'896965538850054100');
/*!40000 ALTER TABLE `api_idnumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_majorinfo`
--

DROP TABLE IF EXISTS `api_majorinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_majorinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `major_id` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `college_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_majorinfo_college_id_caeb63ef_fk_api_collegeinfo_id` (`college_id`),
  CONSTRAINT `api_majorinfo_college_id_caeb63ef_fk_api_collegeinfo_id` FOREIGN KEY (`college_id`) REFERENCES `api_collegeinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_majorinfo`
--

LOCK TABLES `api_majorinfo` WRITE;
/*!40000 ALTER TABLE `api_majorinfo` DISABLE KEYS */;
INSERT INTO `api_majorinfo` VALUES (1,1,'飞行器动力工程',1),(2,2,'飞行器制造工程',1),(3,3,'工业工程',1),(4,4,'机械电子工程',1),(5,5,'航空电子',2),(6,6,'通信工程',2),(7,7,'航空电气',2),(8,8,'自动化',2),(9,9,'计算机科学与技术',4),(10,10,'信息安全',4);
/*!40000 ALTER TABLE `api_majorinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_majorinfo_course`
--

DROP TABLE IF EXISTS `api_majorinfo_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_majorinfo_course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `majorinfo_id` int NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_majorinfo_course_majorinfo_id_course_id_81d126d6_uniq` (`majorinfo_id`,`course_id`),
  KEY `api_majorinfo_course_course_id_82ec94af_fk_api_course_id` (`course_id`),
  CONSTRAINT `api_majorinfo_course_course_id_82ec94af_fk_api_course_id` FOREIGN KEY (`course_id`) REFERENCES `api_course` (`id`),
  CONSTRAINT `api_majorinfo_course_majorinfo_id_efe66ef8_fk_api_majorinfo_id` FOREIGN KEY (`majorinfo_id`) REFERENCES `api_majorinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_majorinfo_course`
--

LOCK TABLES `api_majorinfo_course` WRITE;
/*!40000 ALTER TABLE `api_majorinfo_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_majorinfo_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_message`
--

DROP TABLE IF EXISTS `api_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fromwho` varchar(30) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` varchar(1000) DEFAULT NULL,
  `gettime` datetime(6) NOT NULL,
  `finishtime` datetime(6) NOT NULL,
  `isFinished` int NOT NULL,
  `result` varchar(30) NOT NULL,
  `admin_id` int DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `api_message_admin_id_997b7838_fk_api_admininfo_id` (`admin_id`),
  KEY `api_message_student_id_42494200_fk_api_studentinfo_id` (`student_id`),
  KEY `api_message_teacher_id_044f8d91_fk_api_teacherinfo_id` (`teacher_id`),
  CONSTRAINT `api_message_admin_id_997b7838_fk_api_admininfo_id` FOREIGN KEY (`admin_id`) REFERENCES `api_admininfo` (`id`),
  CONSTRAINT `api_message_student_id_42494200_fk_api_studentinfo_id` FOREIGN KEY (`student_id`) REFERENCES `api_studentinfo` (`id`),
  CONSTRAINT `api_message_teacher_id_044f8d91_fk_api_teacherinfo_id` FOREIGN KEY (`teacher_id`) REFERENCES `api_teacherinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_message`
--

LOCK TABLES `api_message` WRITE;
/*!40000 ALTER TABLE `api_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_outlook`
--

DROP TABLE IF EXISTS `api_outlook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_outlook` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_outlook`
--

LOCK TABLES `api_outlook` WRITE;
/*!40000 ALTER TABLE `api_outlook` DISABLE KEYS */;
INSERT INTO `api_outlook` VALUES (1,'中共党员'),(2,'中共预备党员'),(3,'共青团员'),(4,'民革党员'),(5,'民盟盟员'),(6,'民建会员'),(7,'民进会员'),(8,'农工党党员'),(9,'致公党党员'),(10,'九三学社社员'),(11,'台盟盟员'),(12,'无党派人士'),(13,'群众');
/*!40000 ALTER TABLE `api_outlook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_provinces`
--

DROP TABLE IF EXISTS `api_provinces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_provinces` (
  `id` int NOT NULL AUTO_INCREMENT,
  `aid` int NOT NULL,
  `atitle` varchar(30) NOT NULL,
  `Country_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_provinces_Country_id_dc0af681_fk_api_countries_id` (`Country_id`),
  CONSTRAINT `api_provinces_Country_id_dc0af681_fk_api_countries_id` FOREIGN KEY (`Country_id`) REFERENCES `api_countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_provinces`
--

LOCK TABLES `api_provinces` WRITE;
/*!40000 ALTER TABLE `api_provinces` DISABLE KEYS */;
INSERT INTO `api_provinces` VALUES (1,1,'北京市',1),(2,2,'天津市',1),(3,3,'上海市',1),(4,4,'重庆市',1),(5,5,'河北省',1),(6,6,'山西省',1),(7,7,'台湾省',1),(8,8,'辽宁省',1),(9,9,'吉林省',1),(10,10,'黑龙江省',1),(11,11,'江苏省',1),(12,12,'浙江省',1),(13,13,'安徽省',1),(14,14,'福建省',1),(15,15,'江西省',1),(16,16,'山东省',1),(17,17,'河南省',1),(18,18,'湖北省',1),(19,19,'湖南省',1),(20,20,'广东省',1),(21,21,'甘肃省',1),(22,22,'四川省',1),(23,23,'贵州省',1),(24,24,'海南省',1),(25,25,'云南省',1),(26,26,'青海省',1),(27,27,'陕西省',1),(28,28,'广西壮族自治区',1),(29,29,'西藏自治区',1),(30,30,'宁夏回族自治区',1),(31,31,'新疆维吾尔自治区',1),(32,32,'内蒙古自治区',1),(33,33,'澳门特别行政区',1),(34,34,'香港特别行政区',1);
/*!40000 ALTER TABLE `api_provinces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_results`
--

DROP TABLE IF EXISTS `api_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_results` (
  `id` int NOT NULL AUTO_INCREMENT,
  `result` int NOT NULL,
  `examtime` date NOT NULL,
  `course_id` int NOT NULL,
  `student_id` int NOT NULL,
  `teacher_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_results_course_id_6ed2f306_fk_api_course_id` (`course_id`),
  KEY `api_results_student_id_80ba3eef_fk_api_studentinfo_id` (`student_id`),
  KEY `api_results_teacher_id_46b3698e_fk_api_teacherinfo_id` (`teacher_id`),
  CONSTRAINT `api_results_course_id_6ed2f306_fk_api_course_id` FOREIGN KEY (`course_id`) REFERENCES `api_course` (`id`),
  CONSTRAINT `api_results_student_id_80ba3eef_fk_api_studentinfo_id` FOREIGN KEY (`student_id`) REFERENCES `api_studentinfo` (`id`),
  CONSTRAINT `api_results_teacher_id_46b3698e_fk_api_teacherinfo_id` FOREIGN KEY (`teacher_id`) REFERENCES `api_teacherinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_results`
--

LOCK TABLES `api_results` WRITE;
/*!40000 ALTER TABLE `api_results` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_student2course`
--

DROP TABLE IF EXISTS `api_student2course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_student2course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `isfinished` tinyint(1) NOT NULL,
  `course_id_id` int NOT NULL,
  `student_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_student2course_course_id_id_2ce3255f_fk_api_course_id` (`course_id_id`),
  KEY `api_student2course_student_id_id_0d9bb195_fk_api_studentinfo_id` (`student_id_id`),
  CONSTRAINT `api_student2course_course_id_id_2ce3255f_fk_api_course_id` FOREIGN KEY (`course_id_id`) REFERENCES `api_course` (`id`),
  CONSTRAINT `api_student2course_student_id_id_0d9bb195_fk_api_studentinfo_id` FOREIGN KEY (`student_id_id`) REFERENCES `api_studentinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_student2course`
--

LOCK TABLES `api_student2course` WRITE;
/*!40000 ALTER TABLE `api_student2course` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_student2course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_studentinfo`
--

DROP TABLE IF EXISTS `api_studentinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_studentinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stu_id` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(20) NOT NULL,
  `birthday` date NOT NULL,
  `sex` varchar(5) NOT NULL,
  `entryTime` date NOT NULL,
  `grade` int NOT NULL,
  `nation_id` int NOT NULL,
  `credit` double NOT NULL,
  `Class_id` int NOT NULL,
  `IDnumber_id` int NOT NULL,
  `native_id` int NOT NULL,
  `outlook_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stu_id` (`stu_id`),
  KEY `api_studentinfo_Class_id_749ddc3a_fk_api_classinfo_id` (`Class_id`),
  KEY `api_studentinfo_IDnumber_id_309606ea_fk_api_idnumber_id` (`IDnumber_id`),
  KEY `api_studentinfo_native_id_efba4422_fk_api_cities_id` (`native_id`),
  KEY `api_studentinfo_outlook_id_b7e5aec5_fk_api_outlook_id` (`outlook_id`),
  KEY `api_studentinfo_nation_id_ba3409dd` (`nation_id`),
  CONSTRAINT `api_studentinfo_Class_id_749ddc3a_fk_api_classinfo_id` FOREIGN KEY (`Class_id`) REFERENCES `api_classinfo` (`id`),
  CONSTRAINT `api_studentinfo_IDnumber_id_309606ea_fk_api_idnumber_id` FOREIGN KEY (`IDnumber_id`) REFERENCES `api_idnumber` (`id`),
  CONSTRAINT `api_studentinfo_nation_id_ba3409dd_fk_api_countries_id` FOREIGN KEY (`nation_id`) REFERENCES `api_countries` (`id`),
  CONSTRAINT `api_studentinfo_native_id_efba4422_fk_api_cities_id` FOREIGN KEY (`native_id`) REFERENCES `api_cities` (`id`),
  CONSTRAINT `api_studentinfo_outlook_id_b7e5aec5_fk_api_outlook_id` FOREIGN KEY (`outlook_id`) REFERENCES `api_outlook` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_studentinfo`
--

LOCK TABLES `api_studentinfo` WRITE;
/*!40000 ALTER TABLE `api_studentinfo` DISABLE KEYS */;
INSERT INTO `api_studentinfo` VALUES (1,'190342205','123456','郭江鑫','2000-01-01','男','2019-08-25',2,1,0,2,1,386,3),(2,'190146841','123456','邹嘉旭','2001-06-13','男','2019-08-25',2,1,0,2,2,64,3),(4,'190342209','123456','金泽萱','2000-06-12','男','2019-08-25',2,1,0,2,2,356,3);
/*!40000 ALTER TABLE `api_studentinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_teacher2time`
--

DROP TABLE IF EXISTS `api_teacher2time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_teacher2time` (
  `id` int NOT NULL AUTO_INCREMENT,
  `classroom_id` int NOT NULL,
  `course_id_id` int NOT NULL,
  `teacher_id_id` int NOT NULL,
  `time_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_teacher2time_classroom_id_0fcd9f55_fk_api_classroom_id` (`classroom_id`),
  KEY `api_teacher2time_course_id_id_14fdec79_fk_api_course_id` (`course_id_id`),
  KEY `api_teacher2time_teacher_id_id_7aa88032_fk_api_teacherinfo_id` (`teacher_id_id`),
  KEY `api_teacher2time_time_id_id_ea3f2ca3_fk_api_classtime_id` (`time_id_id`),
  CONSTRAINT `api_teacher2time_classroom_id_0fcd9f55_fk_api_classroom_id` FOREIGN KEY (`classroom_id`) REFERENCES `api_classroom` (`id`),
  CONSTRAINT `api_teacher2time_course_id_id_14fdec79_fk_api_course_id` FOREIGN KEY (`course_id_id`) REFERENCES `api_course` (`id`),
  CONSTRAINT `api_teacher2time_teacher_id_id_7aa88032_fk_api_teacherinfo_id` FOREIGN KEY (`teacher_id_id`) REFERENCES `api_teacherinfo` (`id`),
  CONSTRAINT `api_teacher2time_time_id_id_ea3f2ca3_fk_api_classtime_id` FOREIGN KEY (`time_id_id`) REFERENCES `api_classtime` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_teacher2time`
--

LOCK TABLES `api_teacher2time` WRITE;
/*!40000 ALTER TABLE `api_teacher2time` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_teacher2time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_teacher_title`
--

DROP TABLE IF EXISTS `api_teacher_title`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_teacher_title` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_teacher_title`
--

LOCK TABLES `api_teacher_title` WRITE;
/*!40000 ALTER TABLE `api_teacher_title` DISABLE KEYS */;
INSERT INTO `api_teacher_title` VALUES (1,'教授一级'),(2,'教授二级'),(3,'教授三级'),(4,'教授四级'),(5,'副教授一级'),(6,'副教授二级'),(7,'副教授三级'),(8,'讲师一级'),(9,'讲师二级'),(10,'讲师三级'),(11,'助教一级'),(12,'助教二级'),(13,'助教三级');
/*!40000 ALTER TABLE `api_teacher_title` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_teacherinfo`
--

DROP TABLE IF EXISTS `api_teacherinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_teacherinfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tea_id` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(20) NOT NULL,
  `birthday` date NOT NULL,
  `sex` varchar(5) NOT NULL,
  `entryTime` date NOT NULL,
  `nation` int NOT NULL,
  `IDnumber_id` int NOT NULL,
  `college_id` int NOT NULL,
  `native_id` int NOT NULL,
  `outlook_id` int NOT NULL,
  `title_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tea_id` (`tea_id`),
  KEY `api_teacherinfo_IDnumber_id_a8add07b_fk_api_idnumber_id` (`IDnumber_id`),
  KEY `api_teacherinfo_college_id_c456fc8f_fk_api_collegeinfo4tc_id` (`college_id`),
  KEY `api_teacherinfo_native_id_985a5060_fk_api_cities_id` (`native_id`),
  KEY `api_teacherinfo_outlook_id_22cbfb84_fk_api_outlook_id` (`outlook_id`),
  KEY `api_teacherinfo_title_id_592c0029_fk_api_teacher_title_id` (`title_id`),
  CONSTRAINT `api_teacherinfo_college_id_c456fc8f_fk_api_collegeinfo4tc_id` FOREIGN KEY (`college_id`) REFERENCES `api_collegeinfo4tc` (`id`),
  CONSTRAINT `api_teacherinfo_IDnumber_id_a8add07b_fk_api_idnumber_id` FOREIGN KEY (`IDnumber_id`) REFERENCES `api_idnumber` (`id`),
  CONSTRAINT `api_teacherinfo_native_id_985a5060_fk_api_cities_id` FOREIGN KEY (`native_id`) REFERENCES `api_cities` (`id`),
  CONSTRAINT `api_teacherinfo_outlook_id_22cbfb84_fk_api_outlook_id` FOREIGN KEY (`outlook_id`) REFERENCES `api_outlook` (`id`),
  CONSTRAINT `api_teacherinfo_title_id_592c0029_fk_api_teacher_title_id` FOREIGN KEY (`title_id`) REFERENCES `api_teacher_title` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_teacherinfo`
--

LOCK TABLES `api_teacherinfo` WRITE;
/*!40000 ALTER TABLE `api_teacherinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_teacherinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `api_teacherinfo_course`
--

DROP TABLE IF EXISTS `api_teacherinfo_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_teacherinfo_course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `teacherinfo_id` int NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_teacherinfo_course_teacherinfo_id_course_id_76fcc55f_uniq` (`teacherinfo_id`,`course_id`),
  KEY `api_teacherinfo_course_course_id_4f3d1f3f_fk_api_course_id` (`course_id`),
  CONSTRAINT `api_teacherinfo_cour_teacherinfo_id_b342f453_fk_api_teach` FOREIGN KEY (`teacherinfo_id`) REFERENCES `api_teacherinfo` (`id`),
  CONSTRAINT `api_teacherinfo_course_course_id_4f3d1f3f_fk_api_course_id` FOREIGN KEY (`course_id`) REFERENCES `api_course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_teacherinfo_course`
--

LOCK TABLES `api_teacherinfo_course` WRITE;
/*!40000 ALTER TABLE `api_teacherinfo_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `api_teacherinfo_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add admin info',7,'add_admininfo'),(26,'Can change admin info',7,'change_admininfo'),(27,'Can delete admin info',7,'delete_admininfo'),(28,'Can view admin info',7,'view_admininfo'),(29,'Can add areas',8,'add_areas'),(30,'Can change areas',8,'change_areas'),(31,'Can delete areas',8,'delete_areas'),(32,'Can view areas',8,'view_areas'),(33,'Can add building',9,'add_building'),(34,'Can change building',9,'change_building'),(35,'Can delete building',9,'delete_building'),(36,'Can view building',9,'view_building'),(37,'Can add cities',10,'add_cities'),(38,'Can change cities',10,'change_cities'),(39,'Can delete cities',10,'delete_cities'),(40,'Can view cities',10,'view_cities'),(41,'Can add class info',11,'add_classinfo'),(42,'Can change class info',11,'change_classinfo'),(43,'Can delete class info',11,'delete_classinfo'),(44,'Can view class info',11,'view_classinfo'),(45,'Can add class room',12,'add_classroom'),(46,'Can change class room',12,'change_classroom'),(47,'Can delete class room',12,'delete_classroom'),(48,'Can view class room',12,'view_classroom'),(49,'Can add class time',13,'add_classtime'),(50,'Can change class time',13,'change_classtime'),(51,'Can delete class time',13,'delete_classtime'),(52,'Can view class time',13,'view_classtime'),(53,'Can add college info',14,'add_collegeinfo'),(54,'Can change college info',14,'change_collegeinfo'),(55,'Can delete college info',14,'delete_collegeinfo'),(56,'Can view college info',14,'view_collegeinfo'),(57,'Can add college info4tc',15,'add_collegeinfo4tc'),(58,'Can change college info4tc',15,'change_collegeinfo4tc'),(59,'Can delete college info4tc',15,'delete_collegeinfo4tc'),(60,'Can view college info4tc',15,'view_collegeinfo4tc'),(61,'Can add countries',16,'add_countries'),(62,'Can change countries',16,'change_countries'),(63,'Can delete countries',16,'delete_countries'),(64,'Can view countries',16,'view_countries'),(65,'Can add course',17,'add_course'),(66,'Can change course',17,'change_course'),(67,'Can delete course',17,'delete_course'),(68,'Can view course',17,'view_course'),(69,'Can add function',18,'add_function'),(70,'Can change function',18,'change_function'),(71,'Can delete function',18,'delete_function'),(72,'Can view function',18,'view_function'),(73,'Can add id number',19,'add_idnumber'),(74,'Can change id number',19,'change_idnumber'),(75,'Can delete id number',19,'delete_idnumber'),(76,'Can view id number',19,'view_idnumber'),(77,'Can add outlook',20,'add_outlook'),(78,'Can change outlook',20,'change_outlook'),(79,'Can delete outlook',20,'delete_outlook'),(80,'Can view outlook',20,'view_outlook'),(81,'Can add student2 course',21,'add_student2course'),(82,'Can change student2 course',21,'change_student2course'),(83,'Can delete student2 course',21,'delete_student2course'),(84,'Can view student2 course',21,'view_student2course'),(85,'Can add teacher_title',22,'add_teacher_title'),(86,'Can change teacher_title',22,'change_teacher_title'),(87,'Can delete teacher_title',22,'delete_teacher_title'),(88,'Can view teacher_title',22,'view_teacher_title'),(89,'Can add teacher info',23,'add_teacherinfo'),(90,'Can change teacher info',23,'change_teacherinfo'),(91,'Can delete teacher info',23,'delete_teacherinfo'),(92,'Can view teacher info',23,'view_teacherinfo'),(93,'Can add teacher2 time',24,'add_teacher2time'),(94,'Can change teacher2 time',24,'change_teacher2time'),(95,'Can delete teacher2 time',24,'delete_teacher2time'),(96,'Can view teacher2 time',24,'view_teacher2time'),(97,'Can add student info',25,'add_studentinfo'),(98,'Can change student info',25,'change_studentinfo'),(99,'Can delete student info',25,'delete_studentinfo'),(100,'Can view student info',25,'view_studentinfo'),(101,'Can add results',26,'add_results'),(102,'Can change results',26,'change_results'),(103,'Can delete results',26,'delete_results'),(104,'Can view results',26,'view_results'),(105,'Can add provinces',27,'add_provinces'),(106,'Can change provinces',27,'change_provinces'),(107,'Can delete provinces',27,'delete_provinces'),(108,'Can view provinces',27,'view_provinces'),(109,'Can add message',28,'add_message'),(110,'Can change message',28,'change_message'),(111,'Can delete message',28,'delete_message'),(112,'Can view message',28,'view_message'),(113,'Can add major info',29,'add_majorinfo'),(114,'Can change major info',29,'change_majorinfo'),(115,'Can delete major info',29,'delete_majorinfo'),(116,'Can view major info',29,'view_majorinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'api','admininfo'),(8,'api','areas'),(9,'api','building'),(10,'api','cities'),(11,'api','classinfo'),(12,'api','classroom'),(13,'api','classtime'),(14,'api','collegeinfo'),(15,'api','collegeinfo4tc'),(16,'api','countries'),(17,'api','course'),(18,'api','function'),(19,'api','idnumber'),(29,'api','majorinfo'),(28,'api','message'),(20,'api','outlook'),(27,'api','provinces'),(26,'api','results'),(21,'api','student2course'),(25,'api','studentinfo'),(22,'api','teacher_title'),(24,'api','teacher2time'),(23,'api','teacherinfo'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-05-25 10:42:15.502682'),(2,'auth','0001_initial','2021-05-25 10:42:15.748875'),(3,'admin','0001_initial','2021-05-25 10:42:16.431796'),(4,'admin','0002_logentry_remove_auto_add','2021-05-25 10:42:16.604292'),(5,'admin','0003_logentry_add_action_flag_choices','2021-05-25 10:42:16.622612'),(6,'api','0001_initial','2021-05-25 10:42:17.915180'),(7,'contenttypes','0002_remove_content_type_name','2021-05-25 10:42:20.992160'),(8,'auth','0002_alter_permission_name_max_length','2021-05-25 10:42:21.077130'),(9,'auth','0003_alter_user_email_max_length','2021-05-25 10:42:21.111999'),(10,'auth','0004_alter_user_username_opts','2021-05-25 10:42:21.125875'),(11,'auth','0005_alter_user_last_login_null','2021-05-25 10:42:21.217911'),(12,'auth','0006_require_contenttypes_0002','2021-05-25 10:42:21.227009'),(13,'auth','0007_alter_validators_add_error_messages','2021-05-25 10:42:21.272088'),(14,'auth','0008_alter_user_username_max_length','2021-05-25 10:42:21.365132'),(15,'auth','0009_alter_user_last_name_max_length','2021-05-25 10:42:21.465037'),(16,'auth','0010_alter_group_name_max_length','2021-05-25 10:42:21.501345'),(17,'auth','0011_update_proxy_permissions','2021-05-25 10:42:21.529767'),(18,'sessions','0001_initial','2021-05-25 10:42:21.579714'),(19,'api','0002_auto_20210526_0021','2021-05-25 16:21:08.630024'),(20,'api','0003_auto_20210526_0022','2021-05-25 16:22:05.114644');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-28 23:05:37

-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: solus_db
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `dataCadastro` datetime(6) NOT NULL,
  `status` varchar(10) NOT NULL,
  `cliente_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `accounts_customuser_cliente_id_897c9236_fk_clientes_` (`cliente_id`),
  CONSTRAINT `accounts_customuser_cliente_id_897c9236_fk_clientes_` FOREIGN KEY (`cliente_id`) REFERENCES `clientes_kronos_cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (9,'pbkdf2_sha256$390000$5eGwjpPwW8BCpNPo27wump$NpFU0JG8+yBtLPMhswGRm535N0p3K8DfkWIUUYcuWPs=','2023-11-24 20:18:01.000000',1,'administrador','','','victor@kronostecnologia.com.br',1,1,'2023-11-18 23:57:16.000000','Administrador','2023-11-18 23:57:16.788607','ativado',12),(10,'pbkdf2_sha256$390000$8EJjh9a60cNis1gUuOJhG4$t1NqKiyykoSnpqzHVB21bhybfrTK3lswSql1kSmfPnw=','2023-11-23 13:24:24.048239',0,'kronos','','','',0,1,'2023-11-19 17:16:37.000000','kronos tecnologia','2023-11-19 17:16:38.490372','ativado',10),(11,'pbkdf2_sha256$390000$bm1wnFBpGUgYAaoCk53Kyl$YXSwNz5NCcfUOsWbYXZScAsrqDUg0cWj2D51BpMYk0E=','2023-11-20 15:37:16.000000',0,'Thiago','','','',0,1,'2023-11-20 15:37:10.000000','Thiago Luglimi','2023-11-20 15:37:10.877349','ativado',10),(12,'pbkdf2_sha256$390000$Swn0lOd7hdG0jaVxjjB4Lx$LajuKXsK9fLkwpiwFqIgERF1rapFKW3J1aEziDnIczU=','2023-11-24 17:15:11.239669',0,'eneas','','','',0,1,'2023-11-23 20:04:45.000000','Eneas','2023-11-23 20:04:46.114620','ativado',10),(13,'pbkdf2_sha256$390000$cxXn3of84iXnMBhO8fC4CU$ooQz7xJMGulOpvicFgonZzaqHTSL1q01kqsc0WMkBnc=','2023-11-24 21:18:02.101253',0,'Carla','','','',0,1,'2023-11-24 17:23:24.000000','Carla','2023-11-24 17:23:24.987182','ativado',10);
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
INSERT INTO `accounts_customuser_groups` VALUES (3,10,1),(4,11,1),(5,12,1),(7,13,1);
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Contabilidade'),(2,'Visualizador');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,32),(2,1,33),(3,1,34),(4,1,36),(5,2,32);
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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add cliente',7,'add_cliente'),(26,'Can change cliente',7,'change_cliente'),(27,'Can delete cliente',7,'delete_cliente'),(28,'Can view cliente',7,'view_cliente'),(29,'Can add dashboard',8,'add_dashboard'),(30,'Can change dashboard',8,'change_dashboard'),(31,'Can delete dashboard',8,'delete_dashboard'),(32,'Can view dashboard',8,'view_dashboard'),(33,'Can add nota fiscal',9,'add_notafiscal'),(34,'Can change nota fiscal',9,'change_notafiscal'),(35,'Can delete nota fiscal',9,'delete_notafiscal'),(36,'Can view nota fiscal',9,'view_notafiscal');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes_kronos_cliente`
--

DROP TABLE IF EXISTS `clientes_kronos_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes_kronos_cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nome_empresa` varchar(100) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `cnpj` varchar(20) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes_kronos_cliente`
--

LOCK TABLES `clientes_kronos_cliente` WRITE;
/*!40000 ALTER TABLE `clientes_kronos_cliente` DISABLE KEYS */;
INSERT INTO `clientes_kronos_cliente` VALUES (10,'Cia Paulista','Rod.Augusto montenegro','88888888888','777777777777','static/logos_clientes/discord.png'),(11,'nmmm','jjjjj','987777777','99999999999999999',NULL),(12,'RODOVITOR TRANSPORTES','ESTRADA URIBOCA MARITUBA','9999','08408736000105','static/logos_clientes/08408736000105.png');
/*!40000 ALTER TABLE `clientes_kronos_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dashboards_dashboard`
--

DROP TABLE IF EXISTS `dashboards_dashboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboards_dashboard` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `area` varchar(50) NOT NULL,
  `link` varchar(200) NOT NULL,
  `data_cadastro` datetime(6) NOT NULL,
  `cliente_id` bigint NOT NULL,
  `usuario_cadastrou_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dashboards_dashboard_cliente_id_1f4ff4b7_fk_clientes_` (`cliente_id`),
  KEY `dashboards_dashboard_usuario_cadastrou_id_96aab855_fk_accounts_` (`usuario_cadastrou_id`),
  CONSTRAINT `dashboards_dashboard_cliente_id_1f4ff4b7_fk_clientes_` FOREIGN KEY (`cliente_id`) REFERENCES `clientes_kronos_cliente` (`id`),
  CONSTRAINT `dashboards_dashboard_usuario_cadastrou_id_96aab855_fk_accounts_` FOREIGN KEY (`usuario_cadastrou_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboards_dashboard`
--

LOCK TABLES `dashboards_dashboard` WRITE;
/*!40000 ALTER TABLE `dashboards_dashboard` DISABLE KEYS */;
INSERT INTO `dashboards_dashboard` VALUES (2,'Analise de Resultado','financeiro','https://app.powerbi.com/view?r=eyJrIjoiNDRhMDhkYzQtY2RhOC00OTUxLWEyODItOTM2MzFiZWE3ZThiIiwidCI6IjMxMjliOTg2LTg4YjYtNGJlMi1iNDMzLWNkNDk1MWE0OTJiNiJ9&embedImagePlaceholder=true&pageName=ReportSection490','2023-11-20 13:41:08.487829',10,10),(3,'Painel de Entregas','logistica','https://app.powerbi.com/view?r=eyJrIjoiMWI2ZTIzYmItOWRhMS00ODkxLTgyM2QtMjAyOTg5YzJhZTdhIiwidCI6Ijc3MzI3NTRlLWMwNjktNDU3Ni1iYjliLTk2ZDI4ZTViYTM4OSJ9','2023-11-20 14:52:48.299943',10,10),(4,'Relatorio 150','logistica','https://app.powerbi.com/view?r=eyJrIjoiMTVlNmVkYzYtMzhmMi00YzhkLWJlZTUtOTk5MjI1MDBjZTZlIiwidCI6Ijc3MzI3NTRlLWMwNjktNDU3Ni1iYjliLTk2ZDI4ZTViYTM4OSJ9','2023-11-20 14:54:09.838214',11,10),(5,'Teste','financeiro','https://app.powerbi.com/view?r=eyJrIjoiNDRhMDhkYzQtY2RhOC00OTUxLWEyODItOTM2MzFiZWE3ZThiIiwidCI6IjMxMjliOTg2LTg4YjYtNGJlMi1iNDMzLWNkNDk1MWE0OTJiNiJ9&embedImagePlaceholder=true&pageName=ReportSection490','2023-11-20 14:57:23.159166',10,10);
/*!40000 ALTER TABLE `dashboards_dashboard` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-11-18 23:58:48.821202','9','Rodovitor Transportes',3,'',7,9),(2,'2023-11-18 23:58:48.826902','8','Rodovitor Transportes',3,'',7,9),(3,'2023-11-18 23:58:48.831889','7','Rodovitor Transportes',3,'',7,9),(4,'2023-11-18 23:58:48.835843','6','Rodovitor Transportes',3,'',7,9),(5,'2023-11-18 23:58:48.840638','5','Rodovitor Transportes',3,'',7,9),(6,'2023-11-18 23:58:48.845033','4','Rodovitor Transportes',3,'',7,9),(7,'2023-11-18 23:58:48.848655','3','Rodovitor Transportes',3,'',7,9),(8,'2023-11-18 23:58:48.852653','2','Rodovitor Transportes',3,'',7,9),(9,'2023-11-18 23:58:48.857587','1','Rodovitor Transportes',3,'',7,9),(10,'2023-11-19 13:05:41.349241','1','NF 897 - BolinhaTech',1,'[{\"added\": {}}]',9,9),(11,'2023-11-19 13:26:10.844721','2','NotaFiscal object (2)',1,'[{\"added\": {}}]',9,9),(12,'2023-11-20 01:41:45.844899','1','Contabilidade',1,'[{\"added\": {}}]',3,9),(13,'2023-11-20 02:47:30.809141','10','kronos',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,9),(14,'2023-11-20 14:56:26.011576','2','Visualizador',1,'[{\"added\": {}}]',3,9),(15,'2023-11-20 14:56:47.760343','10','kronos',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,9),(16,'2023-11-20 15:34:45.317190','10','kronos',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,9),(17,'2023-11-20 15:38:51.808831','11','Thiago',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,9),(18,'2023-11-23 20:06:27.185897','12','eneas',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,9),(19,'2023-11-24 17:23:24.988163','13','Carla',1,'[{\"added\": {}}]',6,9),(20,'2023-11-24 17:24:16.902433','13','Carla',2,'[{\"changed\": {\"fields\": [\"Groups\", \"Nome\", \"Cliente\"]}}]',6,9),(21,'2023-11-24 17:25:39.851640','13','Carla',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',6,9),(22,'2023-11-24 20:19:21.286442','12','RODOVITOR TRANSPORTES',1,'[{\"added\": {}}]',7,9),(23,'2023-11-24 20:21:01.026247','10','Cia Paulista',2,'[{\"changed\": {\"fields\": [\"Logo\"]}}]',7,9),(24,'2023-11-24 20:25:54.917344','12','RODOVITOR TRANSPORTES',2,'[{\"changed\": {\"fields\": [\"Logo\"]}}]',7,9),(25,'2023-11-24 20:42:12.843772','9','administrador',2,'[{\"changed\": {\"fields\": [\"Cliente\"]}}]',6,9),(26,'2023-11-24 20:44:23.311754','12','RODOVITOR TRANSPORTES',2,'[{\"changed\": {\"fields\": [\"Cnpj\"]}}]',7,9);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'accounts','customuser'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(7,'clientes_kronos','cliente'),(4,'contenttypes','contenttype'),(8,'dashboards','dashboard'),(9,'protocolo_notas_fiscais','notafiscal'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-12 01:10:24.072923'),(2,'contenttypes','0002_remove_content_type_name','2023-11-12 01:10:24.096929'),(3,'auth','0001_initial','2023-11-12 01:10:24.194952'),(4,'auth','0002_alter_permission_name_max_length','2023-11-12 01:10:24.224957'),(5,'auth','0003_alter_user_email_max_length','2023-11-12 01:10:24.253964'),(6,'auth','0004_alter_user_username_opts','2023-11-12 01:10:24.257964'),(7,'auth','0005_alter_user_last_login_null','2023-11-12 01:10:24.261966'),(8,'auth','0006_require_contenttypes_0002','2023-11-12 01:10:24.264966'),(9,'auth','0007_alter_validators_add_error_messages','2023-11-12 01:10:24.269967'),(10,'auth','0008_alter_user_username_max_length','2023-11-12 01:10:24.273968'),(11,'auth','0009_alter_user_last_name_max_length','2023-11-12 01:10:24.278969'),(12,'auth','0010_alter_group_name_max_length','2023-11-12 01:10:24.289972'),(13,'auth','0011_update_proxy_permissions','2023-11-12 01:10:24.294974'),(14,'auth','0012_alter_user_first_name_max_length','2023-11-12 01:10:24.299974'),(15,'accounts','0001_initial','2023-11-12 01:10:24.402871'),(16,'admin','0001_initial','2023-11-12 01:10:24.457125'),(17,'admin','0002_logentry_remove_auto_add','2023-11-12 01:10:24.464617'),(18,'admin','0003_logentry_add_action_flag_choices','2023-11-12 01:10:24.469214'),(19,'sessions','0001_initial','2023-11-12 01:10:24.487974'),(20,'clientes_kronos','0001_initial','2023-11-15 17:14:13.462477'),(21,'dashboards','0001_initial','2023-11-17 21:07:03.300131'),(22,'accounts','0002_customuser_cliente','2023-11-18 23:04:20.389133'),(23,'accounts','0003_alter_customuser_cliente','2023-11-18 23:55:35.790148'),(24,'protocolo_notas_fiscais','0001_initial','2023-11-19 12:59:55.712841'),(25,'protocolo_notas_fiscais','0002_notafiscal_status_ssw_and_more','2023-11-20 01:37:03.601415'),(26,'protocolo_notas_fiscais','0003_notafiscal_data_ultima_alteracao','2023-11-20 03:04:19.979743'),(27,'protocolo_notas_fiscais','0004_alter_notafiscal_data_ultima_alteracao','2023-11-20 03:36:53.230970'),(28,'protocolo_notas_fiscais','0005_notafiscal_data_status_ssw','2023-11-20 17:29:03.656824'),(29,'clientes_kronos','0002_cliente_logo','2023-11-24 20:13:16.192879'),(30,'protocolo_notas_fiscais','0006_alter_notafiscal_arquivo_nf','2023-11-24 20:13:16.203848'),(31,'clientes_kronos','0003_alter_cliente_logo','2023-11-24 20:25:23.782486');
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
INSERT INTO `django_session` VALUES ('2qreprncgfdalu0himt70vjiwm3jk2y9','.eJxVjEEOwiAQRe_C2pDKQGFcuu8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnERKE6_W6D4SHUHfKd6azK2ui5zkLsiD9rl1Dg9r4f7d1Col29tmbOGPCQNQQ3RgbGZg1XKsnF5RMwMoC0aR6MDFxWflUVNEZEjGBLvD-QGN58:1r6BDS:t603YHZFdSw1E97SN2GEKQdYZjJlcofC_kVobuDWgO0','2023-12-07 15:02:06.666051'),('30nfxp7pt612st0c8723obqibbf26m0b','e30:1r3gpW:7HiJJYu3K5QHPuw2GaSii0slTTxoX9nbLTiWYcsnRvk','2023-11-30 18:11:06.055423'),('3qz204zwzgww4f54suv4b54ulk4jaw6k','e30:1r1z5m:-MqhiIg-bjx8aL5N4jxcytG7hGK6C_PGoHzQyI83wTA','2023-11-26 01:16:50.108720'),('7tp0j9v9y9zw9k08og0ccotqjd0kpsao','e30:1r44EZ:uBe7r76it_ezfum2MB38ZO_6doz_BrNN6d_P6KFTqko','2023-12-01 19:10:31.217172'),('8f2ddikkgimd3ojtuishtg3lq2a4dmwp','e30:1r448h:BIxx9WpVDvPE7Y1MYVOtIrvjHIk54klz-VWRivaFb_g','2023-12-01 19:04:27.686701'),('9dexa9q9d6rbxkwng7iqk0poxjouepcx','.eJxVjDsOwjAQBe_iGln-xD9Kes5g7dprHEC2FCcV4u4QKQW0b2bei0XY1hq3QUucMzszyU6_G0J6UNtBvkO7dZ56W5cZ-a7wgw5-7Zmel8P9O6gw6rdWJgAgCemI0LmUwmRMMDLIVGyw3jqhAxiFTlsqToMHobJACcVPEjN7fwDZSzep:1r3ITc:P1ebXetLi5P2PruPF7Gn8K4iVAvt0DcrImQsh5cGLOg','2023-11-29 16:10:52.577199'),('arn8cqbzwej39c1guy6mywf3sae64n7l','.eJxVjMsOwiAQRf-FtSFAebp07zeQgWGkaiAp7cr479qkC93ec859sQjbWuM2yhJnZGcmBTv9jgnyo7Sd4B3arfPc27rMie8KP-jg147leTncv4MKo35rows6S6BIaid8LkqpKQTwwZFOJmmfLAonM2ZLQoIKEyF5ix7JgFXs_QEDxDhG:1r5snc:JVwvKOm4vSJPJno8EIrZJj9ak2Vp3nfrqJ4dze6M7ns','2023-12-06 19:22:12.142128'),('aydlrcutky67pn5s6phtp6627bzcf0an','.eJxVjMsOwiAQRf-FtSECLQ-X7vsNZIYZpGogKe3K-O_apAvd3nPOfYkI21ri1nmJM4mLUFqcfkeE9OC6E7pDvTWZWl2XGeWuyIN2OTXi5_Vw_w4K9PKtrUlGGVLIqIN1iTIZT2c7KLbgsh8RNdoM6MPALqmQBjRo2QGoYEYv3h8bPDia:1r6Fwt:hAVqqk8MG7NZk0SISIu170bizrQL1ozYN942sCexU08','2023-12-07 20:05:19.083504'),('b64m8sl3dm4br16ed9a8v0sbs24gd819','e30:1r3goR:R0T_BqdxqpWl7ABh82FkqnP78V3DYOGNbWnlXr7TyIo','2023-11-30 18:09:59.619883'),('bxgvapbrfhw8bflotjgqs215m2spdi0h','e30:1r3go1:0XiT8ACD6iwrZm7bvhPYdsYIQJ0D5v0w8sTdn9nRjAo','2023-11-30 18:09:33.079121'),('j73l42lflw1hr3aycae6epaxuhy3eg3l','.eJxVjMsOwiAQRf-FtSE8hkdduvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZSc1Ov2NEeuS2k3THduuceluXOfJd4Qcd_NpTfl4O9--g4qjfGoyLTgsURlEBiwm8dhgtAUlSziZDUU1Ky5INgHdIjrIw1pvi9aSQvT_4YDem:1r6dYo:kdSz2AN_w3pk59EX913YB-J32ZR2pIB5sd7e4K9Uiow','2023-12-08 21:18:02.103255'),('jant7d33oemt9lgo7bzbyxqkq0cbiakh','.eJxVjDsOwjAQBe_iGln-xD9Kes5g7dprHEC2FCcV4u4QKQW0b2bei0XY1hq3QUucMzszyU6_G0J6UNtBvkO7dZ56W5cZ-a7wgw5-7Zmel8P9O6gw6rdWJgAgCemI0LmUwmRMMDLIVGyw3jqhAxiFTlsqToMHobJACcVPEjN7fwDZSzep:1r2j09:uggAJEU-BOESFqQl0cdZ-HxmQ4WKRnedjksoAdcUCGk','2023-11-28 02:18:05.761715'),('jfiu2rsxppq8qzgskhjzoolffcse8jzy','e30:1r44N2:odr2FxgwyHb-iTLznSWQ2xPxfMrYipYgFQ9oIq4H4AM','2023-12-01 19:19:16.434986'),('jhe0g5drckhop84tovevbsvx2ekofidf','e30:1r44ML:xlXcKTVOqQELsXnq-iBBV71Ku9HCC9ls1vmUlDZgjbg','2023-12-01 19:18:33.685342'),('jrryfz8b1iz6fa4qskyr28cdzh3lxkt5','e30:1r44Mg:2CmjiW9TQxahf4EBC7YZUjVsfswAhYBrkgDSZaewc5A','2023-12-01 19:18:54.528665'),('nu4v0373p057kym32e6149dhdjfieigr','e30:1r44GM:c-u7rTfXcoLhXe26o9h1jMkuWk0K-Xdoxm1YhG_Agio','2023-12-01 19:12:22.523632'),('tdf950g28ia3rptkuk1ocy4tdg68p37o','.eJxVjMsOwiAQRf-FtSFAebp07zeQgWGkaiAp7cr479qkC93ec859sQjbWuM2yhJnZGcmBTv9jgnyo7Sd4B3arfPc27rMie8KP-jg147leTncv4MKo35rows6S6BIaid8LkqpKQTwwZFOJmmfLAonM2ZLQoIKEyF5ix7JgFXs_QEDxDhG:1r57q0:ChFFX2qH0g6SAocWqHtT8F5-mZZQfPobQT-ocWZ6z4I','2023-12-04 17:13:32.749462'),('tzfebjydx60gkllayb0b7j7f7ck4cr1l','.eJxVjMsOwiAUBf-FtSE8ioBL934DOReuUjU0Ke3K-O_apAvdnpk5L5GwLjWtnec0FnESVhx-N0J-cNtAuaPdJpmntswjyU2RO-3yMhV-nnf376Ci129tglHauWCVOl5pKDZ4rzIHUHEOTrGPAVq7SLDeeCKGwaBZwUYDhnh_ALw7N4g:1r20Qi:PhkM61lzTfHyfjDDpQ5LFvOYnjRPHdV4vLkvX_39ckI','2023-11-26 02:42:32.085666'),('w3kcgxlb2l4s0uwwhuasv5ckf9fmr7br','.eJxVjEEOwiAQRe_C2pDKQGFcuu8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnERKE6_W6D4SHUHfKd6azK2ui5zkLsiD9rl1Dg9r4f7d1Col29tmbOGPCQNQQ3RgbGZg1XKsnF5RMwMoC0aR6MDFxWflUVNEZEjGBLvD-QGN58:1r6Fvs:2IzAvpKT5tWhkoDG7fVgsIS8ikvo-N9mER9YHGeuE9w','2023-12-07 20:04:16.013134'),('wvt0qx51ufp2jgttxuzkn4c9hfkies38','.eJxVjEEOwiAQRe_C2hBwgIJL956BDMwgVUOT0q6MdzckXej2v_f-W0Tctxr3zmucSVyEVuL0OybMT26D0APbfZF5ads6JzkUedAubwvx63q4fwcVex21TiV4sj44AkBip1mFkBWVUDAbCnoqDoBtssZYryegM7vExrAG5cTnCxl3OBg:1r4uO4:eOyptwqZKh9oPNRP5XGCqLE3x85WT10RFCe55CzgGoI','2023-12-04 02:51:48.096192'),('y5dvfbt7pzysddkr1z4l9hni5a56bqg1','.eJxVjEEOwiAQRe_C2pDKQGFcuu8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnERKE6_W6D4SHUHfKd6azK2ui5zkLsiD9rl1Dg9r4f7d1Col29tmbOGPCQNQQ3RgbGZg1XKsnF5RMwMoC0aR6MDFxWflUVNEZEjGBLvD-QGN58:1r6Xoo:-uS_eOBav5FVUjFpOBWdNr8WaaN4rzMWdwl0NEHauIA','2023-12-08 15:10:10.373797');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `protocolo_notas_fiscais_notafiscal`
--

DROP TABLE IF EXISTS `protocolo_notas_fiscais_notafiscal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `protocolo_notas_fiscais_notafiscal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nome_fornecedor` varchar(100) NOT NULL,
  `cnpj_fornecedor` varchar(18) NOT NULL,
  `numero_nf` varchar(20) NOT NULL,
  `data_cadastro` datetime(6) NOT NULL,
  `data_emissao_nf` date NOT NULL,
  `descricao` longtext NOT NULL,
  `arquivo_nf` varchar(100) NOT NULL,
  `cliente_associado_id` bigint NOT NULL,
  `usuario_cadastrou_id` bigint NOT NULL,
  `status_ssw` varchar(3) NOT NULL,
  `usuario_que_mudou_o_status_id` bigint DEFAULT NULL,
  `data_ultima_alteracao` datetime(6) DEFAULT NULL,
  `data_status_ssw` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `protocolo_notas_fisc_cliente_associado_id_297b01df_fk_clientes_` (`cliente_associado_id`),
  KEY `protocolo_notas_fisc_usuario_cadastrou_id_48786a24_fk_accounts_` (`usuario_cadastrou_id`),
  KEY `protocolo_notas_fisc_usuario_que_mudou_o__40b9dfe5_fk_accounts_` (`usuario_que_mudou_o_status_id`),
  CONSTRAINT `protocolo_notas_fisc_cliente_associado_id_297b01df_fk_clientes_` FOREIGN KEY (`cliente_associado_id`) REFERENCES `clientes_kronos_cliente` (`id`),
  CONSTRAINT `protocolo_notas_fisc_usuario_cadastrou_id_48786a24_fk_accounts_` FOREIGN KEY (`usuario_cadastrou_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `protocolo_notas_fisc_usuario_que_mudou_o__40b9dfe5_fk_accounts_` FOREIGN KEY (`usuario_que_mudou_o_status_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `protocolo_notas_fiscais_notafiscal`
--

LOCK TABLES `protocolo_notas_fiscais_notafiscal` WRITE;
/*!40000 ALTER TABLE `protocolo_notas_fiscais_notafiscal` DISABLE KEYS */;
INSERT INTO `protocolo_notas_fiscais_notafiscal` VALUES (1,'Logisticax','01326631209','59','2023-11-24 17:16:51.039686','2023-11-20','Compra realizada no cartão.','notas_fiscais/59_01326631209.pdf',10,12,'sim',12,'2023-11-24 17:17:41.247549','2023-11-24 17:18:27.478172'),(2,'thiagoLog','00001111222','542','2023-11-24 17:20:24.388915','2023-11-30','aaaaa','notas_fiscais/542_00001111222.pdf',10,12,'nao',13,NULL,'2023-11-24 21:18:09.307276');
/*!40000 ALTER TABLE `protocolo_notas_fiscais_notafiscal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-24 19:28:18

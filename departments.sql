use account;

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '編號',
  `name` varchar(50) DEFAULT NULL COMMENT '部門名稱',
  `manager` varchar(30) DEFAULT NULL COMMENT '主管姓名',
  `note` varchar(500) DEFAULT NULL COMMENT '備註',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


ALTER TABLE account.remittances ADD note varchar(500) NULL;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for FILE
-- ----------------------------
DROP TABLE IF EXISTS `FILE`;
CREATE TABLE `FILE`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `FILENAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `HASHNAME` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `TIME` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of FILE
-- ----------------------------
INSERT INTO `FILE` VALUES (1, 'fanqieLogo.png', 'fanqieLogo.png', '2024-01-01 12:00:00');

-- ----------------------------
-- Table structure for LOGIN_LOG
-- ----------------------------
DROP TABLE IF EXISTS `LOGIN_LOG`;
CREATE TABLE `LOGIN_LOG`  (
  `ID` int(4) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `TIME` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `LOGINIP` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of LOGIN_LOG
-- ----------------------------
INSERT INTO `LOGIN_LOG` VALUES (1, 'admin', '2024-01-01 12:00:00', '127.0.0.1');

-- ----------------------------
-- Table structure for USER
-- ----------------------------
DROP TABLE IF EXISTS `USER`;
CREATE TABLE `USER`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PASSWORD` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `PHONE` varchar(11) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `QQ` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `PID` int(11) NULL DEFAULT NULL,
  `UID` int(1) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of USER
-- ----------------------------
INSERT INTO `USER` VALUES (1, 'admin', '21232f297a57a5a743894a0e4a801fc3', '110', '00001', 202401, 1);
INSERT INTO `USER` VALUES (2, 'pilot', 'e10adc3949ba59abbe56e057f20f883e', '10086', '00001', 202402, 0);
INSERT INTO `USER` VALUES (3, 'fanqie', '0f359740bd1cda994f8b55330c86d845', '10010', '00001', 202403, 0);

-- ----------------------------
-- Table structure for VIRTUAL_USERINFO
-- ----------------------------
DROP TABLE IF EXISTS `VIRTUAL_USERINFO`;
CREATE TABLE `VIRTUAL_USERINFO`  (
  `ID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `NAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `BIRTH` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PHONE` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `IDCARD` varchar(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ADDRESS` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `CREDIT` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of VIRTUAL_USERINFO
-- ----------------------------
INSERT INTO `VIRTUAL_USERINFO` VALUES (1, '李开', '19890920', '18197586673', '360983198909201903', '高安市', '5240707260321504');
INSERT INTO `VIRTUAL_USERINFO` VALUES (2, '范况', '20080805', '17655459195', '513423200808054577', '盐源县', '6229168018533728');
INSERT INTO `VIRTUAL_USERINFO` VALUES (3, '许况劫', '19860218', '14911194450', '530723198602189553', '华坪县', '6228373418968727');
INSERT INTO `VIRTUAL_USERINFO` VALUES (4, '方严骨', '20130612', '18901200104', '510500201306122093', '泸州', '6226008897259120');
INSERT INTO `VIRTUAL_USERINFO` VALUES (5, '赵凡', '19830808', '18058807565', '441302198308081942', '惠城区', '4380888790351368');
INSERT INTO `VIRTUAL_USERINFO` VALUES (6, '朱一', '20100302', '16658529261', '510683201003020598', '绵竹市', '4041216641641024');
INSERT INTO `VIRTUAL_USERINFO` VALUES (7, '李五', '20020319', '13358337842', '533103200203199994', '芒市', '4047384193293066');
INSERT INTO `VIRTUAL_USERINFO` VALUES (8, '邹杜', '19860628', '18136622516', '22012219860628381X', '农安县', '5218994544487616');
INSERT INTO `VIRTUAL_USERINFO` VALUES (9, '方万', '20160413', '13585354609', '140429201604136678', '武乡县', '4033612575501360');
INSERT INTO `VIRTUAL_USERINFO` VALUES (10, '王响', '19871016', '17565224976', '23060319871016233X', '龙凤区', '5201529011937257');

SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------
-- Table structure for USER
-- ----------------------------
DROP TABLE IF EXISTS "pilot"."USER";
CREATE SCHEMA IF NOT EXISTS "pilot";
CREATE TABLE "pilot"."USER" (
  "ID" int4 NOT NULL,
  "USERNAME" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "PASSWORD" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "PHONE" varchar(11) COLLATE "pg_catalog"."default" NOT NULL,
  "QQ" varchar(255) COLLATE "pg_catalog"."default",
  "PID" int4,
  "UID" int4
)
;

-- ----------------------------
-- Records of USER
-- ----------------------------
INSERT INTO "pilot"."USER" VALUES (1, 'admin', '21232f297a57a5a743894a0e4a801fc3', '13888888888', '00001', 202401, 1);
INSERT INTO "pilot"."USER" VALUES (2, 'pilot', 'e10adc3949ba59abbe56e057f20f883e', '18888888888', '00001', 202402, 0);
INSERT INTO "pilot"."USER" VALUES (3, 'fanqie', '0f359740bd1cda994f8b55330c86d845', '17666666666', '00002', 202404, 0);

-- ----------------------------
-- Primary Key structure for table USER
-- ----------------------------
ALTER TABLE "pilot"."USER" ADD CONSTRAINT "USER_pkey" PRIMARY KEY ("ID");

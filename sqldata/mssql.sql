-- ----------------------------
-- Table structure for USER
-- ----------------------------
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'pilot')
BEGIN
    CREATE DATABASE pilot;
END
GO

USE pilot;
GO

IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[USER]') AND type IN ('U'))
    DROP TABLE [dbo].[USER];
GO

CREATE TABLE [dbo].[USER] (
    [ID] int NOT NULL,
    [USERNAME] varchar(255) COLLATE Chinese_PRC_CI_AS NOT NULL,
    [PASSWORD] varchar(255) COLLATE Chinese_PRC_CI_AS NOT NULL,
    [PHONE] varchar(11) COLLATE Chinese_PRC_CI_AS NOT NULL,
    [QQ] varchar(255) COLLATE Chinese_PRC_CI_AS NULL,
    [PID] int NULL,
    [UID] int NULL
);
GO

ALTER TABLE [dbo].[USER] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of USER
-- ----------------------------
INSERT INTO [dbo].[USER] ([ID], [USERNAME], [PASSWORD], [PHONE], [QQ], [PID], [UID]) VALUES (N'1', N'admin', N'21232f297a57a5a743894a0e4a801fc3', N'13888888888', N'00001', N'202401', N'1')
GO

INSERT INTO [dbo].[USER] ([ID], [USERNAME], [PASSWORD], [PHONE], [QQ], [PID], [UID]) VALUES (N'2', N'pilot', N'e10adc3949ba59abbe56e057f20f883e', N'18888888888', N'00001', N'202402', N'0')
GO

INSERT INTO [dbo].[USER] ([ID], [USERNAME], [PASSWORD], [PHONE], [QQ], [PID], [UID]) VALUES (N'3', N'fanqie', N'0f359740bd1cda994f8b55330c86d845', N'17666666666', N'00002', N'202403', N'1')
GO


-- ----------------------------
-- Primary Key structure for table USER
-- ----------------------------
ALTER TABLE [dbo].[USER] ADD CONSTRAINT [PK__USER__3214EC273C8F1CA2] PRIMARY KEY CLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


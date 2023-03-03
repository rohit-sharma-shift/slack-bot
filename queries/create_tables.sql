USE [Bot]
GO

/****** Object:  Table [dbo].[force_ui_engineering_meet_schedule]    Script Date: 2023-03-03 16:56:59 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[force_ui_engineering_meet_schedule](
	[date] [date] NOT NULL,
	[squad] [nvarchar](50) NOT NULL,
	[contact] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO


USE [Bot]
GO

/****** Object:  Table [dbo].[force_ui_support_member_list]    Script Date: 2023-03-03 16:57:11 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[force_ui_support_member_list](
	[id] [int] NOT NULL,
	[email] [nvarchar](max) NOT NULL,
	[squad] [nvarchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


USE [Bot]
GO

/****** Object:  Table [dbo].[force_ui_support_schedule]    Script Date: 2023-03-03 16:57:21 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[force_ui_support_schedule](
	[From] [date] NULL,
	[To] [date] NULL,
	[Platform] [varchar](max) NULL,
	[HnL] [varchar](max) NULL,
	[PnC] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO



USE [Bot]
GO

INSERT INTO [dbo].[force_ui_engineering_meet_schedule]
           ([date]
           ,[squad]
           ,[contact])
     VALUES
		('2022-10-29','hnl','rohit.sharma@shift-technology.com'),
		('2022-11-11','platform','rohit.sharma@shift-technology.com'),
		('2022-11-18','pnc','rohit.sharma@shift-technology.com'),
		('2022-11-25','hnl','rohit.sharma@shift-technology.com'),
		('2022-12-02','platform','rohit.sharma@shift-technology.com'),
		('2022-12-09','pnc','rohit.sharma@shift-technology.com')
GO

INSERT INTO [dbo].[force_ui_support_member_list]
           ([id]
           ,[email]
           ,[squad])
     VALUES
		(1,'vahid.jahanbakhsh@shift-technology.com','pnc'),
		(2,'leslie.bonaposta@shift-technology.com','pnc'),
		(3,'nicolas.benning@shift-technology.com','hnl'),
		(4,'brice.hernandez@shift-technology.com','hnl'),
		(5,'ihor.saievych@shift-technology.com','hnl'),
		(6,'ekaterina.nekrasova@shift-technology.com','hnl')
GO

INSERT INTO [dbo].[force_ui_support_schedule]
           ([From]
           ,[To]
           ,[Platform]
           ,[HnL]
           ,[PnC])
     VALUES
		('2022-10-20','2022-10-26','rohit.sharma@shift-technology.com','rohit.sharma@shift-technology.com','rohit.sharma@shift-technology.com')
GO



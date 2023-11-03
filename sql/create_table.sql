--------------------------------------------------------
--  DDL for Table FASHION
--------------------------------------------------------

  CREATE TABLE "DB"."FASHION" 
   (	"PRODUCTID" NUMBER(38,0) CONSTRAINT PKEY2 PRIMARY KEY,
	"GENDER" VARCHAR2(26 BYTE), 
	"CATEGORY" VARCHAR2(26 BYTE), 
	"SUBCATEGORY" VARCHAR2(26 BYTE), 
	"PRODUCTTYPE" VARCHAR2(26 BYTE), 
	"COLOUR" VARCHAR2(26 BYTE), 
	"USAGE" VARCHAR2(26 BYTE), 
	"PRODUCTTITLE" VARCHAR2(128 BYTE), 
	"IMAGE" VARCHAR2(26 BYTE) NOT NULL, 
	"IMAGEURL" VARCHAR2(256 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
--------------------------------------------------------
--  Constraints for Table FASHION
--------------------------------------------------------

  ALTER TABLE "DB"."FASHION" MODIFY ("PRODUCTID" NOT NULL ENABLE);
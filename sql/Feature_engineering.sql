-- Count total data = 2906
SELECT count(*) from FASHION;



-------------------------------------------------------------------------------
---------------------DUPLICATION CHECK 중복검사---------------------------------
-- PRODUCTID 고유값 기준 중복 데이터 검사 (결과: 중복 없음)
-- duplicate data check based on PRODUCTID(unique data) -> no duplicate result!
SELECT PRODUCTID, count(*) FROM FASHION
GROUP BY PRODUCTID
HAVING count(*) > 1;   

-- IMAGE 고유값 기준 중복 데이터 검사 (결과: 중복 없음)
-- duplicate data check based on IMAGE(unique data) -> no duplicate result!
SELECT IMAGE, count(*) FROM FASHION
GROUP BY IMAGE
HAVING count(*) > 1;  

-- IMAGEURL 고유값 기준 중복 데이터 검사 (결과: 중복 없음)
-- duplicate data check based on IMAGEURL(unique data) -> no duplicate result!
SELECT IMAGEURL, count(*) FROM FASHION
GROUP BY IMAGEURL
HAVING count(*) > 1;  



-------------------------------------------------------------------------------
--------------------------GENDER simplification---------------------------------
-- Check unique keywords before binary labeling (Women:769, Girls:567, Men:811, Boys:759)
select GENDER, count(*) from FASHION
group by GENDER;


-- Update Gender_simplified(simple binary:: 0 = Female, 1 = Male)
ALTER TABLE FASHION ADD (Gender_simplified NUMBER);
UPDATE FASHION SET Gender_simplified = case when GENDER = 'Girls' or GENDER = 'Women'  Then 0
when GENDER = 'Boys' or GENDER = 'Men' then 1
end;


-- Update Female_simplified(Female binary:: 0 = Girls, 1 = Women, else = null)
ALTER TABLE FASHION ADD (Female_simplified NUMBER);
UPDATE FASHION SET Female_simplified = case when GENDER = 'Girls' Then 0
when GENDER = 'Women' then 1
else null
end;


-- Update Male_simplified(male binary:: 0 = Boys, 1 = Men, else = null)
ALTER TABLE FASHION ADD (Male_simplified NUMBER);
UPDATE FASHION SET Male_simplified = case when GENDER = 'Boys' Then 0
when GENDER = 'Men' then 1
else null
end;



-------------------------------------------------------------------------------
--------------------------CATEGORY simplification------------------------------
-- Check unique keywords before binary labeling (Footwear:1580, Apparel:1326)
select CATEGORY, count(*) from FASHION
group by CATEGORY;

-- Update Category_simplified(Category binary:: 0 = Footwear, 1 = Apparel, else = null)
ALTER TABLE FASHION ADD (Category_simplified NUMBER);
UPDATE FASHION SET Category_simplified = case when CATEGORY = 'Footwear' Then 0
when CATEGORY = 'Apparel' then 1
else null
end;



-------------------------------------------------------------------------------
---------------------other columns simplifing trials---------------------------
-- Check unique keywords before binary labeling -> 9kinds -> no labeling here
-- subcategory is not well balanced
select SUBCATEGORY, count(*) from FASHION
group by SUBCATEGORY;

-- Check unique keywords before binary labeling -> 31kinds -> no labeling here
-- product type is not well balanced
select PRODUCTTYPE, count(*) from FASHION
group by PRODUCTTYPE;

-- Check unique keywords before binary labeling -> 39kinds -> no labeling here
-- mostly Black and then White
select COLOUR, count(*) from FASHION
group by COLOUR;

-- Check unique keywords before binary labeling -> 6kinds -> no labeling here
-- overally, Casual(2457), Sports(357) and the rest is small out of 2906(unbalnced)
select USAGE, count(*) from FASHION
group by USAGE;

-- Check unique keywords before binary labeling -> 2174kinds -> no labeling here
select producttitle, count(*) from FASHION
group by producttitle
ORDER BY count(*) DESC;



-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- Delete unnecessary column and commit
ALTER TABLE FASHION DROP (GENDER);
ALTER TABLE FASHION DROP (CATEGORY);



commit;
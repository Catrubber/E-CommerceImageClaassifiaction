#!/usr/bin/env python
# coding: utf-8

# # Run this file after sql query (SQL 실행 후 실행합니다.)
# ## Data load from SQL query and do EDA and then export the file from pandas
# ## SQL작업 데이터 호출, EDA 후 저장하는 내용입니다.

# install package if necessary 패키지 설치
get_ipython().system('pip install cx_Oracle')

import pandas as pd
import cx_Oracle as oci  # data import. it is told that python 3.4 is preferable.

# Go to C:\oraclexe\app\oracle\product\11.2.0\server\network\ADMIN. Then check 'port (1521)' and 'service name(xe)' in 'tnsname.ora'
# use your own information on user and pw.  (user와 pw변수는 각자 맞는 정보로 고쳐서 실행)
user = "DB"
pw = "1234"
dsn = "localhost:1521/xe" 

# connection 연결
con = oci.connect(user=user, password=pw, dsn=dsn)

# cursor 커서
cur = con.cursor()

query = 'select * from FASHION'
df = pd.read_sql_query(query, con)

# change the column sequence for convinence purpose. 편의상 컬럼 순서 정렬
df = df[['PRODUCTID','GENDER_SIMPLIFIED', 'FEMALE_SIMPLIFIED','MALE_SIMPLIFIED','CATEGORY_SIMPLIFIED','SUBCATEGORY','PRODUCTTYPE','COLOUR','USAGE','PRODUCTTITLE','IMAGE','IMAGEURL']]

# U.S standard name fix from U.K.  영국이 아닌 미국기준 철자로 변경
df.rename(columns = {'COLOUR':'COLOR'},inplace=True)

df.describe(include='all').T  # statistics for all data. 문자열 정보를 포함한 경우까지 조회

# Save all process so far without index
# SQL 작업 + 지금까지의 분석 데이터 저장 (index 생성 방지 옵션 설정)
df.to_csv('../data/Fashion_SQL.csv', index=False) 
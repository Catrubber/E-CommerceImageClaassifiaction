import os
import shutil
import glob

# 원래 디렉터리 구조

# images
#     Apparel
#         Men
#         Women
#     Footwear
#         Mem
#         Women


# 3개의 각 모델을 파이토치로 불러오기 위해 디렉터리를 개별로 생성
os.mkdir("../img_GENDER")
os.mkdir("../img_GENDER/Men")
os.mkdir("../img_GENDER/Women")

os.mkdir("../img_CATEGORY")
os.mkdir("../img_CATEGORY/Apparel")
os.mkdir("../img_CATEGORY/Footwear")

os.mkdir("../img_COLOR")
##################


# img_GENDER 파일에 Men과 Women을 기준으로 모든 데이터를 넣음
for file in glob.glob('../images/Apparel/Men/*.jpg'):
    print(file)
    shutil.copy(file, "../img_GENDER/Men")
    
for file in glob.glob('../images/Footwear/Men/*.jpg'):
    print(file)
    shutil.copy(file, "../img_GENDER/Men")
    
for file in glob.glob('../images/Apparel/Women/*.jpg'):
    print(file)
    shutil.copy(file, "../img_GENDER/Women")
    
for file in glob.glob('../images/Footwear/Women/*.jpg'):
    print(file)
    shutil.copy(file, "../img_GENDER/Women")


# img_CATEGORY 파일에 Apparel과 Footwear을 기준으로 모든 데이터를 넣음
for file in glob.glob('../images/Apparel/Men/*.jpg'):
    print(file)
    shutil.copy(file, "../img_CATEGORY/Apparel")
    
for file in glob.glob('../images/Apparel/Women/*.jpg'):
    print(file)
    shutil.copy(file, "../img_CATEGORY/Apparel")

for file in glob.glob('../images/Footwear/Men/*.jpg'):
    print(file)
    shutil.copy(file, "../img_CATEGORY/Footwear")
    
for file in glob.glob('../images/Footwear/Women/*.jpg'):
    print(file)
    shutil.copy(file, "../img_CATEGORY/Footwear")


print("Succeeded")
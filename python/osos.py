import os
import shutil

# 파이토치가 Men, Women 레이블로 인식할 수 있도록 디렉터리 이름을 변경
os.rename("../images/Apparel/Boys/Images/images_with_product_ids", "../images/Apparel/Boys/Images/Men")
os.rename("../images/Apparel/Girls/Images/images_with_product_ids", "../images/Apparel/Girls/Images/Women")
src1 = '../images/Apparel/Boys/Images/Men'
src2 = '../images/Apparel/Girls/Images/Women'
dst1 = "../images/Apparel"
dst2 = "../images/Apparel"

# 디렉터리 이동
shutil.move(src1, dst1)
shutil.move(src2, dst2)

# 기존 디렉터리 삭제
os.rmdir("../images/Apparel/Boys/Images")
os.rmdir("../images/Apparel/Boys")
os.rmdir("../images/Apparel/Girls/Images")
os.rmdir("../images/Apparel/Girls")


print("(Apparel) Move Completed\n")


# 임시 폴더 생성
os.mkdir("../images/Footwear_temp")

# 파이토치가 Men, Women 레이블로 인식할 수 있도록 디렉터리 이름을 변경
os.rename("../images/Footwear/Men/Images/images_with_product_ids", "../images/Footwear/Men/Images/Men")
os.rename("../images/Footwear/Women/Images/images_with_product_ids", "../images/Footwear/Women/Images/Women")
src1 = '../images/Footwear/Men/Images/Men'
src2 = '../images/Footwear/Women/Images/Women'
dst1 = "../images/Footwear_temp"
dst2 = "../images/Footwear_temp"
 
 # 디렉터리 이동
shutil.move(src1, dst1)
shutil.move(src2, dst2)

# 기존 디렉터리 삭제 (속에 있는 폴더부터 순차적으로 삭제)
os.rmdir("../images/Footwear/Men/Images")
os.rmdir("../images/Footwear/Men")
os.rmdir("../images/Footwear/Women/Images")
os.rmdir("../images/Footwear/Women")
os.rmdir("../images/Footwear")

# 임시 폴더를 공식 폴더명으로 변경
os.rename("../images/Footwear_temp", "../images/Footwear")

print("(Footwear) Move Completed\n")

# 최종 디렉터리 구조

# images
#     Apparel
#         Men
#         Women
#     Footwear
#         Mem
#         Women
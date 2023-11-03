import os
import shutil

# try:
#     os.mkdir("../images/Apparel/Men")
#     os.mkdir("../images/Apparel/Women")
# except FileExistsError:
#     pass

os.rename("../images/Apparel/Boys/Images/images_with_product_ids", "../images/Apparel/Boys/Images/Men")
os.rename("../images/Apparel/Girls/Images/images_with_product_ids", "../images/Apparel/Girls/Images/Women")
src1 = '../images/Apparel/Boys/Images/Men'
src2 = '../images/Apparel/Girls/Images/Women'
dst1 = "../images/Apparel"
dst2 = "../images/Apparel"
 
shutil.move(src1, dst1)
shutil.move(src2, dst2)

os.rmdir("../images/Apparel/Boys/Images")
os.rmdir("../images/Apparel/Boys")
os.rmdir("../images/Apparel/Girls/Images")
os.rmdir("../images/Apparel/Girls")

print("(Apparel) Move Completed\n")

os.mkdir("../images/Footwear_temp")

os.rename("../images/Footwear/Men/Images/images_with_product_ids", "../images/Footwear/Men/Images/Men")
os.rename("../images/Footwear/Women/Images/images_with_product_ids", "../images/Footwear/Women/Images/Women")
src1 = '../images/Footwear/Men/Images/Men'
src2 = '../images/Footwear/Women/Images/Women'
dst1 = "../images/Footwear_temp"
dst2 = "../images/Footwear_temp"
 
shutil.move(src1, dst1)
shutil.move(src2, dst2)

os.rmdir("../images/Footwear/Men/Images")
os.rmdir("../images/Footwear/Men")
os.rmdir("../images/Footwear/Women/Images")
os.rmdir("../images/Footwear/Women")
os.rmdir("../images/Footwear")

os.rename("../images/Footwear_temp", "../images/Footwear")

print("(Footwear) Move Completed\n")
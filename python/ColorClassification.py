import pandas as pd
import os
import glob
import shutil


table = pd.read_csv("../data/Fashion_SQL_Formatted.csv")
table.head()


# Create color directories
colornamelist = list(table["COLOR"].unique())
for colorname in colornamelist:
    os.mkdir("../img_COLOR/"+colorname)


# Gather all images
os.mkdir("../allimages")

for file in glob.glob('../images/Apparel/Men/*.jpg'):
    print(file)
    shutil.copy(file, "../allimages")
    
for file in glob.glob('../images/Footwear/Men/*.jpg'):
    print(file)
    shutil.copy(file, "../allimages")

for file in glob.glob('../images/Apparel/Women/*.jpg'):
    print(file)
    shutil.copy(file, "../allimages")
    
for file in glob.glob('../images/Footwear/Women/*.jpg'):
    print(file)
    shutil.copy(file, "../allimages")

# Classify the images by color
for i in range(len(table)):
    productID = table.loc[i, 'PRODUCTID']
    color_ = table.loc[i, 'COLOR']
    shutil.move("../allimages/"+str(productID)+".jpg", "../img_COLOR/"+color_)

os.rmdir("../allimages")

print("Succeeded!")
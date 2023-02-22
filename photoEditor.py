from PIL import Image, ImageEnhance, ImageFilter
import os

# path = './imgs'
# pathOut = '/editedImgs'

# for pic in os.listdir(path):
#     img = Image.open(f"{path}/{pic}")
#     edit = img.filter(ImageFilter.SHARPEN)
#     clean_name = os.path.splitext(pic)[0]
#     edit.save(f'.{pathOut}/{clean_name}_edited.jpg')

# Tried a method from Geeks4Geeks

# img = Image.open(f'{path}')
# img = img.convert("RGB")

# d = img.getdata()

# new_image = []
# for item in d:
#     if item[0] in list(range(200, 256)):
#         new_image.append((255, 224, 100))
#     else:
#         new_image.append(item)

# img.putdata(new_image_data)


# Method from tutorialexample.com


img = Image.open("./imgs/bulbasaur.png")
width = img.size[0]
height = img.size[1]
for i in range(0, width):
    for j in range(0, height):
        data = img.getpixel((i, j))
        if (data[0]==255 and data[1]==255 and data[2]==255):
            img.putpixel((i,j),(44, 44, 44))
img.show()
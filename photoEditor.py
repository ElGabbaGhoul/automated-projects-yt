from PIL import Image
import os

img = Image.open("./imgs/bulbasaur.png")
width = img.size[0]
height = img.size[1]

new_img = Image.new('RGB', (width, height))

for i in range(width):
    for j in range(height):
        # BULB
        # changes bulb light greens to light blues
        r, g, b = img.getpixel((i, j))
        if ( r>= 160 and r <= 185 and g>= 195 and g<=220 and b>= 125 and b <= 150):
            r, g, b = 1, 200, 235
        new_img.putpixel((i, j), (r, g, b))
        # changes bulb medium greens to medium blues
        if (r >= 100 and r <= 140 and g>=160 and g<=200 and b>= 75 and b <= 115):
            r, g, b = 1, 120, 235
        new_img.putpixel((i, j), (r, g, b))
        # changes bulb darkest greens to darkest blues
        if (r >= 40 and r <= 80 and g >= 120 and g <= 160 and b >= 40 and b <= 80 ):
            r, g, b = 30, 30, 150
        new_img.putpixel((i, j), (r, g, b))
        # BODY
        #changes body light green to light orange
        if (r >= 120 and r <= 130 and g >= 186 and g <= 199 and b >= 168 and b >= 180):
            r, g, b = 252, 226, 143
        new_img.putpixel((i, j), (r, g, b))
        # changes body dark green to tan
        # if (r >= x and r <= y and g >= x and g <=y and b >= x and b >= y):
        #     r, g, b = newvalue, newvalue, newvalue
        # new_img.putpixel((i, j), (r, g, b))

new_img.show()

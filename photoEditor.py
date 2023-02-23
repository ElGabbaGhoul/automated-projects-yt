from PIL import Image

img = Image.open("./imgs/bulbasaur.png")

color_map = {
    ((150, 180, 120), (180, 220, 150)): (0, 200, 232)
}

new_img = Image.new(img.mode, img.size)

for i in range(img.size[0]):
    for j in range(img.size[1]):
        # Get the original color of the pixel
        color = img.getpixel((i, j))
        # Look up the new color in the color map
        new_color = None
        for key in color_map:
            if isinstance(key, tuple):
                # key is a color range
                lower, upper = key
                if all(lower[k] <= color[k] <= upper[k] for k in range(3)):
                    new_color = color_map[key]
                    break
            else:
                # key is a color
                if color == key:
                    new_color = color_map[key]
                    break
        # Use the original color if there is no mapping in the color map
        if new_color is None:
            new_color = color
        # Set the new color for the pixel in the new image
        new_img.putpixel((i, j), new_color)

new_img.show()

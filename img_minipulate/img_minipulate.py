from PIL import Image

image_bg = Image.open("beach.jpg")
image_fo = Image.open("cactus.jpg")
image_final = Image.new('RGB', image_bg.size)
pixel_bg = image_bg.load()
pixel_fo = image_fo.load()
pixel_final = image_final.load()
width, height = image_bg.size
color = pixel_fo[1, 1]

for y in range(0, height):
    for x in range(0, width):
        (r, g, b) = pixel_fo[x, y]
        if r <= 150 and 215 <= g and b <= 60:
            pixel_final[x, y] = pixel_bg[x, y]
        else:
            pixel_final[x, y] = pixel_fo[x, y]

image_final.save('final_img.jpg')
image_final.show()

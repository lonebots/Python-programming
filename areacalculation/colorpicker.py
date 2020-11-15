from PIL import Image

img = Image.open('test1.png')

#converting the image to rgb values
rgb_img = img.convert("RGB")
r, g, b = rgb_img.getpixel(
    (1, 1))  #getpixel function fetch the rgb value from thhe image
print(r, g, b)

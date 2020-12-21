#flipping the image
from PIL import Image

#opening the image
img = Image.open("jishnu.jpg")

#transposing the image matrix
trans_img = img.transpose(Image.FLIP_TOP_BOTTOM)

#convert to human understandable format
trans_img.save("jishnu_flip.jpg")

print("dont flipping")
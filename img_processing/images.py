from PIL import Image, ImageFilter

img = Image.open('./img/pikachu.jpg')

print(img.mode)
print(img.size)
print(img.format)

# applies a blur to the image
filtered_img = img.filter(ImageFilter.BLUR)

# converts RGB into grayscale
filtered_img = filtered_img.convert('L')
filtered_img = filtered_img.rotate(90)
# crop removing 100px border
filtered_img = filtered_img.crop((100, 100, 500, 500))
filtered_img = filtered_img.resize((100, 100))


# saved and converted to png
# jpg does not support filters
filtered_img.save('blurred.png', 'png')


#####################################################
astro_img = Image.open('./img/astro.jpg')
# unlike resize, 'thumbnail' method will not strech or compress the image
# it'll try to modify the image maintaining the same aspect ratio
astro_img.thumbnail((400, 400))
astro_img.save('resized_astro.jpg')

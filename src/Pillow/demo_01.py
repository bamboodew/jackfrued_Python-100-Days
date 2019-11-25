from PIL import Image, ImageFilter

im = Image.open('test.jpg')
w, h = im.size
print('Original image size: %sX%s' % (w, h))
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sX%s' % (w // 2, h // 2))
im.save('thumbnail.jpg', 'jpeg')

im_1 = Image.open('cat.jpg')
im_2 = im_1.filter(ImageFilter.BLUR)
im_2.save('blur.jpg', 'jpeg')

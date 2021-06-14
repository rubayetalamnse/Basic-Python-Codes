from PIL import Image
woman_picture = Image.open('bifa.jpg')
bg1 = Image.open('mus1.jpg')
bg1.paste(woman_picture,(0, 0), woman_picture)
bg1.show()

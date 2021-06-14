from PIL import Image
man_picture = Image.open('man.png')
bg1 = Image.open('mus1.jpg')
bg1.paste(man_picture,(0, 0), man_picture)
bg1.show()

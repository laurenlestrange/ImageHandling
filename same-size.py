import os, glob
from PIL import Image

size = input('maximum px: ')

folder = size + 'px'
if not os.path.exists(folder):
    os.mkdir(folder)

input = int(size)

pics = []
for file in glob.glob('*.png'):
    pic = Image.open(file)
    pics.append(pic)

max_W = 0
max_H = 0
for pic in pics:
    W, H = pic.size
    W, H = round(input * W / H), round(input * H / W)
    if W > max_W:
        max_W = W
    if H > max_H:
        max_H = H

for pic in pics:
    W, H = pic.size
    if W > H:
        W, H = max_W, round(max_W * H / W)
    else:
        W, H = round(max_H * W / H), max_H
    resized = pic.resize((W, H))
    canvas = Image.new('RGBA', (max_W, max_H), (0, 0, 0, 0))
    center = ((max_W - W) // 2, (max_H - H) // 2)
    canvas.paste(resized, center)
    canvas.thumbnail((input, input))
    canvas.save(folder + '/' + pic.filename)

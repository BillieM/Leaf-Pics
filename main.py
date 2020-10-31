from functionTime import leafProcessor
import os

imgs = []
path = os.path.abspath(os.path.dirname(__file__))
try:
    os.mkdir(f'{path}/out')
except:
    pass
valid_images = ['.jpg', '.png']

for i, f in enumerate(os.listdir(path)):

        name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1]

        if ext.lower() not in valid_images:
            continue

        '''
        optional params:
            detect edges
                default 160 - 210

        '''

        leafProcessor(str(i), f, ext, 160, 210)

for i, f in enumerate(os.listdir(f'{path}/out')):
    size = os.stat(f'out/{f}').st_size
    if size < 4000:
        os.remove(f'out/{f}')
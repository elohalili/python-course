import sys
from os import listdir
from pathlib import Path

from PIL import Image

source_dir = sys.argv[1]
destination_dir = sys.argv[2]
# create destination dir if it doesn't exist
Path(destination_dir).mkdir(exist_ok=True)

try:
    for img in listdir(source_dir):
        # retrieve the file name without the extension
        img_name = img[:img.index('.')]
        # open image
        image = Image.open(f'{source_dir}/{img}')
        # save the new image converting it to png
        image.save(f'{destination_dir}/{img_name}.png', 'png')
except Exception as err:
    raise err

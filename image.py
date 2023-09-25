import sys
import os
from PIL import Image

path = r"C:/Users/guest1/Desktop/img"
directory = r"C:/Users/guest1/OneDrive/Documents/python tools/converted"
if not os.path.exists(directory):
    os.makedirs(directory)

# Process and convert images
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(os.path.join(path, filename))
    img.save(os.path.join(directory, f'{clean_name}.png'), 'png')

print('All done!')

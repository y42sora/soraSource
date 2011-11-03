'''
Created on 2011/10/25

@author: y42sora

from here
http://handasse.blogspot.com/2008/04/python_16.html
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""covgraph.py  by nox, 2008.4.15"""

import sys, os, bz2, base64
from PIL import Image

def cover(input_image, output_image, text_data):
    """
    """
    if os.path.isfile(text_data):
        text = file(text_data).read()
    else: text = text_data
    bz2_text = bz2.compress(text)
    b16_text = base64.b16encode(bz2_text)
    im = Image.open(input_image).convert("RGB").convert("RGBA")
    data = list(im.getdata())
    if len(data) < len(b16_text) * 4:
        print >>sys.stderr, "Error: text too large."
        sys.exit(1)
    for i in range(len(b16_text)):
        for j in range(4):
            n = i * 4 + j
            data[n] = (data[n][0], data[n][1], data[n][2], 255 - (int(b16_text[i], 16) >> j & 1))
    data[n+1] = (data[n+1][0], data[n+1][1], data[n+1][2], 253)
    im.putdata(data)
    im.save(output_image)

def uncover(image_file):
    im = Image.open(image_file)
    data = list(im.getdata())
    end = [d[3] for d in data].index(253)
    data = [hex((255 - a[3]) + ((255 - b[3]) << 1) + ((255 - c[3]) << 2) + ((255 - d[3]) << 3)).upper()[-1] for a, b, c, d in zip(data[:end:4], data[1:end:4], data[2:end:4], data[3:end:4])]
    b16_text = "".join(data)
    bz2_text = base64.b16decode(b16_text)
    text = bz2.decompress(bz2_text)
    return text

def main(args):
    cover("tetriscosp.jpg","Tetris.png", "Tetris.py")
    #print uncover("tetris.png")

if __name__ == "__main__": main(sys.argv)

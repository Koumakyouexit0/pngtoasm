import re
from PIL import Image

def list():
    import os
    files = [f for f in os.listdir('.') if f.lower().endswith('.inc')]
    if not files:
        print("Not found anything!!")
        exit(1)
    print("Choose .inc file:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    choice = int(input("Nhập số: "))
    return files[choice-1]

def imgsize(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    width = None
    height = None
    hex_values = []
    for line in lines:
        if '_width' in line:
            width = int(line.split()[-1])
        elif '_height' in line:
            height = int(line.split()[-1])
        else:
            hex_values.extend(re.findall(r'0x([0-9A-Fa-f]{2})', line))
    if width is None or height is None:
        raise ValueError("Width/Height not found in inc file")
    return width, height, [int(x, 16) for x in hex_values]

def imgblock(pixels, width, height):
    total_pixels = width * height
    pixels = pixels[:total_pixels]
    for y in range(0, height, 2):
        line = ''
        for x in range(width):
            top = pixels[y * width + x]
            bottom = pixels[(y+1) * width + x] if y+1 < height else (0, 0, 0)
            line += f'\x1b[38;2;{top[0]};{top[1]};{top[2]}m\x1b[48;2;{bottom[0]};{bottom[1]};{bottom[2]}m▀'
        line += '\x1b[0m'
        print(line)

inc_file = list()

orig_w, orig_h, pixel_bytes = imgsize(inc_file)

img_pixels = []
for i in range(0, len(pixel_bytes), 3):
    img_pixels.append((pixel_bytes[i], pixel_bytes[i+1], pixel_bytes[i+2]))

imgblock(img_pixels, orig_w, orig_h)

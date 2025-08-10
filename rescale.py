from PIL import Image

# image path
input_path = "a.png"

# image reader
img = Image.open(input_path)
orig_w, orig_h = img.size

# image scale
res_options = [
    ("Gốc", (orig_w, orig_h)),
    ("720p", (1280, 720)),
    ("480p", (854, 480)),
    ("360p", (640, 360)),
    ("240p", (426, 240)),
    ("144p", (256, 144)),
    ("96p", (170, 96)),
    ("Customize", None)
]

print("Chọn độ phân giải:")
for i, (name, size) in enumerate(res_options, 1):
    if size:
        print(f"{i}. {name} - {size[0]}x{size[1]}")
    else:
        print(f"{i}. {name}")

choice = int(input(" Input: "))

# new w/h
if choice == len(res_options):  # custom size
    new_w = int(input("Width: "))
    new_h = int(input("Height: "))
else:
    new_w, new_h = res_options[choice-1][1]

# resize module
img_resized = img.resize((new_w, new_h), Image.LANCZOS)

# save
output_path = f"output_{new_w}x{new_h}.png"
img_resized.save(output_path)

print(f" Done and save on {output_path}")

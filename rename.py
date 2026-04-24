import os

files = os.listdir('folder/')
i = 1c
for image in files:
    image_name = f"{image}".split(".")
    os.rename(image_name[0],(f"image_{i}."+image_name[1]))
    i+=1, 
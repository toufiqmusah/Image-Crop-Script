import os
from PIL import Image
from pathlib import Path


folder_path = Path(r"C:\Users\\OWNER\\Desktop\\Image-Crop-Script\\Test-Input")
save_path = Path(r"C:\\Users\\OWNER\Desktop\\Image-Crop-Script\\Output")

# Adjust for desired crop length
crop_ratio = 0.95

#loop through images in the directory
for images in os.listdir(folder_path):
    # Open the image
    print(f'Working on {folder_path.joinpath(images)}')
    image = Image.open(folder_path.joinpath(images))

    # Calculating dimensions for the crop
    width, height = image.size
    new_height = int(height * crop_ratio)
        
    # box for cropping (left, upper, right, lower)
    crop_box = (0, 0, width, new_height)
        
    # Crop the image and save it
    cropped_image = image.crop(crop_box)
    cropped_image.save(save_path.joinpath(images))
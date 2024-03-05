import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageFilter
import os

# Paths to the CSV files
images_csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240302/testing/embedding_of_patch_64.csv'
values_csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240302/testing/predicted_cost_of_patch_64.csv'
output_dir = '/home/zhiyundeng/AEROPlan/experiment/20240302/splitted_costmap'  # User-specified output directory

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load CSV files
df_images = pd.read_csv(images_csv_path)
df_values = pd.read_csv(values_csv_path)

# Assuming both CSVs are sorted and aligned; otherwise, you'll need to join them on a common key
mapped_values = dict(zip(df_images.iloc[:, 0], df_values.iloc[:, 0]))

def value_to_intensity(value):
    # Maps the value (0 to 3) to a grayscale intensity (255 is white, 0 is black)
    return {
        0: 0,  # White
        1: 85,  # Light gray
        2: 170,   # Dark gray
        3: 255     # Black
    }[value]

def convert_to_density_map(image_path, value, output_dir):
    # Convert an image's intensity based on its value, then apply Gaussian blur
    intensity = value_to_intensity(value)
    with Image.open(image_path) as img:
        # Convert image to grayscale
        gray_img = img.convert('L')
        # Apply the initial intensity
        np_img = np.array(gray_img)
        np_img[:] = intensity
        pre_blur_img = Image.fromarray(np_img)
        # Apply Gaussian blur to create a density effect
        blurred_img = pre_blur_img.filter(ImageFilter.GaussianBlur(radius=5))  # Adjust the radius as needed
        # Save the modified image to the specified output directory
        blurred_img.save(os.path.join(output_dir, os.path.basename(image_path)))

# Process each image with the new function
for img_path, value in mapped_values.items():
    convert_to_density_map(img_path, value, output_dir)
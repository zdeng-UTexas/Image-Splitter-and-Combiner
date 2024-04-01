#     image_paths_csv = '/home/dengzy/AEROPlan_Dataset/Costmap/embeddings_256_testing.csv'  # Path to the CSV with image paths
#     values_csv = '/home/dengzy/AEROPlan_Dataset/Costmap/embeddings_256_predictive_cost.csv'  # Path to the CSV with values
#  output_dir='/home/dengzy/AEROPlan_Dataset/Costmap/Processed_Images'):
#     # Read the CSV files into dictionaries

import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageFilter
import os

# Paths to the CSV files
images_csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240320/testing/embedding_of_patch_32.csv'
values_csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240320/testing/predicted_cost_of_patch_32.csv'
output_dir = '/home/zhiyundeng/AEROPlan/experiment/20240320/splitted_costmap_32'  # User-specified output directory

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
        # 0: 0
        # 10: 10
        # 80: 80
        # 160: 160
        # 254: 254
    }[value]

def convert_to_color(image_path, value, output_dir):
    # Convert an image to a specific shade of gray based on its value.
    # intensity = value_to_intensity(value)
    intensity = value
    with Image.open(image_path) as img:
        # Convert image to grayscale
        gray_img = img.convert('L')
        # Apply the intensity
        np_img = np.array(gray_img)
        np_img[:] = intensity
        final_img = Image.fromarray(np_img)
        # Save the modified image to the specified output directory
        final_img.save(os.path.join(output_dir, os.path.basename(image_path)))

# Process each image
for img_path, value in mapped_values.items():
    convert_to_color(img_path, value, output_dir)

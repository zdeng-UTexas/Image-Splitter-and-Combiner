import csv
from PIL import Image
import numpy as np

def read_csv_to_dict(filename, key_column_index=0, value_column_index=1):
    """Read a CSV file and return a dictionary with keys and values from specified columns."""
    result_dict = {}
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key = row[key_column_index]
            value = row[value_column_index]
            result_dict[key] = value
    return result_dict

def process_images(image_paths_csv, values_csv, output_dir='/home/dengzy/AEROPlan_Dataset/Costmap/Processed_Images'):
    # Read the CSV files into dictionaries
    image_paths = read_csv_to_dict(image_paths_csv, key_column_index=0, value_column_index=0)
    values = read_csv_to_dict(values_csv, key_column_index=0, value_column_index=1)
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each image
    for image_name, image_path in image_paths.items():
        value = int(values[image_name])  # Convert the value to an integer (or adjust based on your color logic)
        color = (value, value, value)  # Assuming grayscale for simplicity
        
        # Load the image
        img = Image.open(image_path)
        img = img.convert('RGB')  # Ensure the image is in RGB mode
        
        # Create a new image with the same size but filled with the determined color
        processed_img = Image.new('RGB', img.size, color=color)
        
        # Save the processed image
        processed_img_path = os.path.join(output_dir, os.path.basename(image_path))
        processed_img.save(processed_img_path)

    print(f"Processed images have been saved to {output_dir}")

# Example usage
if __name__ == "__main__":
    image_paths_csv = '/home/dengzy/AEROPlan_Dataset/Costmap/embeddings_256_testing.csv'  # Path to the CSV with image paths
    values_csv = '/home/dengzy/AEROPlan_Dataset/Costmap/embeddings_256_predictive_cost.csv'  # Path to the CSV with values
    process_images(image_paths_csv, values_csv)

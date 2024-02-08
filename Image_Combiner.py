from PIL import Image
import os
import sys
import re

def filename_to_position(filename):
    """Extracts row and column indices from the filename."""
    parts = filename.split('.')[0].split('_')  # Split by underscore and remove file extension
    return int(parts[0]), int(parts[1])

def combine_patches(input_dir, output_image_path):
    # List all the files and sort them by row and column using the filename_to_position function
    files = sorted(os.listdir(input_dir), key=filename_to_position)

    # Open the first patch to get the dimensions
    first_patch = Image.open(os.path.join(input_dir, files[0]))
    patch_width, patch_height = first_patch.size

    # Assuming files are correctly named and present for every position
    num_patches_x = max(filename_to_position(file)[1] for file in files)
    num_patches_y = max(filename_to_position(file)[0] for file in files)

    img_width = patch_width * num_patches_x
    img_height = patch_height * num_patches_y

    # Create a new image with the calculated dimensions
    original_image = Image.new('RGB', (img_width, img_height))

    # Iterate over each patch and paste it into the correct position
    for file in files:
        row, col = filename_to_position(file)
        patch = Image.open(os.path.join(input_dir, file))
        x = (col - 1) * patch_width
        y = (row - 1) * patch_height
        original_image.paste(patch, (x, y))

    # Save the reassembled image
    original_image.save(output_image_path)
    print(f"Image reassembled and saved to: {output_image_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 Image_Combiner.py <input_dir> <output_image_path>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_image_path = sys.argv[2]
    
    combine_patches(input_dir, output_image_path)


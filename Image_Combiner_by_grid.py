import os
from PIL import Image
import sys
import re  # Import regular expressions module

def combine_images(input_dir, output_image_path):
    """
    Combine grid images into a single image.

    :param input_dir: Directory containing the grid images.
    :param output_image_path: Path to save the combined image.
    """
    # Use a regular expression to match files and extract coordinates
    pattern = re.compile(r'grid_(\d+)_(\d+)\.png')

    # Find all files that match the expected pattern
    image_files = [f for f in os.listdir(input_dir) if pattern.match(f)]
    if not image_files:
        print("No matching images found in the directory.")
        return

    # Extract coordinates and sort
    image_files.sort(key=lambda x: (int(pattern.match(x).group(1)), int(pattern.match(x).group(2))))

    # Open the first image to get the size
    with Image.open(os.path.join(input_dir, image_files[0])) as img:
        grid_width, grid_height = img.size

    # Calculate the dimensions of the combined image
    grid_size_x = max(int(pattern.match(f).group(1)) for f in image_files) + 1
    grid_size_y = max(int(pattern.match(f).group(2)) for f in image_files) + 1
    total_width = grid_width * grid_size_x
    total_height = grid_height * grid_size_y

    # Create a new image with the combined dimensions
    combined_image = Image.new('RGB', (total_width, total_height))

    # Place each grid image in its correct position
    for image_file in image_files:
        match = pattern.match(image_file)
        x, y = int(match.group(1)), int(match.group(2))
        with Image.open(os.path.join(input_dir, image_file)) as img:
            combined_image.paste(img, (x * grid_width, y * grid_height))

    # Save the combined image
    combined_image.save(output_image_path)
    print(f"Combined image saved as {output_image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 Image_Combiner_by_grid.py /path/to/patches /path/to/output/image.jpg")
        sys.exit(1)

    input_dir, output_image_path = sys.argv[1], sys.argv[2]
    combine_images(input_dir, output_image_path)

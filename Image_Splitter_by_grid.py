import os
from PIL import Image
import sys

def split_image(image_path, grid_x, grid_y, output_dir):
    """
    Splits the image into smaller grid cells.

    :param image_path: Path to the input image.
    :param grid_x: Number of grid cells along the x-axis.
    :param grid_y: Number of grid cells along the y-axis.
    :param output_dir: Directory to save the output images.
    """
    try:
        img = Image.open(image_path)
        img_width, img_height = img.size
        cell_width = img_width // grid_x
        cell_height = img_height // grid_y

        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for x in range(grid_x):
            for y in range(grid_y):
                left = x * cell_width
                upper = y * cell_height
                right = (x+1) * cell_width
                lower = (y+1) * cell_height

                img_cropped = img.crop((left, upper, right, lower))
                output_path = os.path.join(output_dir, f'grid_{x}_{y}.png')
                img_cropped.save(output_path)
                print(f'Saved: {output_path}')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python Image_Splitter_by_grid.py <image_path> <grid_x> <grid_y> <output_dir>")
        sys.exit(1)

    image_path, grid_x, grid_y, output_dir = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    split_image(image_path, grid_x, grid_y, output_dir)

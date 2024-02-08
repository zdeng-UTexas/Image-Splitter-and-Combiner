from PIL import Image
import os
import sys
import zipfile

def split_image(image_path, patch_width, patch_height, output_dir='patches'):
    # Load the image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Calculate the number of patches in each dimension
    num_patches_x = img_width // patch_width
    num_patches_y = img_height // patch_height

    # Split the image into patches and save them
    for y in range(num_patches_y):
        for x in range(num_patches_x):
            left = x * patch_width
            upper = y * patch_height
            right = left + patch_width
            lower = upper + patch_height

            # Extract the patch and save it
            patch = img.crop((left, upper, right, lower))
            patch_filename = f"{y+1}_{x+1}.png"  # Naming as row_column
            patch_path = os.path.join(output_dir, patch_filename)
            patch.save(patch_path)

    # Zip the patches
    zip_filename = os.path.join(output_dir + '.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    return zip_filename

# # Example usage
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 split_image.py <image_path> <patch_width> <patch_height> <output_dir>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    patch_width = int(sys.argv[2])
    patch_height = int(sys.argv[3])
    output_dir = sys.argv[4]
    
    zip_path = split_image(image_path, patch_width, patch_height, output_dir)
    print(f"Patches saved and zipped at: {zip_path}")


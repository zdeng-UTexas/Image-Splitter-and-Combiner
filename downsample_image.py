from PIL import Image
import sys

def downsample_image(input_image_path, output_image_path, target_width, target_height):
    """
    Resize an image to the specified dimensions.

    :param input_image_path: Path to the input image.
    :param output_image_path: Path to save the resized image.
    :param target_width: Target width of the image.
    :param target_height: Target height of the image.
    """
    try:
        # Open the original image
        with Image.open(input_image_path) as img:
            # Resize the image
            resized_img = img.resize((target_width, target_height), Image.ANTIALIAS)

            # Save the resized image
            resized_img.save(output_image_path)
            print(f"Resized image saved as {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python downsample_image.py <input_image_path> <output_image_path> <target_width> <target_height>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    target_width = int(sys.argv[3])
    target_height = int(sys.argv[4])

    downsample_image(input_image_path, output_image_path, target_width, target_height)

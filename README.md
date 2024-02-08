# Image-Splitter-and-Combiner

This repository contains two Python scripts for splitting an image into a grid of patches and then reassembling those patches back into the original image. The scripts are designed to work with images of any size and split them into patches of specified dimensions.

## Scripts

- `Image_Splitter.py`: Splits a given image into smaller patches based on specified dimensions (width and height in pixels). The patches are saved with filenames indicating their position in the original image (e.g., `1_1.png` for the first row and first column), and then zipped into a single file.

- `Image_Combiner.py`: Takes a directory of image patches named according to their position in the original image and reassembles them into a single image file.

## Requirements

- Python 3
- Pillow library

Before running the scripts, make sure you have Python 3 installed on your system and install the Pillow library using pip:

```bash
pip install Pillow
```

## Usage

### Splitting an Image

To split an image, run `Image_Splitter.py` with the following arguments:

1. Path to the input image.
2. Desired patch width in pixels.
3. Desired patch height in pixels.
4. Output directory to save the patches.

Example:

```bash
python Image_Splitter.py "/path/to/image.jpg" 512 512 "/path/to/output/directory"
```

This will split `image.jpg` into 512x512 patches and save them in the specified output directory, followed by zipping these patches into a single file.

Example output:

```
Patches saved and zipped at: /path/to/output/directory/patches.zip
```

### Combining Image Patches

To reassemble an image from patches, run `Image_Combiner.py` with the following arguments:

1. Path to the directory containing the image patches.
2. Path to save the reassembled image.

Example:

```bash
python3 Image_Combiner.py /path/to/patches /path/to/output/image.jpg
```

This will reassemble the patches located in `/path/to/patches` into a single image and save it to `/path/to/output/image.jpg`.

Example output:

```
Image reassembled and saved to: /path/to/output/image.jpg
```

## Tutorial Example

- **Splitting an Image**

```bash
(base) zhiyunjerrydeng@wireless-10-146-142-131 ~ % python Image_Splitter.py "/Users/zhiyunjerrydeng/Library/CloudStorage/Box-Box/University of Texas at Austin/AMRL/SARA/Aerial Imagery/EER-02072024/DJI_0432.JPG" 512 512 "/Users/zhiyunjerrydeng/Downloads/patches"
Patches saved and zipped at: /Users/zhiyunjerrydeng/Downloads/patches.zip
```

- **Combining Image Patches**

```bash
(base) zhiyunjerrydeng@wireless-10-146-142-131 ~ % python3 Image_Combiner.py /Users/zhiyunjerrydeng/Downloads/patches /Users/zhiyunjerrydeng/Downloads/merge.png 
Image reassembled and saved to: /Users/zhiyunjerrydeng/Downloads/merge.png
```

## Contributing

Feel free to fork this repository and submit pull requests to contribute to the development of these scripts.

## License

This project is open-source and available under the MIT License.

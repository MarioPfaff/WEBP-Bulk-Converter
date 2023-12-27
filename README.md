# .WEBP Bulk Converter

This converter simplifies the transformation of multiple images into lossless .webp files, allowing users to adjust resolution and quality settings. Developed to address limitations found in online tools that often charge for these basic functionalities, this tool offers a cost-free solution.

## Dependencies

This project relies on the Python Imaging Library (PIL) for image processing and conversion.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

## Usage Guide

### Getting Started

- **Preparing Images:**
  - Add your images to the designated folder. An example folder can be found in the distributed files under `images > unoptimized`.

- **Running the Converter:**
  - Launch the .exe file under `dist > convert_images.exe`
  - Specify the directory of your unoptimized files (input).
  - Set the directory for the optimized files to be saved (output).

- **Customizing Settings:**
  - Optionally adjust the quality and/or resolution settings.

### Additional Information

- **Resolution Handling:** The converter maintains the aspect ratio of the image, ensuring the closest possible match during conversion.
- **Quality Recommendations:** To retain the lossless nature of .webp images, it's recommended to maintain a quality above 95%. However, this setting is adjustable to suit specific preferences.

### Notes

- Feel free to customize settings based on your preferences or requirements.
- Any adjustments made to resolution or quality might impact the resulting file sizes and image quality.

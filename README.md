# Image Color Decomposition and Restoration with Eigenvectors

This Python program uses the `PIL` (Python Imaging Library) to perform image decomposition based on eigenvectors of the covariance matrix of the RGB channels and restores the image. The program extracts the RGB values of an image, computes the mean, the covariance matrix, and the eigenvectors. It then uses one of the eigenvectors to transform the image and restore it back.

### Input
<p align="center">
  <img src="./images/girl1.png" alt="Photo1" height="200"/>
  <img src="./images/girl2.png" alt="Photo2" height="200"/>
  <img src="./images/fox.jpg" alt="Photo3" height="200"/>
</p>

### Output
<p align="center">
  <img src="./images/new_girl1.png" alt="NewPhoto1" height="200"/>
  <img src="./images/new_girl2.png" alt="NewPhoto2" height="200"/>
  <img src="./images/new_fox.png" alt="NewPhoto3" height="200"/>
</p>

## Features

- **Decompose the image's RGB channels**: Extract RGB values from the image and stack them into a matrix for analysis.
- **Covariance and Eigenvector Calculation**: Calculate the covariance matrix of the centered RGB data and extract eigenvectors.
- **Image Restoration**: Use the eigenvectors and centered data to restore the image.
  
## Requirements

- Python 3.x
- Libraries:
  - `PIL` (Python Imaging Library) or `Pillow`
  - `numpy`

## Usage

Run the program from the command line.
```bash
python <script_name>.py <input_image> <output_image>
```

Where:
- <input_image>: The path to the input image.
- <output_image>: The path to save the restored image.

Process Breakdown
1. **Extracting RGB values:** The program reads the input image and extracts the RGB channel values into three separate arrays. These arrays are stacked together to form a matrix X.

2. **Centering the data:** The RGB arrays are centered by subtracting their mean values. This results in a centered matrix Xcentered.

3. **Covariance Matrix:** A covariance matrix of the centered RGB values is calculated. This matrix captures the relationship between the color channels.

4. **Eigenvectors and Eigenvalues:** The eigenvalues and eigenvectors of the covariance matrix are computed. Each eigenvector corresponds to one direction of variation in the color data.

5. **Image Restoration:** The image is restored by applying the selected eigenvector (first by default) to the centered data and adding the mean values back.

## Customization

*Changing the eigenvector:* The script allows you to select different eigenvectors to restore the image:

```bash
v = eigvecs[:, 0]  # First eigenvector
v = eigvecs[:, 1]  # Second eigenvector
v = eigvecs[:, 2]  # Third eigenvector
```

By default, the first eigenvector is used. You can uncomment the desired line to use another.

## Output
- The output is a PNG image saved with the provided filename.
- The restored image should look different depending on the eigenvector used, revealing different aspects of the color variation in the original image.

## Notes
- The process of image restoration and transformation is dependent on the chosen eigenvector. Each eigenvector emphasizes different characteristics of the color distribution in the image.
- This script currently only supports RGB images.
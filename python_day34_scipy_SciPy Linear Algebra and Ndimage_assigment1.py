# Lab 1: Using a sobel filter. filter the image and then diplay it

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from imageio import imread
import requests
from PIL import Image
from io import BytesIO

# Step 1: Load the image from URL
url = 'https://github.com/AnudipAE/DANLC/blob/master/dog.jpg?raw=true'
response = requests.get(url)
image = Image.open(BytesIO(response.content))

# Step 2: Convert the image to grayscale
image = np.array(image.convert('L'))

# Step 3: Apply Sobel filter using scipy
sobelx = ndimage.sobel(image, axis=0)  # Sobel filter along X-axis
sobely = ndimage.sobel(image, axis=1)  # Sobel filter along Y-axis

# Combine both the X and Y gradient directions
sobel_combined = np.hypot(sobelx, sobely)

# Step 4: Plot the original and the Sobel filtered image
plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(sobel_combined, cmap='nipy_spectral')  # Use 'nipy_spectral' for a colorful filter effect
plt.title('Filtered Image (Sobel Filter)')
plt.axis('off')

plt.show()

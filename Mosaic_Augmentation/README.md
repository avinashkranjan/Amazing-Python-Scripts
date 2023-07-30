# Mosaic Augmentation Implementation in Python

This script implements the mosaic augmentation technique in Python to create mosaics of images. Mosaic augmentation is a data augmentation method commonly used in computer vision tasks to augment image datasets.

## Setup Instructions

To use this script, follow these steps:

1. Install the required dependencies:

```bash
pip install numpy opencv-python Pillow
```

2. Download the script from the GitHub repository: [link-to-repository]

3. Place the script in the same directory as the dataset folder containing 'Annotations' and 'Images' subfolders.

4. Import the necessary modules at the beginning of your script:

```python
import random
import cv2
import os
import glob
import numpy as np
from PIL import Image
```

5. Modify the `ANNO_DIR` and `IMG_DIR` variables in the script to point to the respective folders containing annotations and images.

6. Run the script:

```bash
python script_name.py
```

## Detailed Explanation

This script reads a dataset of annotated images, randomly selects four images, and creates a mosaic image by combining them. The mosaic is divided into four quadrants, and each input image is placed in one quadrant with a random scale. Annotations for the new mosaic are also updated accordingly.


### Developed by [Arvind Srivastav](https://github.com/alwenpy)

## Disclaimers

This script is provided as-is and without any warranties. The author is not responsible for any misuse or damages resulting from the use of this script. Use it responsibly and at your own risk.
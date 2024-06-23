from PIL import Image
import numpy as np

# Rotation code
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = list(reversed(matrix[i]))

# Function to load image and convert to 2D matrix
def image_to_matrix(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    matrix = np.array(image).tolist()
    return matrix

# Function to convert 2D matrix back to image
def matrix_to_image(matrix):
    array = np.array(matrix, dtype=np.uint8)
    image = Image.fromarray(array)
    return image

# Main function to rotate image
def rotate_image(image_path, output_path):
    matrix = image_to_matrix(image_path)
    solution = Solution()
    solution.rotate(matrix)
    rotated_image = matrix_to_image(matrix)
    rotated_image.save(output_path)

# Example usage
input_image_path = 'input_image.jpeg'  # Replace with your image path
output_image_path = 'rotated_image.jpg'  # Path to save the rotated image

rotate_image(input_image_path, output_image_path)
print(f"Rotated image saved as {output_image_path}")

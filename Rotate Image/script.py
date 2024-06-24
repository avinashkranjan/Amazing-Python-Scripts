from PIL import Image
import numpy as np


def rotate(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.

    Parameters:
    matrix (list of list of int): The 2D matrix to be rotated.

    Returns:
    list of list of int: The rotated 2D matrix.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i] = list(reversed(matrix[i]))
    return matrix


def image_to_matrix(image_path):
    """
    Loads an image and converts it to a 2D matrix.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    list of list of int: The image represented as a 2D matrix.
    """
    image = Image.open(image_path)
    image = image.convert('RGB')
    matrix = np.array(image).tolist()
    return matrix


def matrix_to_image(matrix):
    """
    Converts a 2D matrix back to an image.

    Parameters:
    matrix (list of list of int): The 2D matrix representing the image.

    Returns:
    Image: The image object created from the 2D matrix.
    """
    array = np.array(matrix, dtype=np.uint8)
    image = Image.fromarray(array)
    return image


def rotate_image(image_path, output_path):
    """
    Rotates an image 90 degrees clockwise and saves the rotated image.

    Parameters:
    image_path (str): The path to the input image file.
    output_path (str): The path to save the rotated image file.

    Returns:
    None
    """
    matrix = image_to_matrix(image_path)
    matrix = rotate(matrix)
    rotated_image = matrix_to_image(matrix)
    rotated_image.save(output_path)


# Example usage
input_image_path = 'input_image.jpeg'  # Replace with your image path
output_image_path = 'rotated_image.jpg'  # Path to save the rotated image

rotate_image(input_image_path, output_image_path)
print(f"Rotated image saved as {output_image_path}")

import cv2
import argparse


def perform_bitwise_operations(image1_path, image2_path):
    src1 = cv2.imread(image1_path)
    src2 = cv2.imread(image2_path)

    # Resizing the images to have the same dimensions
    src2 = cv2.resize(src2, src1.shape[1::-1])

    # Performing bitwise AND operation
    and_op = cv2.bitwise_and(src1, src2, mask=None)

    # Performing bitwise OR operation
    or_op = cv2.bitwise_or(src1, src2, mask=None)

    # Performing bitwise XOR operation
    xor_op = cv2.bitwise_xor(src1, src2, mask=None)

    return and_op, or_op, xor_op


def save_images(image1, image2, image3):
    cv2.imshow('Bitwise AND', image1)
    cv2.imshow('Bitwise OR', image2)
    cv2.imshow('Bitwise XOR', image3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Creating command-line arguments parser
    parser = argparse.ArgumentParser(
        description='Perform bitwise operations on two images.')
    parser.add_argument('image1', type=str,
                        help='Path to the first image file.')
    parser.add_argument('image2', type=str,
                        help='Path to the second image file.')
    args = parser.parse_args()

    image1_path = args.image1
    image2_path = args.image2

    # Performing bitwise operations
    result1, result2, result3 = perform_bitwise_operations(
        image1_path, image2_path)

    # Displaying and saving the resulting images
    save_images(result1, result2, result3)

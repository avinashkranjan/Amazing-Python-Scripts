import cv2


def resize_image(input_image, output_image, new_width, new_height):
    # Read the input image
    image = cv2.imread(input_image)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Save the resized image
    cv2.imwrite(output_image, resized_image)

    print("Image resized and saved successfully!")

    # Display the original image
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)

    # Display the resized image
    resized_image = cv2.imread(output_image)
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Specify the input image path, output image path, and new dimensions
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'
new_width = 300
new_height = 150

# Resize the image
resize_image(input_image_path, output_image_path, new_width, new_height)

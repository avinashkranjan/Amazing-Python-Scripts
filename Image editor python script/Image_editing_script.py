"""
IMAGE EDITOR USING PILLOW LIBRARY.
"""

# Importing the image module from pillow library.

# Importing ImageFilter, ImageEnhance modules from pillow library.

from PIL import Image, ImageFilter, ImageEnhance

# Importing system module.

import sys

'''
============================================================================
^^^~~~~~~~~~~~~~~~~~~~~~|||||DEFINED FUNCTIONS|||||~~~~~~~~~~~~~~~~~~~~~~^^^
============================================================================
'''

'''
============== Function to show available options on CLI ==================
'''


def home():

    print(" --> 1. Flip the image.")

    print(" --> 2. Rotate the image by 90 degrees.")

    print(" --> 3. Rotate the image by 180 degrees")

    print(" --> 4. Blur the image")

    print(" --> 5. Embossed image")

    print(" --> 6. Apply more filters")

    print(" --> 7. Contrast adjustments")

    print(" --> 8. Increase sharpness")

    print(" --> 9. quit")

    print(" ")


'''
======================== Function to save edited image ========================
'''


# This function will ask the user if he wants the edited file to be saved

def saving_edited_image():

    print("========Do you want to save the edited image ?==========")

    saving_choice = input("Type 1 for YES and 2 for NO : ")

    if saving_choice in ("1", "2"):

        if saving_choice == '1':

            path_specified = input(r"===== Enter the path where you"
                                   r" want to store the edited image."
                                   r"also mention the name of image "
                                   r"with extension=====")

            # saving the image at given path

            im.save(path_specified)

            # final message after saving the image

            print("====Image changes done and saved !! Keep editing====")

        if saving_choice == '2':

            # back to the main menu

            print("~~~Back to the main menu~~~")

            main()

    else:

        '''
        if the user inputs value other than the specified ones,
        this function will be called again.
        '''

        print("=====!!! PLEASE CHOOSE FROM SPECIFIED OPTIONS !!!=====")

        saving_edited_image()


'''
================== Function for edited image preview =======================
'''


'''
this function will ask the user if he wants a
preview of edited image or not and will provide the same
'''


def edited_image_preview(image_name):

    print("=======Do you want to preview the edited image ?=======")

    preview_choice = input("Type 1 for YES and 2 for NO : ")

    if preview_choice in ('1', '2'):

        if preview_choice == '1':

            # this will show the edited image for the user to review

            image_name.show()

            # function to save the image is called

            saving_edited_image()

        if preview_choice == '2':
            # function to save the image is again called

            saving_edited_image()

    else:

        print("=====!!! PLEASE CHOOSE FROM SPECIFIED OPTIONS !!!=====")

        edited_image_preview(image_name)


'''
====================== Function to flip image =====================
'''


def flip():

    flipped_image = im.transpose(Image.FLIP_LEFT_RIGHT)

    # function to preview edited image is called

    edited_image_preview(flipped_image)


'''
=================== Function to rotate image by 90 degrees =================
'''


def rotate_90():

    rotated_image_90 = im.transpose(Image.ROTATE_90)

    # function to preview edited image is called

    edited_image_preview(rotated_image_90)


'''
================ Function to rotate image by 180 image ============
'''


def rotate_180():

    rotated_image_180 = im.transpose(Image.ROTATE_180)

    # function to preview edited image is called

    edited_image_preview(rotated_image_180)


'''================= function to blur the image ==================='''


def blur():

    blur_image = im.filter(ImageFilter.BLUR)

    # function to preview edited image is called

    edited_image_preview(blur_image)


'''================== Function to emboss the image =================='''


def embossing():

    emboss_image = im.filter(ImageFilter.EMBOSS)

    # function to preview edited image is called

    edited_image_preview(emboss_image)


'''================ Function to sharpen the image ====================='''


def sharpen():

    sharpness_enhancer = ImageEnhance.Sharpness(im)

    sharpened_image = sharpness_enhancer.enhance(5)

    # function to preview edited image is called

    edited_image_preview(sharpened_image)


'''============= Function for changing the contrast ================='''


# this is the function to increase or decrease the contrast of the image

def contrast():

    print("Actions available : ")

    print("--> 1. Increase contrast")

    print("--> 2. Decrease contrast")

    print("--> 3. Main menu")

    contrast_choice = input("CHOOSE ACTION TO TAKE : ")

    if contrast_choice in ('1', '2', '3'):

        if contrast_choice == '1':

            # increasing the contrast of the image by specifying factor of 2

            contrast_enhancer = ImageEnhance.Contrast(im)

            inc_contrast = contrast_enhancer.enhance(2)

            # function to preview edited image is called

            edited_image_preview(inc_contrast)

        elif contrast_choice == '2':

            # decreasing the contrast of the image by specifying factor of 0.5

            contrast_decrease = ImageEnhance.Contrast(im)

            dec_contrast = contrast_decrease.enhance(0.5)

            # function to preview edited image is called

            edited_image_preview(dec_contrast)

        elif contrast_choice == '3':

            # function to load main menu is called

            main()

    else:
        print("=====!!! PLEASE CHOOSE FROM SPECIFIED OPTIONS !!!=====")

        '''
        if the user won't chose from the specified options, this function will
        be called again unless and until user chooses from specified options
        '''

        contrast()


'''
=============Function to show available filter options on CLI=================
'''


def filter_options():

    print("--> 1. Black And White")

    print("--> 2. Sepia")

    print("--> 3. Negative")

    print("--> 4. Rust")

    print("--> 5. Canary Yellow")

    print("--> 6. Dracula")

    print("--> 7. Mystic Meadows")

    print("--> 8. Back to main menu")


'''
=========Functions containing different RGB values for different filters=======
'''

'''
- these are the functions defined for different filters

- new_red, new_green, new_blue will store the modified
  r, g, b values of the image
'''

# function for black and white filter


def black_n_white(r, g, b):
    """
    changing r, g, b values according to filter
    and storing them in new_red, new_green, new_blue
    """

    new_red = (r + g + b) // 3

    new_green = (r + g + b) // 3

    new_blue = (r + g + b) // 3

    return new_red, new_green, new_blue


# function for sepia filter

def sepia(r, g, b):

    new_red = int((r * .393) + (g * .769) + (b * .189))

    new_green = int((r * .349) + (g * .686) + (b * .168))

    new_blue = int((r * .272) + (g * .534) + (b * .131))

    return new_red, new_green, new_blue


# function for negative filter

def negative(r, g, b):

    new_red = 255 - r

    new_green = 255 - g

    new_blue = 255 - b

    return new_red, new_green, new_blue


# function for rust filter

def rust(r, g, b):

    new_red = (r + g + b) // 2

    new_green = (r + g + b) // 4

    new_blue = (r + g + b) // 6

    return new_red, new_green, new_blue


# function for canary_yellow

def canary_yellow(r, g, b):

    new_red = r

    new_green = r + g*0

    new_blue = b

    return new_red, new_green, new_blue


# function for dracula filter

def dracula(r, g, b):

    new_red = (r + g + b) // 2

    new_green = g // 2

    new_blue = b // 2

    return new_red, new_green, new_blue


# function for mystic meadows filter

def mystic(r, g, b):

    new_red = r

    new_green = g

    new_blue = g + b*0

    return new_red, new_green, new_blue


'''
==========Function for the filter selection submenu==========
'''


def submenu_filters():
    # printing all filter options

    filter_options()

    # asking the user to choose a filter to apply

    filter_choice = input("Enter what filter would you "
                          "like to apply(1, 2, 3, 4, 5, 6, 7, 8 : ")

    if filter_choice in ('1', '2', '3', '4', '5', '6', '7', '8'):

        '''
        iterating over the pixels of the image
        present in y axis(height) and x axis(width)
        '''

        for pixel_y in range(height):

            for pixel_x in range(width):

                '''
                loading rgb values of pixels at
                x and y coordinates into r, g, b
                '''

                r, g, b = im.getpixel((pixel_x, pixel_y))

                if filter_choice == '1':

                    # function to apply black and white filter is called

                    pixels[pixel_x, pixel_y] = black_n_white(r, g,
                                                             b)
                elif filter_choice == '2':

                    # function to apply sepia filter is called

                    pixels[pixel_x, pixel_y] = sepia(r, g, b)

                elif filter_choice == '3':

                    # function to apply negative filter is called

                    pixels[pixel_x, pixel_y] = negative(r, g, b)

                elif filter_choice == '4':

                    # function to apply rust filter is called

                    pixels[pixel_x, pixel_y] = rust(r, g, b)

                elif filter_choice == '5':

                    # function to apply canary yellow filter is called

                    pixels[pixel_x, pixel_y] = canary_yellow(r, g,
                                                             b)

                elif filter_choice == '6':

                    # function to apply dracula filter is called

                    pixels[pixel_x, pixel_y] = dracula(r, g, b)

                elif filter_choice == '7':

                    # function to apply mystic meadows filter is called

                    pixels[pixel_x, pixel_y] = mystic(r, g, b)

                elif filter_choice == '8':

                    # for going back to main menu main function is called

                    main()

        # to view and save the edited image edited_image_preview is called

        edited_image_preview(im)

    else:

        print("=====!!! PLEASE CHOOSE FROM SPECIFIED OPTIONS !!!=====")

        '''
         if the user won't chose from the specified options,
         this function will be called again unless and until
         user chooses from specified options
        '''
        submenu_filters()


'''
====================== MAIN MENU =========================
'''


def main():

    while True:

        # showing list of operations to be performed on the image onto the CLI

        home()

        choice = input("Choose the action you want to "
                       "take (1,2,3,4,5,6,7,8,9) : ")

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):

            if choice == '1':
                flip()

            if choice == '2':
                rotate_90()

            if choice == '3':
                rotate_180()

            if choice == '4':
                blur()

            if choice == '5':
                embossing()

            if choice == '6':
                submenu_filters()

            if choice == '7':
                contrast()

            if choice == '8':
                sharpen()

            if choice == '9':

                # final message as the program is closed

                print("Thanks for using Image editor")

                sys.exit()  # terminates the program

        else:

            print("=====!!! PLEASE CHOOSE FROM SPECIFIED OPTIONS !!!=====")

            main()


'''======================================================================'''

print("=" * 22 + "IMAGE EDITOR SCRIPT" + "=" * 22)

print("==INSTRUCTIONS==")

print(" # Welcome to the image editing script.")

print(" # Start by entering the path of the image to be edited")

print(" # The path must include the image name along with the extension.")

print(" # Choose from the given editing options.")

print(" # Save the image by specifying the path and the new image name "
      "along with extension.")

print(" ")

print("="*50)

# Taking path of image from the user

image_input = input(r"Enter the path of the image to be edited : ")

# creating an image object im

# converting image into RGB and loading it into im

im = Image.open(image_input).convert("RGB")

# im.size stores the width and height of the image in the tuple

width, height = im.size

pixels = im.load()

# Calling main function

main()

'''=========================================================='''

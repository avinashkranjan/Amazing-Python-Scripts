from PIL import Image, ImageEnhance

# ASCII characters used to build the output text
char_ramp = []

# Choose character sequence for mapping
def set_char_ramp():
    global char_ramp
    print("Choose a Character Sequence!")
    print("1 - Basic")
    print("2 - Standard (Short)")
    print("3 - Standard (Long)")
    print("4 - Unicode Blocks")
    print("5 - Unicode Shades")
    print("6 - Enter Custom Sequence")
    choice = input("Input: ")

    try:
        choice = int(choice)
    except Exception:
        print("Invalid Input!")
        exit()

    if choice == 1:
        char_ramp = list("00011111...")
    elif choice == 2:
        char_ramp = list("@%#*+=-:. ")
    elif choice == 3:
        char_ramp = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1}{[]?-_+~<>i!lI;:,\"^`'. ")
    elif choice == 4:
        char_ramp = ["█", "▉", "▊", "▋", "▌", "▍", "▎", "▏"]
    elif choice == 5:
        char_ramp = ["█", "▓", "▒", "░", " "]
    elif choice == 6:
        custom_ramp = input("Enter your Character Sequence from High density to Low: ")
        if len(custom_ramp) == 0:
            print("Invalid Input!")
            exit()
        char_ramp = list(custom_ramp)
    else:
        print("Invalid Input!")
        exit()


# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image, contrast_factor):
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    pixels = image.getdata()
    characters = " ".join([char_ramp[int((pixel/256)*len(char_ramp))] for pixel in pixels])
    return(characters)

# Driver function
def photoascii():
    # Attempt to open image file from user-input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)
    except Exception:
        print("Invalid Path!")
        exit()
    
    contrast_factor = input("Enter contrast factor (1 = Original Contrast) [Note: Enter negative value to invert output] : ")
    try:
        contrast_factor = float(contrast_factor)
    except Exception:
        print("Invalid Input!")
        exit()
    
    set_char_ramp()
    
    if contrast_factor < 0:
        global char_ramp
        char_ramp.reverse()
        contrast_factor = -contrast_factor
    
    # Fetch the name of the image file
    dot_index = path.rfind('.')
    slash_index = path.rfind('\\')
    if slash_index == -1:
        slash_index = path.rfind('/')
    image_name = path[slash_index+1:dot_index] + "_" + path[dot_index+1:]
    
    # Resize image
    new_width = 100
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    
    # Convert image to ASCII
    new_image_data = pixels_to_ascii(resized_image, contrast_factor)
    pixel_count = len(new_image_data)
    scanline_width = new_width * 2;
    ascii_image = "\n".join([new_image_data[index:(index+scanline_width)]
                            for index in range(0, pixel_count, scanline_width)])
    
    # Save result to text file
    with open(path[:slash_index] + "/{}_ASCII.txt".format(image_name), "w", encoding='utf8') as f:
        f.write(ascii_image)


# Run Program
if __name__ == '__main__':
    photoascii()

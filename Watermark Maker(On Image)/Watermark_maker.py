# Import required Image library
from PIL import Image, ImageDraw, ImageFont

# Taking Input From user
path = input("Input the path of the image: ")
path = path.strip('""')
im = Image.open(path)
width, height = im.size

# Taking input for the text
text = input('Enter the text for the watermark: ')
font = ImageFont.truetype('arial.ttf', 20)

# Taking Input For the Position of the text
print("To Specify the position of the text , enter a number between 1 to 5.\n")
print("Enter\n 1 for Top Left \n 2 for Top Right \n 3 for Bottom Left \n 4 for Bottom Right \n 5 for Center")
pos = int(input())


# resize the image and
# upscaling quality
re_width = 500
re_height = 500
# The image upscaling quality
r_img = im.resize((re_width, re_height), Image.LANCZOS)
r_img.size

# textwrap the lines


def text_wrap(text, font, max_width):
    lines = []

    # If the text width is smaller than the image width, then
    # no need to split
    # just add it to the line list and return

    if font.getsize(text)[0] <= max_width:
        lines.append(text)

    else:
        # split the line on the basis of spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines


max_x = 250
lines = text_wrap(text, font, max_x)
# calculating the max height that a text can have
line_height = font.getsize('hg')[1]

# setting the x,y values for different positions
x_min = (r_img.size[0] * 5) // 100
if font.getsize(text)[0] < max_x:
    x_max = (r_img.size[0] - font.getsize(text)[0]) + 10

else:
    x_max = (r_img.size[0] * 50) // 100


# For image at top
y_min = (r_img.size[1] * 4) // 100
# For Image at Bottom
y_max = (r_img.size[1] * 97) // 100
y_max -= (len(lines)*line_height)


if pos == 1:
    x_start = x_min
    y_start = y_min

elif pos == 2:
    x_start = x_max
    y_start = y_min

elif pos == 3:
    x_start = x_min
    y_start = y_max

elif pos == 4:
    x_start = x_max
    y_start = y_max

else:
    x_start = (r_img.size[0] * 40) // 100
    y_start = (r_img.size[0] * 50) // 100


draw = ImageDraw.Draw(r_img)

# x coordinate and y coordinate for the text position
x = x_start
y = y_start

for line in lines:

    draw.text((x, y), line, fill='rgb(255,255,255)', font=font)

    y = y + line_height

r_img.show()

# Save watermarked image
r_img.save('Test_Image.png')

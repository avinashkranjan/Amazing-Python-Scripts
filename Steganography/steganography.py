
from cv2 import cv2
import math
import argparse

parser = argparse.ArgumentParser(description="Steganography of text in image")
parser.add_argument("image", type=str, metavar="", help="Path of Image File")
group1 = parser.add_mutually_exclusive_group()
group2 = parser.add_mutually_exclusive_group()
group1.add_argument("-e", "--encode", action="store_true", help="Encode Image")
group2.add_argument("-d", "--decode", action="store_true", help="Decode Image")
group2.add_argument("-o", help="Encoded Image Nmae",
                    default="Encoded_image.png")
group1.add_argument("-t", help="Output in Text File", default=False)


def encode(path_image, data):
    img = cv2.imread(path_image)
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape

    Pixal = len(data) * 3
    print("[*] Required pixels are ", Pixal)

    Row = Pixal/width
    Row = math.ceil(Row)

    count = 0
    charCount = 0
    print("[*] Encoding Data.......")
    for i in range(Row + 1):
        while (count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            for index_k, k in enumerate(char):
                if ((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if (index_k % 3 == 2):
                    count += 1
                if (index_k == 7):
                    if (charCount*3 < Pixal and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if (charCount*3 >= Pixal and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0

    return img


def decode(path_image):
    img = cv2.imread(path_image)
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if ((index_j) % 3 == 2):
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                if (bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                data.append(bin(j[2])[-1])
        if (stop):
            break

    message = []
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    return message


def encode_image(image_path, message, Output):
    img = encode(image_path, message)
    cv2.imwrite(Output, img)
    print("[*] Data Encoded in ", Output)


def decode_image(image_path, textfile):
    print("[*] Decoding Message...... ")
    msg = decode(image_path)
    print("[*] Message decoded ..")
    if textfile:
        with open(textfile, "w") as f:
            f.write(msg)
    else:
        print(msg)


if __name__ == "__main__":
    args = parser.parse_args()
    if not (args.encode or args.decode):
        parser.error('No action requested, add --encode or --decode')

    if args.encode:
        msg = input("[*] Input Message: ")
        encode_image(args.image, msg, args.o)

    elif args.decode:
        decode_image(args.image, args.t)

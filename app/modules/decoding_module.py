from PIL import Image
import numpy as np
import cv2
import os


def decode_text_from_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    binary_text = ''
    for row in range(height):
        for col in range(width):
            pixel = pixels[col, row]
            for n in range(3):  # Process each color channel
                binary_text += str(pixel[n] & 1)

    # Convert the binary text back to characters
    characters = [chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)]
    decoded_text = ''.join(characters)
    delimiter_index = decoded_text.find('\x00' * 8)  # Find the sequence of eight null characters

    if delimiter_index != -1:
        decoded_text = decoded_text[:delimiter_index]
    return decoded_text

def decode_image_to_text(image_path):
    text = decode_text_from_image(image_path)
    # print
    return text
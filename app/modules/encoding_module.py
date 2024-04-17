import os
from PIL import Image

import numpy as np
import cv2
import os

# app.config['ENCODED_IMAGES'] = 'path/to/static/encoded'

def load_and_preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Resize image to (224, 224)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
    img = img.astype('float32') / 255.0  # Normalize pixel values to [0, 1]
    return img

def encode_text_into_image(preprocessed_img, text, output_path,output_directory):
    # Load the image
    img = Image.fromarray((preprocessed_img * 255).astype('uint8'))
    encoded_img = img.copy()
    width, height = img.size
    index = 0
    
 # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_text += '00000000' * 8  # Adding an 8-byte (64 bit) delimiter of null bytes

    # Ensure the image can hold the binary text
    if len(binary_text) > width * height * 3:
        raise ValueError("Text is too long to be hidden in the image.")

    pixels = encoded_img.load()

    for row in range(height):
        for col in range(width):
            pixel = list(pixels[col, row])
            for n in range(3):  # Process each color channel
                if index < len(binary_text):
                    pixel[n] = pixel[n] & ~1 | int(binary_text[index], 2)
                    index += 1
                else:
                    break
            if index >= len(binary_text):
                break
            pixels[col, row] = tuple(pixel)
        if index >= len(binary_text):
            break

    file_name = os.path.basename(output_path)
    add_png = os.path.splitext(file_name)[0] + "enc" + ".png"
    save_path = os.path.join(output_directory, add_png)
    encoded_img.save(save_path, format='PNG')
    return add_png


# def encode_text_into_image(preprocessed_img, text, output_path,output_directory):
#     encoded_img = Image.fromarray((preprocessed_img * 255).astype('uint8'))  # Convert back to a PIL image
#     binary_text = ''.join(format(ord(char), '08b') for char in text)
#     binary_text += '1111111111111110'  # Delimiter for end of text

#     data_index = 0
#     for row in range(encoded_img.height):
#         for col in range(encoded_img.width):
#             if data_index < len(binary_text):
#                 pixel = list(encoded_img.getpixel((col, row)))
#                 for n in range(3):  # Process each color channel
#                     if data_index < len(binary_text):
#                         pixel[n] = pixel[n] & ~1 | int(binary_text[data_index])
#                         data_index += 1
#                 encoded_img.putpixel((col, row), tuple(pixel))

#     # encoded_img.save(output_path, format='PNG')
#     file_name = os.path.basename(output_path)
#     add_png = os.path.splitext(file_name)[0] + "enc" + ".png"
#     save_path = os.path.join(output_directory, add_png)
#     encoded_img.save(save_path, format='PNG')
#     return add_png


def encode_text_in_image(image_path, text, save_directory):
    # Load the image
    img = Image.open(image_path)

    file_name = os.path.basename(image_path)
    add_png = os.path.splitext(file_name)[0] + ".png"
    save_path = os.path.join(save_directory, add_png)

    # Save the processed image
    img.save(save_path,"PNG")

    preprocessed_img = load_and_preprocess_image(save_path)
    img_name = encode_text_into_image(preprocessed_img, text, save_path,save_directory)



    return img_name

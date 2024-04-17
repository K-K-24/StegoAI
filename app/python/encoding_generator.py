import tensorflow as tf
import numpy as np
import cv2
import os
from PIL import Image

import gensim.downloader as api
from nltk.tokenize import word_tokenize
import numpy as np

import numpy as np
import cv2
import os



# Function to convert text to embedding
def text_to_embedding(text, embedding_size=128):
    # Load pre-trained Word2Vec model
    w2v_model = api.load('word2vec-google-news-300')
    # Tokenize the text
    tokens = word_tokenize(text)

    # Initialize an empty list to store word vectors
    word_vectors = []

    # Iterate over tokens and get their word vectors
    for token in tokens:
        try:
            # Get the word vector for the token
            word_vector = w2v_model[token]
            word_vectors.append(word_vector)
        except KeyError:
            # Ignore tokens not found in the vocabulary
            pass

    # Average the word vectors to get the text embedding
    if word_vectors:
        text_embedding = np.mean(word_vectors, axis=0)
    else:
        # If no word vectors found, use zeros
        text_embedding = np.zeros((embedding_size,))

    # Pad or truncate the embedding to have the desired size
    if len(text_embedding) < embedding_size:
        text_embedding = np.pad(text_embedding, ((0, embedding_size - len(text_embedding))), mode='constant')
    elif len(text_embedding) > embedding_size:
        text_embedding = text_embedding[:embedding_size]

    # Reshape to match the desired shape (1, 128)
    text_embedding = text_embedding.reshape((1, embedding_size))

    return text_embedding


def generate_embedded_image(model_path, image_path, text_embedding,output_path,output_directory):

    generator = tf.keras.models.load_model(model_path)
    
    input_img = load_and_preprocess_image(image_path)
    input_img = np.expand_dims(input_img, axis=0)  # Add batch dimension
    

    
    # Generate the embedded image
    embedded_img = generator.predict([input_img, text_embedding])
    
    # Convert the output from float to uint8 type and scale back to [0, 255]
    embedded_img = np.clip(embedded_img[0] * 255, 0, 255).astype(np.uint8)

    file_name = os.path.basename(output_path)
    add_png = os.path.splitext(file_name)[0] + "enc" + ".png"
    save_path = os.path.join(output_directory, add_png)
    embedded_img.save(save_path, format='PNG')
    return add_png
    

def load_and_preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
    img = img.astype('float32') / 255.0  
    return img


def encode_text_in_image(image_path, text, save_directory):
    img = Image.open(image_path)
    file_name = os.path.basename(image_path)
    add_png = os.path.splitext(file_name)[0] + ".png"
    save_path = os.path.join(save_directory, add_png)

    # Save the processed image
    img.save(save_path,"PNG")

    model_path = 'models/generator_w.h5'
    image_path = 'path_to_your_image.jpg'
    text_embedding = text_to_embedding(text)

    img_name = generate_embedded_image(model_path, image_path, text_embedding,save_path,save_directory)
    return img_name

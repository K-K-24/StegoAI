import tensorflow as tf

def decode_text_from_image(image_path):
    decoder = tf.keras.models.load_model('models/decoder.h5')
    decoded_predictions = decoder.predict(image_path)

    return decoded_predictions
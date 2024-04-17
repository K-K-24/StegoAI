from flask import Flask, render_template, request, send_file,jsonify
from werkzeug.utils import secure_filename
import os
from modules.encoding_module import encode_text_in_image
from modules.decoding_module import decode_image_to_text

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ENCODED_IMAGES'] = 'static/encoded'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        file = request.files['inputImage']
        text = request.form['inputText']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Call your encoding function here
            encoded_image_name = encode_text_in_image(file_path, text, app.config['ENCODED_IMAGES'])
            return jsonify({'encodedImagePath': encoded_image_name})
            # print(encoded_image_path)
            # return send_file(encoded_image_path, mimetype='image/png')
    return render_template('encode.html')


@app.route('/decode', methods=['GET','POST'])
def decode():
    if request.method == 'POST':
        file = request.files['inputImage']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Call your decoding function which should return the decoded text
            decoded_text = decode_image_to_text(file_path)
            return jsonify({'decodedText': decoded_text})
    return render_template('decode.html')

if __name__ == '__main__':
    app.run(debug=True)

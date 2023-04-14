from flask import Flask, request
from werkzeug.utils import secure_filename
import os, random, piexif, string

app = Flask(__name__)

url = "http://127.0.0.1:9900/static/Keira/"
upload_folder = os.getcwd() + "/static/Keira/"
exif_remove_types = [".jpg", ".jpeg", ".jpe"]

@app.route('/')
def home():
    return "403", 403

# definitely protect this with htaccess or something
@app.route('/u', methods=['POST'])
def do_upload():
    if request.method == 'POST':
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        if 'file' not in request.files:
            return "No file selected."
        file = request.files['file']
        if file.filename == '':
            return "No file selected."
        if file:
            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            newname = ''.join(random.sample("-_"+string.ascii_uppercase+string.ascii_lowercase+string.digits,20)) + extension
            file.save(os.path.join(upload_folder, newname))
            if extension in exif_remove_types:
                piexif.remove(upload_folder + newname)
            response = newname
        return url + response
    return "Request error"
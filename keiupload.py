from flask import Flask, request
from werkzeug.utils import secure_filename
import os, random, piexif, string

app = Flask(__name__)

@app.route('/')
def home():
    return "403", 403

# definitely protect this with htaccess or something
@app.route('/u', methods=['POST'])
def do_upload():
    if request.method == 'POST':
        url = "http://127.0.0.1:9900/static/Keira/"
        upload_folder = os.getcwd() + "/static/Keira/"
        exif_remove_types = [".jpg", ".jpeg", ".jpe"]

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

            if request.values.get('randomize_filename') and request.values.get('randomize_filename') is '1':
                f_name, f_ext = os.path.splitext(os.path.basename(filename).split("/")[-1])
                filename = ''.join(random.sample("-_"+string.ascii_uppercase+string.ascii_lowercase+string.digits,20)) + '.' + f_name + f_ext

            if request.values.get('path'):
                folder_subpath = ""
                if request.values.get('path') != "":
                    folder_subpath = secure_filename(request.values.get('path')) + '/'
                else:
                    folder_subpath = ''.join(random.sample("-_"+string.ascii_uppercase+string.ascii_lowercase+string.digits,20)) + '/'
                upload_folder = upload_folder + folder_subpath
                
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            file.save(os.path.join(upload_folder, filename))

            if not request.values.get('keep_exif'):
                if extension in exif_remove_types:
                    piexif.remove(upload_folder + filename)

            if request.values.get('path'):
                response = folder_subpath + filename
            else:
                response = filename
        return url + response
    return "Request error"
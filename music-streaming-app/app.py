from flask import Flask, request, send_from_directory, jsonify, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return redirect(url_for('upload_page'))

@app.route('/upload_page')
def upload_page():
    return render_template('upload.html')

@app.route('/player_page')
def player_page():
    songs = os.listdir(UPLOAD_FOLDER)
    return render_template('player.html', songs=songs)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file and file.filename.endswith('.mp3'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully"}), 200
    return jsonify({"error": "Invalid file format"}), 400

@app.route('/songs')
def list_songs():
    songs = os.listdir(UPLOAD_FOLDER)
    return jsonify(songs)

@app.route('/play/<filename>')
def play_song(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
from main import process_audio

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio_route():
    if 'audio' in request.files:
        audio_file = request.files['audio']
    elif 'url' in request.form:
        url = request.form['url']
        audio_file = download_file(url)
    else:
        return "No audio file or URL provided", 400
    output_file = process_audio(audio_file)
    return redirect(url_for('processing_complete')), 200

@app.route('/list_audio', methods=['GET'])
def list_audio():
    audio_files = get_processed_audio_files()
    return jsonify(audio_files), 200

if __name__ == '__main__':
    app.run(threaded=True)

from flask import Flask, request, redirect, url_for, jsonify
from main import process_audio

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio_route():
    audio_file = request.files['audio']
    if audio_file.startswith('http'):
        audio_file = download_file(audio_file)
    output_file = process_audio(audio_file)
    return redirect(url_for('notification'))

def get_processed_audio_files():
    # Implementation to list all finished processed audio files
    pass

@app.route('/list_audio', methods=['GET'])
def list_audio():
    audio_files = list_audio()
    for audio_file in audio_files:
        os.remove(audio_file)
    return jsonify(audio_files)
    
if __name__ == '__main__':
    app.run(threaded=True)

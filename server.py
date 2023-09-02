from flask import Flask, request
from main import process_audio

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio_route():
    audio_file = request.files['audio']
    output_file = process_audio(audio_file)
    return output_file, 200

if __name__ == '__main__':
    app.run(threaded=True)

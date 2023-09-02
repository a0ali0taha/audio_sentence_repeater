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

@app.route('/list_audio', methods=['GET'])
def list_audio():
    audio_files = get_processed_audio_files()
    for audio_file in audio_files:
        os.remove(audio_file)
    html_links = []
    for audio_file in audio_files:
        file_name = os.path.basename(audio_file)
        file_link = f'<a href="{audio_file}" download>{file_name}</a>'
        html_links.append(file_link)
    return '\n'.join(html_links)

if __name__ == '__main__':
    app.run(threaded=True)

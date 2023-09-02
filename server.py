
def download_file(audio_file):
    import requests
    import os

    response = requests.get(audio_file)
    file_name = audio_file.split('/')[-1]
    file_path = os.path.join('downloads', file_name)

    with open(file_path, 'wb') as file:
        file.write(response.content)

    return file_path

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
    return jsonify(audio_files)

if __name__ == '__main__':
    app.run(threaded=True)

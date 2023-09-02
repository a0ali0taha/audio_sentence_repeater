
def process_audio(input_file, output_file, downloaded=False):
    from conacat import duplicate_and_concatenate_audio
    import os
    import subprocess
    import time
    from ffrepeater import split
    audio_name = os.path.basename(input_file).replace('.mp3','')

    splited_folder=f"splt_folder/{round(time.time())}"
    command = f'mkdir "{splited_folder}"'
    subprocess.run(command, shell=True)
    split(splited_folder,input_file)
    duplicate_and_concatenate_audio(splited_folder,output_file)
    if downloaded:
        os.remove(input_file)
    return "Audio processing complete."
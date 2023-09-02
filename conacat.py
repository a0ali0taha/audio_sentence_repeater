import subprocess
import os
from slowdown import slow_down
def add_silent(output_file):
    command = f'cat silent.mp3 >> "{output_file}"'
    subprocess.run(command, shell=True)

def add_slow(input_path,output_file):
    command = f'cat "{slow_down(input_path)}" >> "{output_file}"'
    subprocess.run(command, shell=True)

def duplicate_and_concatenate_audio(input_folder, output_file, loop=3):
    audio_files = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]
    audio_files.sort()
    for audio_file in audio_files:
        audio_path = os.path.join(input_folder, audio_file)
        i=0
        for _ in range(loop):
            add_silent(output_file)
            if i==1:
                add_slow(audio_path,output_file)
            else:
                command = f'cat "{audio_path}" >> "{output_file}"'
                subprocess.run(command, shell=True)
            i+=1



    print("Concatenation complete.")

if __name__ == "__main__":
    input_folder = 'splt_folder/1693541192'
    output_file = '111.mp3'
    duplicate_and_concatenate_audio(input_folder, output_file)
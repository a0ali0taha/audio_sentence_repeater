
from conacat import duplicate_and_concatenate_audio
import os
import subprocess
import time
from ffrepeater import split
input_file="downloads/577_Casey_Muratori_Clean_Code_Horrible_Performance.mp3"
audio_name = os.path.basename(input_file).replace('.mp3','')

splited_folder=f"splt_folder/{round(time.time())}"
command = f'mkdir "{splited_folder}"'
subprocess.run(command, shell=True)
split(splited_folder,input_file)
duplicate_and_concatenate_audio(splited_folder,f'out/{audio_name} RB.mp3')
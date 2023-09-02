import subprocess
def slow_down(input):
    output=input.replace('.mp3','slow.mp3')
    command = f'ffmpeg -i {input} -filter:a "atempo=0.75" {output}'
    subprocess.run(command, shell=True)
    return output
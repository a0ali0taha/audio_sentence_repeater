import subprocess
import os
def split(splt_folder,input_audio):
    output_template = f'{splt_folder}/output_%03d.mp3'

    ffmpeg_command = [
        'ffmpeg',
        '-i', input_audio,
        '-af', 'silencedetect=noise=-30dB:d=0.3',
        '-f', 'null', '-'
    ]

    output = subprocess.check_output(ffmpeg_command, stderr=subprocess.STDOUT)

    silence_segments = []
    silence_segments.append(0.0)
    p = 1
    for line in output.decode().splitlines():
        if 'silence_start' in line:
            start_time = float(line.split('silence_start: ')[1].split()[0])
            if start_time-silence_segments[p-1]>3:
                silence_segments.append(start_time)
                p+=1

    # segment_files = [output_template % i for i in range(len(silence_segments))]

    for i, start_time in enumerate(silence_segments):
        end_time = silence_segments[i + 1] if i < len(silence_segments) - 1 else None
        output_file = output_template % i
        ffmpeg_command = [
            'ffmpeg',
            '-i', input_audio,
            '-ss', str(start_time),
            '-to', str(end_time) if end_time else 'end',
            '-c:a', 'copy',
            output_file
        ]
        subprocess.run(ffmpeg_command)


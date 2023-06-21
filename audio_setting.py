import os
import shutil
import wave
from datetime import datetime


# 아래는 1초에서 5초 사이의 음성들을 dst_foler에 저장하는 코드입니다.
def get_duration(wav_file):
    with wave.open(wav_file, 'r') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


src_folder = 'C:/Users/roista/Downloads/kss'
dst_folder = 'C:/Users/roista/Downloads/kss_set'
copied_files = []

# create destination folder if not exists
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)


for dirpath, dirnames, filenames in os.walk(src_folder):
    for filename in filenames:
        if filename.endswith('.wav'):
            src_file = os.path.join(dirpath, filename)
            duration = get_duration(src_file)
            if 1 <= duration <= 5:
                # maintain the folder structure
                structure = os.path.join(dst_folder, os.path.relpath(dirpath, src_folder))
                if not os.path.isdir(structure):
                    os.mkdir(structure)
                dst_file = os.path.join(structure, filename)
                shutil.copy2(src_file, dst_file)
                copied_files.append(os.path.join(os.path.relpath(dirpath, src_folder), filename))

# get current time
now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")

# use the current time in the output file name
with open(os.path.join(dst_folder, 'file-{}.txt'.format(timestamp)), 'w') as f:
    for file_name in copied_files:
        f.write("%s\n" % file_name)

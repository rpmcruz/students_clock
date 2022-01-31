import argparse
parser = argparse.ArgumentParser()
parser.add_argument('start', nargs='?', type=int, default=0)
args = parser.parse_args()

from unidecode import unidecode
import yaml
import os

students = yaml.safe_load(open('videos.yaml'))
students = sorted(students, key=lambda x: unidecode(x['name']))

for i in range(args.start, len(students)):
    print(f'***************** {i+1}/{len(students)} *****************')
    student = students[i]
    os.system(f"python3 video-title.py \"{student['title']}\" \"{student['name']}\"")
    os.system(f"vlc -f videos/{student['nmec']}.mp4 vlc://quit")
    next = students[i+1]['name'] if i+1 < len(students) else ''
    os.system(f"python3 video-end.py \"{student['name']}\" \"{next}\"")

os.system(f"python3 video-title.py \"THE END\" \"Obrigado pela vossa presença.\"")

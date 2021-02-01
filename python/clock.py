#!/usr/bin/python3
# Runs the students Python projects, with a clock, automatically moves
# to the next project.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('yaml_file')
parser.parse_args()

import tkinter as tk
from PIL import Image, ImageTk
import subprocess, os
import yaml

d = yaml.load(open(args.yaml_file))

names = d['names'].split('\n')
images = d['images'].split('\n')
commands = d['commands'].split('\n')
assert len(names) == len(images), f'names: {len(names)}, images: {len(images)}'
assert len(names) == len(commands), f'names: {len(names)}, commands: {len(commands)}'

root = tk.Tk()
root.configure(background='black')

proc = None
start_new_id = None
current = 0
remaining = 2*60+10

def prep_name(name):
    return name.split()[0] + ' ' + name.split()[-1]

def prev(event=None):
    global current, remaining
    if current > 0:
        remaining = 2*60+11
        current -= 1
        sync()

def next(event=None):
    global current, remaining
    if current < len(names)-1:
        remaining = 2*60+11
        current += 1
        sync()
    else:
        global proc
        if proc:
            proc.kill()
            proc = None

def timer(event=None):
    global remaining
    remaining -= 1
    if remaining < 0:
        remaining = 2*60+10
        next()
    time.configure(text='%02d:%02d' % (remaining//60, remaining%60))
    time.configure(fg='red' if remaining <= 10 else 'white')
    root.after(1000, timer)

def sync():
    global proc, start_new_id
    img = Image.open(images[current])
    img = img.resize((600, 400))  # thumbnail
    img = ImageTk.PhotoImage(img)
    photo.configure(image=img)
    photo.img = img
    label.configure(text=prep_name(names[current]))
    next_txt = 'Depois: ' + prep_name(names[current+1]) if current < len(names)-1 else ''
    next_label.configure(text=next_txt)
    if proc:
        proc.kill()
        proc = None
    if start_new_id:
        root.after_cancel(start_new_id)
    start_new_id = root.after(5*1000, start_new)

def start_new():
    global proc
    cmd = commands[current]
    proc = subprocess.Popen(['python3', os.path.basename(cmd)], cwd=os.path.dirname(cmd))

root.bind_all('<Left>', prev)
root.bind_all('<Right>', next)
root.after(1000, timer)
root.title('')

photo = tk.Label(root)
photo.pack()

label = tk.Label(root, text='', font=('Helvetica', 32), bg='black', fg='white')
label.pack()

time = tk.Label(root, text='02:10', font=('Helvetica', 32), bg='black', fg='white')
time.pack()

next_label = tk.Label(root, text='', font=('Helvetica', 16), bg='black', fg='white')
next_label.pack()

sync()

tk.mainloop()

import os
from subprocess import Popen, PIPE
from tkinter import *


def btn_clicked():
    print("Button Clicked")


def assistant_ok(p):
    p.communicate(input='\n')


def end():
    exit(0)


window = Tk()

os.system('cd ~/')
os.system('/bin/bash -c "source env/bin/activate"')
a = Popen(['googlesamples-assistant-pushtotalk --credentials /home/cd52022/.config/google-oauthlib-tool/credentials.json'], stdin=PIPE, shell=True)


window.geometry("480x320")
window.configure(bg="#363636")
canvas = Canvas(
    window,
    bg="#363636",
    height=320,
    width=480,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    808.0, 511.5,
    image=background_img)

img0 = PhotoImage(file=f"vol-.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=18, y=867,
    width=48,
    height=48)

img1 = PhotoImage(file=f"vol+.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

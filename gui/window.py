import os
from tkinter import *


def btn_clicked():
    print("Button Clicked")


def assistant():
    os.system('googlesamples-assistant-pushtotalk --credentials /home/cd52022/.config/google-oauthlib-tool/credentials.json')


def end():
    exit(0)


window = Tk()

window.geometry("1440x1024")
window.configure(bg="#363636")
canvas = Canvas(
    window,
    bg="#363636",
    height=1024,
    width=1440,
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

b1.place(
    x=18, y=666,
    width=48,
    height=48)

img2 = PhotoImage(file=f"back.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b2.place(
    x=18, y=464,
    width=48,
    height=48)

img3 = PhotoImage(file=f"home.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b3.place(
    x=18, y=280,
    width=48,
    height=48)

quit = PhotoImage(file=f"quit.png")
b4 = Button(
    image=quit,
    borderwidth=0,
    highlightthickness=0,
    command=end,
    relief="flat")


b4.place(
    x=18, y=96,
    width=48,
    height=48)

img5 = PhotoImage(file=f"assistant.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=assistant,
    relief="flat")

b5.place(
    x=1052, y=501,
    width=189,
    height=217)

img6 = PhotoImage(file=f"config.png")
b6 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b6.place(
    x=310, y=512,
    width=163,
    height=206)

img7 = PhotoImage(file=f"radio.png")
b7 = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b7.place(
    x=1154, y=135,
    width=141,
    height=198)

img8 = PhotoImage(file=f"maps.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b8.place(
    x=824, y=115,
    width=169,
    height=218)

img9 = PhotoImage(file=f"bluetooth.png")
b9 = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b9.place(
    x=525, y=142,
    width=178,
    height=191)

img10 = PhotoImage(file=f"celular.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b10.place(
    x=224, y=107,
    width=207,
    height=223)

window.resizable(False, False)
window.mainloop()

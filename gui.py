import os
from subprocess import Popen, PIPE
from PIL import Image, ImageTk
from tkinter import Tk, Canvas, PhotoImage, Button


def assets(path):
    return Image.open("assets/" + path).convert("RGBA")


def google_assistant():
    pass


def end():
    exit(0)


window = Tk()
os.system('cd ~/')
os.system('/bin/bash -c "source env/bin/activate"')
Popen(['googlesamples-assistant-pushtotalk --credentials /home/cd52022/.config/google-oauthlib-tool/credentials.json'],
          stdin=PIPE, shell=True)

window.geometry("480x320")
window.configure(bg="#363636")

canvas = Canvas(
    window,
    bg="#363636",
    height=320,
    width=480,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = ImageTk.PhotoImage(assets("image_1.png"))
image_1 = canvas.create_image(
    240.0,
    160.0,
    image=image_image_1
)

button_image_1 = ImageTk.PhotoImage(assets("vol-.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=8.0,
    y=279.0,
    width=26.307693481445312,
    height=26.307693481445312
)

button_image_2 = ImageTk.PhotoImage(assets("vol+.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=8.0,
    y=213.0,
    width=26.307693481445312,
    height=26.307693481445312
)

button_image_3 = ImageTk.PhotoImage(assets("return.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=8.0,
    y=147.0,
    width=26.307693481445312,
    height=26.307693481445312
)

button_image_4 = ImageTk.PhotoImage(assets("home.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=8.0,
    y=81.0,
    width=26.307693481445312,
    height=26.307693481445312
)

close = ImageTk.PhotoImage(assets("close.png"))
close_btn = Button(
    image=close,
    borderwidth=0,
    highlightthickness=0,
    command=end,
    relief="flat"
)
close_btn.place(
    x=8.0,
    y=15.0,
    width=26.307693481445312,
    height=26.30769157409668
)

assistant = ImageTk.PhotoImage(assets("assistant.png"))
assistant_btn = Button(
    image=assistant,
    borderwidth=0,
    highlightthickness=0,
    command=google_assistant,
    relief="flat"
)
assistant_btn.place(
    x=336.0,
    y=193.0,
    width=87.0,
    height=66.0
)

button_image_7 = ImageTk.PhotoImage(assets("help.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=240.0,
    y=195.0,
    width=51.0,
    height=64.0
)

button_image_8 = ImageTk.PhotoImage(assets("settings.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=128.0,
    y=194.0,
    width=67.0,
    height=62.0
)

button_image_9 = ImageTk.PhotoImage(assets("bluetooth.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=171.0,
    y=69.0,
    width=89.0,
    height=65.0
)

button_image_10 = ImageTk.PhotoImage(assets("radio.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=395.0,
    y=69.0,
    width=46.0,
    height=65.0
)

button_image_11 = ImageTk.PhotoImage(assets("telephone.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=70.0,
    y=70.0,
    width=71.0,
    height=58.0
)

button_image_12 = ImageTk.PhotoImage(assets("maps.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=290.0,
    y=53.0,
    width=74.76275634765625,
    height=77.0
)


#window.attributes("-fullscreen", True)
window.resizable(False, False)
window.mainloop()

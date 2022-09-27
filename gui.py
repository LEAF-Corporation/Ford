import os
from subprocess import Popen, PIPE
from PIL import Image, ImageTk
import tkinter as tk


class CanvasButton:
    flash_delay = 100

    def __init__(self, canvas, x, y, image_path, command, state=tk.NORMAL):
        self.canvas = canvas
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state,
                                                      image=self.btn_image)
        canvas.tag_bind(self.canvas_btn_img_obj, '<ButtonRelease-1>',
                        lambda event: (self.flash(), command()))

    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)


def assets(path):
    return Image.open("assets/" + path).convert("RGBA")


def google_assistant():
    Popen(['googlesamples-assistant-pushtotalk --credentials /home/cd52022/.config/google-oauthlib-tool/credentials.json'],
          stdin=PIPE, shell=True)


def end():
    exit(0)


window = tk.Tk()
os.system('cd ~/')
os.system('/bin/bash -c "source env/bin/activate"')

window.geometry('480x320')
window.configure(bg='#363636')

canvas = tk.Canvas(
    window,
    bg='#363636',
    height=320,
    width=480,
    bd=0,
    highlightthickness=0,
    relief='flat'
)

canvas.place(x=0, y=0)
image_image_1 = ImageTk.PhotoImage(assets('image_1.png'))
image_1 = canvas.create_image(
    240.0,
    160.0,
    image=image_image_1
)

vol_btn = CanvasButton(canvas, 6, 279, 'assets/vol-.png', end)
vol_btn2 = CanvasButton(canvas, 6, 213, 'assets/vol+.png', end)
return_btn = CanvasButton(canvas, 6, 147, 'assets/return.png', end)
home_btn = CanvasButton(canvas, 6, 81, 'assets/home.png', end)
close_btn = CanvasButton(canvas, 6, 15, 'assets/close.png', end)
assistant_btn = CanvasButton(canvas, 336, 193, 'assets/assistant.png', google_assistant)
help_btn = CanvasButton(canvas, 240, 195, 'assets/help.png', end)
settings_btn = CanvasButton(canvas, 128, 194, 'assets/settings.png', end)
bluetooth_btn = CanvasButton(canvas, 171, 69, 'assets/bluetooth.png', end)
radio_btn = CanvasButton(canvas, 395, 69, 'assets/radio.png', end)
telephone_btn = CanvasButton(canvas, 70, 70, 'assets/telephone.png', end)
maps_btn = CanvasButton(canvas, 305, 65, 'assets/maps.png', end)

# window.attributes('-fullscreen', True)
window.resizable(False, False)
window.mainloop()

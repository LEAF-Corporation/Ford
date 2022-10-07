import os
import subprocess as sub
from PIL import Image, ImageTk
import tkinter as tk
import pygame as pyg


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


class MyLabel(tk.Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        tk.Label.__init__(self, master, image=self.frames[0])

        lut = [1] * 256
        lut[im.info["transparency"]] = 0

        temp = seq[0]
        for image in seq[1:]:
            mask = image.point(lut, "1")
            # point() is used to map image pixels into mask pixels
            # via the lookup table (lut), creating a mask
            # with value 0 at transparent pixels and
            # 1 elsewhere
            temp.paste(image, None, mask)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(1000, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)


def assets(path):
    return Image.open("assets/" + path).convert("RGBA")


def google_assistant():
    CanvasButton(canvas, 6, 15, 'assets/assistant2.png', nothing)
    try:
        os.system('xterm -into %d -geometry 40x20 -sb &' % wid)
    except Exception as err:
        print(f'Error, {err}')


def play_sound():
    pyg.init()
    pyg.mixer.music.load('sounds/google.mp3')
    pyg.mixer.music.play(loops=1)


def vol_up():
    print('Vol +')


def vol_down():
    print('Vol -')


def back():
    print('Voltar')


def home():
    print('Menu principal')


def help_menu():
    import platform
    value = platform.uname()
    print(f'System: {value.system}; Version: {value.version}; Machine: {value.machine}')


def maps():
    print('Mapa')


def radio():
    print('Rádio')


def bluetooth():
    print('Bluetooth')


def settings():
    print('Ajustes')


def telephone():
    print('Ligação')


def nothing():
    sub.run(["echo", "hello"],  text=True, shell=True, stdout=sub.PIPE, stdin=sub.DEVNULL, stderr=sub.DEVNULL)


def end():
    exit(0)


def stop_it():
    while True:
        anim = MyLabel(window, 'assets/animation.gif')
        anim.pack()


window = tk.Tk()

try:
    os.system('cd ~/')
    os.system('/bin/bash -c "source env/bin/activate"')
except Exception as err:
    print(f'Error: {err}')

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

canvas2 = tk.Canvas(
    window,
    bg='#363636',
    height=320,
    width=480,
    bd=0,
    highlightthickness=0,
    relief='flat'
)

canvas.place(x=0, y=0)
pic = ImageTk.PhotoImage(assets('image_1.png'))
background = canvas.create_image(
    240.0,
    160.0,
    image=pic
)


vol_btn = CanvasButton(canvas, 6, 279, 'assets/vol-.png', vol_down)
vol_btn2 = CanvasButton(canvas, 6, 213, 'assets/vol+.png', vol_up)
return_btn = CanvasButton(canvas, 6, 147, 'assets/return.png', back)
home_btn = CanvasButton(canvas, 6, 81, 'assets/home.png', home)
close_btn = CanvasButton(canvas, 6, 15, 'assets/close.png', end)
assistant_btn = CanvasButton(canvas, 336, 193, 'assets/assistant.png', stop_it)
help_btn = CanvasButton(canvas, 240, 195, 'assets/help.png', help_menu)
settings_btn = CanvasButton(canvas, 128, 194, 'assets/settings.png', settings)
bluetooth_btn = CanvasButton(canvas, 171, 69, 'assets/bluetooth.png', bluetooth)
radio_btn = CanvasButton(canvas, 395, 69, 'assets/radio.png', radio)
telephone_btn = CanvasButton(canvas, 70, 70, 'assets/telephone.png', telephone)
maps_btn = CanvasButton(canvas, 305, 65, 'assets/maps.png', maps)


# window.attributes('-fullscreen', True)
window.title('Ford Multimídia V2.23')
window.resizable(False, False)
window.mainloop()

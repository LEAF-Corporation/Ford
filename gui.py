import os
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


def assets(path):
    return Image.open("assets/" + path).convert("RGBA")


def ok_google():
    try:
        play_sound()
        CanvasButton(canvas, 45, 0, 'assets/ok_google.png', os.system('googlesamples-assistant-hotword'))
    except Exception as err:
        print(f'Error: {err}')


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
    print('Ajuda')


def maps():
    print('Mapa')


def radio():
    print('Rádio')


def bluetooth():
    print('Bluetooth')


def settings(frame):
    frame.tkraise()


def telephone():
    print('Ligação')


def end():
    exit(0)



pyg.init()
pyg.mixer.music.load('sounds/startup.mp3')
pyg.mixer.music.play(loops=1)
window = tk.Tk()

try:
    import platform
    value = platform.uname()
    print(f'System: {value.system}; Version: {value.version}; Machine: {value.machine}')
    print('Ford Multimidia - V2.23')
    if value.system != 'Windows':
        os.system('cd ~/')
        os.system('/bin/bash -c "source env/bin/activate"')
    else:
        print('Debug mode: ON')
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
assistant_btn = CanvasButton(canvas, 336, 193, 'assets/assistant.png', ok_google)
help_btn = CanvasButton(canvas, 240, 195, 'assets/help.png', help_menu)
settings_btn = CanvasButton(canvas, 128, 194, 'assets/settings.png', settings)
bluetooth_btn = CanvasButton(canvas, 171, 69, 'assets/bluetooth.png', bluetooth)
radio_btn = CanvasButton(canvas, 395, 69, 'assets/radio.png', radio)
telephone_btn = CanvasButton(canvas, 70, 70, 'assets/telephone.png', telephone)
maps_btn = CanvasButton(canvas, 305, 65, 'assets/maps.png', maps)


try:
    img = tk.PhotoImage(file='assets/animation.gif')
    window.tk.call('wm', 'iconphoto', window._w, img)
except:
    pass

# window.attributes('-fullscreen', True)
window.title('Ford Multimídia V2.23')
window.resizable(False, False)
window.mainloop()

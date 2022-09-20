import tkinter as tk
from PIL import Image, ImageTk


def quitGame(event):
    window.destroy()


window = tk.Tk()
window.geometry("500x500")

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

bgImage = ImageTk.PhotoImage(Image.open("Proxlight_Designer_Export/background.png"))
bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

quitImage = ImageTk.PhotoImage(Image.open("Proxlight_Designer_Export/quit.png"))
quitButton = canvas.create_image(50, 50, image=quitImage)
canvas.tag_bind(quitButton, "<Button-1>", quitGame)

window.mainloop()

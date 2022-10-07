from tkinter import *
from PIL import Image, ImageTk


class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
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

        Label.__init__(self, master, image=self.frames[0])

        lut = [1] * 256
        lut[im.info["transparency"]] = 0

        temp = seq[0]
        for image in seq[1:]:
            mask = image.point(lut, "1")
            # point() is used to map image pixels into mask pixels
            # via the lookup table (lut), creating a mask
            # with value 0 at transparent pixels and
            # 1 elsewhere
            temp.paste(image, None, mask) #paste with mask
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


root = Tk()

anim = MyLabel(root, 'assets/animation.gif')
anim.pack()


def play_it():
    anim.after_idle(anim.play)


def stop_it():
    anim.after_cancel(anim.cancel)


Button(root, text='play', command=play_it).pack()
Button(root, text='stop', command=stop_it).pack()

root.mainloop()

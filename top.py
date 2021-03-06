from tkinter import *
import random

class Timer(object):

    def reset(self):
        self.timeron = False
        self.t.set('00:00:00')

    def start_timer(self):
        self.timeron = True
        self.timer()

    def stop(self):
        self.timeron = False

    def timer(self):
        if self.timeron == True:
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))

            h = int(h)
            m = int(m)
            s = int(s)
            if (s < 59):
                s += 1
            elif (s == 59):
                s = 0
                if (m < 59):
                    m += 1
                elif (m == 59):
                    h += 1
            if (h < 10):
                h = str(0) + str(h)
            else:
                h = str(h)
            if (m < 10):
                m = str(0) + str(m)
            else:
                m = str(m)
            if (s < 10):
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s

            self.t.set(self.d)

            self.root.after(930, self.timer)

    def __init__(self, root):
        super(Timer, self).__init__(root)

        self.root = root
        root.title("Stop Watch")
        root.geometry("600x500")
        root.resizable(False, False)
        self.grid()
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self, textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))
        self.bt1 = Button(self, text="Start", command=self.start_timer, font=("Courier 12 bold"))
        self.bt2 = Button(self, text="Stop", command=self.stop, font=("Courier 12 bold"))
        self.bt3 = Button(self, text="Reset", command=self.reset, font=("Courier 12 bold"))
        self.lb.grid(row=1, column=1)
        self.bt1.grid(row=2,column=1)
#        self.bt2.grid(2,2)
#        self.bt3.grid(2,3)
        self.timeron = False

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.timer = Timer(root)
        self.master = master
        self.photo_list = ["photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif", "photo5.gif", "photo6.gif",
                           "photo7.gif", "photo8.gif", "photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif",
                           "photo5.gif", "photo6.gif", "photo7.gif", "photo8.gif"]
        self.grid()
        self.start_bttn = Button(self, text="Click to Start!", command=self.start_game)
        self.start_bttn.grid(row=0, column=0)

    def start_game(self):
        self.timer.start_timer()


    def create_widgets(self):
        self.start_bttn.destroy()
        self.photo1a = self.get_image()
        self.bttn_1a = Button(self, image=self.photo1a)
        self.bttn_1a.photo = self.photo1a
        self.bttn_1a.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.photo1b = self.get_image()
        self.bttn_1b = Button(self, image=self.photo1b)
        self.bttn_1b.photo = self.photo1b
        self.bttn_1b.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        self.photo2a = self.get_image()
        self.bttn_2a = Button(self, image=self.photo2a)
        self.bttn_2a.photo = self.photo2a
        self.bttn_2a.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        self.photo2b = self.get_image()
        self.bttn_2b = Button(self, image=self.photo2b)
        self.bttn_2b.photo = self.photo2b
        self.bttn_2b.grid(row=0, column=3, padx=10, pady=10, sticky=W)
        self.photo3a = self.get_image()
        self.bttn_3a = Button(self, image=self.photo3a)
        self.bttn_3a.photo = self.photo3a
        self.bttn_3a.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.photo3b = self.get_image()
        self.bttn_3b = Button(self, image=self.photo3b)
        self.bttn_3b.photo = self.photo3b
        self.bttn_3b.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        self.photo4a = self.get_image()
        self.bttn_4a = Button(self, image=self.photo4a)
        self.bttn_4a.photo = self.photo4a
        self.bttn_4a.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        self.photo4b = self.get_image()
        self.bttn_4b = Button(self, image=self.photo4b)
        self.bttn_4b.photo = self.photo4b
        self.bttn_4b.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        self.photo5a = self.get_image()
        self.bttn_5a = Button(self, image=self.photo5a)
        self.bttn_5a.photo = self.photo5a
        self.bttn_5a.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.photo5b = self.get_image()
        self.bttn_5b = Button(self, image=self.photo5b)
        self.bttn_5b.photo = self.photo5b
        self.bttn_5b.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        self.photo6a = self.get_image()
        self.bttn_6a = Button(self, image=self.photo6a)
        self.bttn_6a.photo = self.photo6a
        self.bttn_6a.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        self.photo6b = self.get_image()
        self.bttn_6b = Button(self, image=self.photo6b)
        self.bttn_6b.photo = self.photo6b
        self.bttn_6b.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        self.photo7a = self.get_image()
        self.bttn_7a = Button(self, image=self.photo7a)
        self.bttn_7a.photo = self.photo7a
        self.bttn_7a.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.photo7b = self.get_image()
        self.bttn_7b = Button(self, image=self.photo7b)
        self.bttn_7b.photo = self.photo7b
        self.bttn_7b.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        self.photo8a = self.get_image()
        self.bttn_8a = Button(self, image=self.photo8a)
        self.bttn_8a.photo = self.photo8a
        self.bttn_8a.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        self.photo8b = self.get_image()
        self.bttn_8b = Button(self, image=self.photo8b)
        self.bttn_8b.photo = self.photo8b
        self.bttn_8b.grid(row=3, column=3, padx=10, pady=10, sticky=W)
        self.master.after(3000, self.flip)

    def get_image(self):
        a = random.choice(self.photo_list)
        b = PhotoImage(file=a)
        self.photo_list.remove(a)
        return b

    def flip(self):
        self.show1a = False
        self.show1b = False
        self.show2a = False
        self.show2b = False
        self.show3a = False
        self.show3b = False
        self.show4a = False
        self.show4b = False
        self.show5a = False
        self.show5b = False
        self.show6a = False
        self.show6b = False
        self.show7a = False
        self.show7b = False
        self.show8a = False
        self.show8b = False
        self.photo = PhotoImage(file="blank.gif")
        self.bttn_1a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_1a, self.photo1a, self.show1a))
        self.bttn_1a.photo = self.photo
        self.bttn_1b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_1b, self.photo1b, self.show1b))
        self.bttn_1b.photo = self.photo
        self.bttn_2a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_2a, self.photo2a, self.show2a))
        self.bttn_2a.photo = self.photo
        self.bttn_2b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_2b, self.photo2b, self.show2b))
        self.bttn_2b.photo = self.photo
        self.bttn_3a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_3a, self.photo3a, self.show3a))
        self.bttn_3a.photo = self.photo
        self.bttn_3b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_3b, self.photo3b, self.show3b))
        self.bttn_3b.photo = self.photo
        self.bttn_4a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_4a, self.photo4a, self.show4a))
        self.bttn_4a.photo = self.photo
        self.bttn_4b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_4b, self.photo4b, self.show4b))
        self.bttn_4b.photo = self.photo
        self.bttn_5a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_5a, self.photo5a, self.show5a))
        self.bttn_5a.photo = self.photo
        self.bttn_5b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_5b, self.photo5b, self.show5b))
        self.bttn_5b.photo = self.photo
        self.bttn_6a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_6a, self.photo6a, self.show6a))
        self.bttn_6a.photo = self.photo
        self.bttn_6b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_6b, self.photo6b, self.show6b))
        self.bttn_6b.photo = self.photo
        self.bttn_7a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_7a, self.photo7a, self.show7a))
        self.bttn_7a.photo = self.photo
        self.bttn_7b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_7b, self.photo7b, self.show7b))
        self.bttn_7b.photo = self.photo
        self.bttn_8a.config(image=self.photo, command=lambda: self.switchImage(self.bttn_8a, self.photo8a, self.show8a))
        self.bttn_8a.photo = self.photo
        self.bttn_8b.config(image=self.photo, command=lambda: self.switchImage(self.bttn_8b, self.photo8b, self.show8b))
        self.bttn_8b.photo = self.photo

    def switchImage(self, bttn, img, showing):
        if not showing:
            bttn.config(image=img)
            bttn.photo = img


root = Tk()
root.title("Memory")
root.geometry("400x500")
app = Application(root)
root.mainloop()

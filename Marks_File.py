import top
from tkinter import *

class Timer(Frame):

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
        self.bt2.grid(row =2, column = 2)
        self.bt3.grid(row = 2,column = 3)
        self.timeron = False


root = Tk()
app = Timer(root)
root.mainloop()



from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)



root = Tk()
root.title("")
root.geometry("200x85")
app = Application(root)
root.mainloop()

from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn_1a = Button(self).grid(row=0, column=0, padx=5, sticky=W)
        self.bttn_1b = Button(self).grid(row=0, column=2, padx=5, sticky=W)
        self.bttn_2a = Button(self).grid(row=0, column=4, padx=5, sticky=W)
        self.bttn_2b = Button(self).grid(row=0, column=6, padx=5, sticky=W)
        self.bttn_3a = Button(self).grid(row=1, column=0, padx=5, sticky=W)
        self.bttn_3b = Button(self).grid(row=1, column=2, padx=5, sticky=W)
        self.bttn_4a = Button(self).grid(row=1, column=4, padx=5, sticky=W)
        self.bttn_4b = Button(self).grid(row=1, column=6, padx=5, sticky=W)
        self.bttn_5a = Button(self).grid(row=2, column=0, padx=5, sticky=W)
        self.bttn_5b = Button(self).grid(row=2, column=2, padx=5, sticky=W)
        self.bttn_6a = Button(self).grid(row=2, column=4, padx=5, sticky=W)
        self.bttn_6b = Button(self).grid(row=2, column=6, padx=5, sticky=W)
        self.bttn_7a = Button(self).grid(row=3, column=0, padx=5, sticky=W)
        self.bttn_7b = Button(self).grid(row=3, column=2, padx=5, sticky=W)
        self.bttn_8a = Button(self).grid(row=3, column=4, padx=5, sticky=W)
        self.bttn_8b = Button(self).grid(row=3, column=6, padx=5, sticky=W)


root = Tk()
root.title("hi")
root.geometry("200x85")
app = Application(root)
root.mainloop()

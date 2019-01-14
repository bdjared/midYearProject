from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.bttn_1a = Button(self,).grid()
        self.bttn_1b = Button(self,).grid()
        self.bttn_2a = Button(self,).grid()
        self.bttn_2b = Button(self,).grid()
        self.bttn_3a = Button(self,).grid()
        self.bttn_3b = Button(self,).grid()
        self.bttn_4a = Button(self,).grid()
        self.bttn_4b = Button(self,).grid()


root = Tk()
root.title("")
root.geometry("200x85")
app = Application(root)
root.mainloop()

from tkinter import *
import random

list = ["photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif", "photo5.gif", "photo6.gif", "photo7.gif","photo8.gif"]

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        photo1a = self.get_image()
        self.bttn_1a = Button(self, image=photo1a)
        self.bttn_1a.photo = photo1a
        self.bttn_1a.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        photo1b = self.get_image()
        self.bttn_1b = Button(self, image=photo1b)
        self.bttn_1b.photo = photo1b
        self.bttn_1b.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        photo2a = self.get_image()
        self.bttn_2a = Button(self, image=photo2a)
        self.bttn_2a.photo = photo2a
        self.bttn_2a.grid(row=0, column=4, padx=10, pady=10, sticky=W)
        photo2b = self.get_image()
        self.bttn_2b = Button(self, image=photo2b)
        self.bttn_2b.photo = photo2b
        self.bttn_2b.grid(row=0, column=6, padx=10, pady=10, sticky=W)
        self.bttn_3a = Button(self, image=self.get_image()).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.bttn_3b = Button(self, image=self.get_image()).grid(row=1, column=2, padx=10, pady=10, sticky=W)
        self.bttn_4a = Button(self, image=self.get_image()).grid(row=1, column=4, padx=10, pady=10, sticky=W)
        self.bttn_4b = Button(self, image=self.get_image()).grid(row=1, column=6, padx=10, pady=10, sticky=W)
        self.bttn_5a = Button(self, image=self.get_image()).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.bttn_5b = Button(self, image=self.get_image()).grid(row=2, column=2, padx=10, pady=10, sticky=W)
        self.bttn_6a = Button(self, image=self.get_image()).grid(row=2, column=4, padx=10, pady=10, sticky=W)
        self.bttn_6b = Button(self, image=self.get_image()).grid(row=2, column=6, padx=10, pady=10, sticky=W)
        self.bttn_7a = Button(self, image=self.get_image()).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.bttn_7b = Button(self, image=self.get_image()).grid(row=3, column=2, padx=10, pady=10, sticky=W)
        self.bttn_8a = Button(self, image=self.get_image()).grid(row=3, column=4, padx=10, pady=10, sticky=W)
        self.bttn_8b = Button(self, image=self.get_image()).grid(row=3, column=6, padx=10, pady=10, sticky=W)

    def get_image(self):
        a = random.randint(0, 7)
        b = list[a]
        del(list[a])
        return b


root = Tk()
root.title("hi")
root.geometry("200x810")
app = Application(root)
root.mainloop()

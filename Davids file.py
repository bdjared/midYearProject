from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.photo_list = ["photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif", "photo5.gif", "photo6.gif",
                           "photo7.gif", "photo8.gif", "photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif",
                           "photo5.gif", "photo6.gif", "photo7.gif", "photo8.gif"]
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        photo = self.get_image()
        self.bttn_1a = Button(self, image=photo)
        self.bttn_1a.photo = photo
        self.bttn_1a.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_1b = Button(self, image=photo)
        self.bttn_1b.photo = photo
        self.bttn_1b.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_2a = Button(self, image=photo)
        self.bttn_2a.photo = photo
        self.bttn_2a.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_2b = Button(self, image=photo)
        self.bttn_2b.photo = photo
        self.bttn_2b.grid(row=0, column=3, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_3a = Button(self, image=photo)
        self.bttn_3a.photo = photo
        self.bttn_3a.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_3b = Button(self, image=photo)
        self.bttn_3b.photo = photo
        self.bttn_3b.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_4a = Button(self, image=photo)
        self.bttn_4a.photo = photo
        self.bttn_4a.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_4b = Button(self, image=photo)
        self.bttn_4b.photo = photo
        self.bttn_4b.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_5a = Button(self, image=photo)
        self.bttn_5a.photo = photo
        self.bttn_5a.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_5b = Button(self, image=photo)
        self.bttn_5b.photo = photo
        self.bttn_5a.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_6a = Button(self, image=photo)
        self.bttn_6a.photo = photo
        self.bttn_6a.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_6b = Button(self, image=photo)
        self.bttn_6b.photo = photo
        self.bttn_6b.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_7a = Button(self, image=photo)
        self.bttn_7a.photo = photo
        self.bttn_7a.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_7b = Button(self, image=photo)
        self.bttn_7b.photo = photo
        self.bttn_7b.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_8a = Button(self, image=photo)
        self.bttn_8a.photo = photo
        self.bttn_8a.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        photo = self.get_image()
        self.bttn_8b = Button(self, image=photo)
        self.bttn_8b.photo = photo
        self.bttn_8b.grid(row=3, column=3, padx=10, pady=10, sticky=W)

    def get_image(self):
        a = random.choice(self.photo_list)
        b = PhotoImage(file=a)
        self.photo_list.remove(a)
        return b


root = Tk()
root.title("hi")
root.geometry("200x810")
app = Application(root)
root.mainloop()

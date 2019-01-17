from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master = master
        self.photo_list = ["photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif", "photo5.gif", "photo6.gif",
                           "photo7.gif", "photo8.gif", "photo1.gif", "photo2.gif", "photo3.gif", "photo4.gif",
                           "photo5.gif", "photo6.gif", "photo7.gif", "photo8.gif"]
        self.grid()
        self.start_bttn = Button(self, text="Click to Start!", command=self.create_widgets)
        self.start_bttn.grid(row=0, column=0)

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
        photo = PhotoImage(file="blank.gif")
        self.bttn_1a.config(image=photo)
        self.bttn_1a.photo = photo
        self.bttn_1b.config(image=photo)
        self.bttn_1b.photo = photo
        self.bttn_2a.config(image=photo)
        self.bttn_2a.photo = photo
        self.bttn_2b.config(image=photo)
        self.bttn_2b.photo = photo
        self.bttn_3a.config(image=photo)
        self.bttn_3a.photo = photo
        self.bttn_3b.config(image=photo)
        self.bttn_3b.photo = photo
        self.bttn_4a.config(image=photo)
        self.bttn_4a.photo = photo
        self.bttn_4b.config(image=photo)
        self.bttn_4b.photo = photo
        self.bttn_5a.config(image=photo)
        self.bttn_5a.photo = photo
        self.bttn_5b.config(image=photo)
        self.bttn_5b.photo = photo
        self.bttn_6a.config(image=photo)
        self.bttn_6a.photo = photo
        self.bttn_6b.config(image=photo)
        self.bttn_6b.photo = photo
        self.bttn_7a.config(image=photo)
        self.bttn_7a.photo = photo
        self.bttn_7b.config(image=photo)
        self.bttn_7b.photo = photo
        self.bttn_8a.config(image=photo)
        self.bttn_8a.photo = photo
        self.bttn_8b.config(image=photo)
        self.bttn_8b.photo = photo


root = Tk()
root.title("Memory")
root.geometry("400x500")
app = Application(root)
root.mainloop()

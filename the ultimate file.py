import tkinter as tk
import random
import itertools
import time


class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.t = tk.StringVar()
        self.seconds = 0
        self.minutes = 0
        self.grid()
        self.var_dict = {}
        self.create_photos()
        self.lb = tk.Label(self, textvariable=self.t)
        self.lb.config(font="Courier 20 bold")
        self.lb.grid(row=5, column=0, columnspan=5)

        self.start_bttn = tk.Button(self, text="Click to Start!", command=self.create_tiles)
        self.start_bttn.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.score = 0

    def create_photos(self):
        alpha = "abcdefgh"
        for i in range(8):
            self.var_dict[alpha[i] + "1"] = tk.PhotoImage(file="photo" + str(i+1) + ".gif")
            self.var_dict[alpha[i] + "2"] = tk.PhotoImage(file="photo" + str(i+1) + ".gif")

    def create_tiles(self):
        self.start_bttn.destroy()
        keys = list(self.var_dict.keys())
        x_pts = [0, 1, 2, 3]
        y_pts = [0, 1, 2, 3]
        pos_list = list(itertools.product(x_pts, y_pts))
        for i in range(0, 16):
            rand = random.randint(0, len(pos_list) - 1)
            temp = pos_list.pop(rand)
            tk.Button(self, image=self.var_dict[keys[i]]).grid(row=temp[0], column=temp[1], padx=10, pady=10, sticky=tk.W)
        self.score_lbl = tk.Label(text="Score: %d" % self.score)
        self.score_lbl.grid(row=3, column=0)
        self.master.after(3000, self.flip)
        self.after(3000, self.start_timer)
        self.time_start = time.time() + 3

    def flip(self):
        self.photo = tk.PhotoImage(file="blank.gif")
        x_pts = [0, 1, 2, 3]
        y_pts = [0, 1, 2, 3]
        pos_list = list(itertools.product(x_pts, y_pts))
        for i in range(0, 16):
            temp = pos_list[i]
            self.what = tk.Button(self, image=self.photo)
            self.what['command'] = lambda idx=i, binst=self.what: self.click(binst)
            self.what.grid(row=temp[0], column=temp[1], padx=10, pady=10, sticky=tk.W)

    def click(self, binst):
        binst.destroy()

    def start_timer(self):
        self.t.set("%d minutes and %d seconds" % (self.minutes, self.seconds))
        self.seconds = int(time.time() - self.time_start) - self.minutes * 60
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0
        self.after(1000, self.start_timer)



root = tk.Tk()
root.title("Memory")
root.geometry("400x675")
app = Application(root)
root.mainloop()





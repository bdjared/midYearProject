#import tkinter as tk
#import random
#from tkinter import messagebox
#import time


#class MemoryTile:
 #   def __init__(self, parent):
 #       self.parent = parent
 #       self.buttons = [[tk.Button(root,
 #                                  width=4,
 #                                  height=2,
 #                                  command=lambda row=row, column=column: self.choose_tile(row, column)
 #                                  ) for column in range(4)] for row in range(4)]
 #       for row in range(4):
 #           for column in range(4):
 #               self.buttons[row][column].grid(row=row, column=column)
 #       self.first = None
 #       self.draw_board()

 #   def draw_board(self):
 #       self.answer = list('AABBCCDDEEFFGGHH')
 #       random.shuffle(self.answer)
 #       self.answer = [self.answer[:4],
 #                      self.answer[4:8],
 #                      self.answer[8:12],
 #                      self.answer[12:]]
 #       for row in self.buttons:
 #           for button in row:
 #               button.config(text='', state=tk.NORMAL)
 #       self.start_time = time.monotonic()

 #   def choose_tile(self, row, column):
 #       self.buttons[row][column].config(text=self.answer[row][column])
 #       self.buttons[row][column].config(state=tk.DISABLED)
 #       if not self.first:
 #           self.first = (row, column)
 #       else:
 #           a, b = self.first
 #           if self.answer[row][column] == self.answer[a][b]:
 #               self.answer[row][column] = ''
 #               self.answer[a][b] = ''
 #               if not any(''.join(row) for row in self.answer):
 #                   duration = time.monotonic() - self.start_time
 #                   messagebox.showinfo(title='Success!', message='You win! Time: {:.1f}'.format(duration))
 #                   self.parent.after(5000, self.draw_board)
 #           else:
 #               self.parent.after(3000, self.hide_tiles, row, column, a, b)
 #           self.first = None

 #   def hide_tiles(self, x1, y1, x2, y2):
 #       self.buttons[x1][y1].config(text='', state=tk.NORMAL)
 #       self.buttons[x2][y2].config(text='', state=tk.NORMAL)


#root = tk.Tk()
#memory_tile = MemoryTile(root)
#root.mainloop()

from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.t = StringVar()
        self.dict_list = [1, 2, 3, 4, 5, 6, 7, 8]
        a = "photo1.gif"
        b = "photo2.gif"
        c = "photo3.gif"
        d = "photo4.gif"
        e = "photo5.gif"
        f = "photo6.gif"
        g = "photo7.gif"
        h = "photo8.gif"
        self.photo_list = {"1": [a, a], "2": [b, b], "3": [c, c], "4": [d, d],
                           "5": [e, e], "6": [f, f], "7": [g, g], "8": [h, h]}
        self.t.set("00:00:00")
        self.lb = Label(self, textvariable=self.t)
        self.lb.config(font="Courier 40 bold")
        self.lb.grid(row=5, column=0, columnspan=5)
        self.timeron = False
        self.bttn_1a = Button(self)
        self.bttn_1b = Button(self)
        self.bttn_2a = Button(self)
        self.bttn_2b = Button(self)
        self.bttn_3a = Button(self)
        self.bttn_3b = Button(self)
        self.bttn_4a = Button(self)
        self.bttn_4b = Button(self)
        self.bttn_5a = Button(self)
        self.bttn_5b = Button(self)
        self.bttn_6a = Button(self)
        self.bttn_6b = Button(self)
        self.bttn_7a = Button(self)
        self.bttn_7b = Button(self)
        self.bttn_8a = Button(self)
        self.bttn_8b = Button(self)
        self.master = master
        self.grid()
        self.start_bttn = Button(self, text="Click to Start!", command=self.start_game)
        self.start_bttn.grid(row=0, column=0, sticky=W+E)
        self.score = 0

    def start_game(self):
        self.create_widgets()

    def create_widgets(self):
        self.start_bttn.destroy()
        self.photo1a = self.get_text(self.bttn_1a)
        self.bttn_1a = Button(self, text=self.photo1a)
        self.bttn_1a.photo = self.photo1a
        self.bttn_1a.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.photo1b = self.get_text(self.bttn_1b)
        self.bttn_1b = Button(self, text=self.photo1b)
        self.bttn_1b.photo = self.photo1b
        self.bttn_1b.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        self.photo2a = self.get_text(self.bttn_2a)
        self.bttn_2a = Button(self, text=self.photo2a)
        self.bttn_2a.photo = self.photo2a
        self.bttn_2a.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        self.photo2b = self.get_text(self.bttn_2b)
        self.bttn_2b = Button(self, text=self.photo2b)
        self.bttn_2b.photo = self.photo2b
        self.bttn_2b.grid(row=0, column=3, padx=10, pady=10, sticky=W)
        self.photo3a = self.get_text(self.bttn_3a)
        self.bttn_3a = Button(self, text=self.photo3a)
        self.bttn_3a.photo = self.photo3a
        self.bttn_3a.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.photo3b = self.get_text(self.bttn_3b)
        self.bttn_3b = Button(self, text=self.photo3b)
        self.bttn_3b.photo = self.photo3b
        self.bttn_3b.grid(row=1, column=1, padx=10, pady=10, sticky=W)
        self.photo4a = self.get_text(self.bttn_4a)
        self.bttn_4a = Button(self, text=self.photo4a)
        self.bttn_4a.photo = self.photo4a
        self.bttn_4a.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        self.photo4b = self.get_text(self.bttn_4b)
        self.bttn_4b = Button(self, text=self.photo4b)
        self.bttn_4b.photo = self.photo4b
        self.bttn_4b.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        self.photo5a = self.get_text(self.bttn_5a)
        self.bttn_5a = Button(self, text=self.photo5a)
        self.bttn_5a.photo = self.photo5a
        self.bttn_5a.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.photo5b = self.get_text(self.bttn_5b)
        self.bttn_5b = Button(self, text=self.photo5b)
        self.bttn_5b.photo = self.photo5b
        self.bttn_5b.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        self.photo6a = self.get_text(self.bttn_6a)
        self.bttn_6a = Button(self, text=self.photo6a)
        self.bttn_6a.photo = self.photo6a
        self.bttn_6a.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        self.photo6b = self.get_text(self.bttn_6b)
        self.bttn_6b = Button(self, text=self.photo6b)
        self.bttn_6b.photo = self.photo6b
        self.bttn_6b.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        self.photo7a = self.get_text(self.bttn_7a)
        self.bttn_7a = Button(self, text=self.photo7a)
        self.bttn_7a.photo = self.photo7a
        self.bttn_7a.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.photo7b = self.get_text(self.bttn_7b)
        self.bttn_7b = Button(self, text=self.photo7b)
        self.bttn_7b.photo = self.photo7b
        self.bttn_7b.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        self.photo8a = self.get_text(self.bttn_8a)
        self.bttn_8a = Button(self, text=self.photo8a)
        self.bttn_8a.photo = self.photo8a
        self.bttn_8a.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        self.photo8b = self.get_text(self.bttn_8b)
        self.bttn_8b = Button(self, text=self.photo8b)
        self.bttn_8b.photo = self.photo8b
        self.bttn_8b.grid(row=3, column=3, padx=10, pady=10, sticky=W)
        self.score_lbl = Label(text="Score: %d" % self.score)
        self.score_lbl.grid(row=0, column=4)
        self.master.after(3000, self.flip)
        self.after(3000, self.start_timer)

    def get_text(self, bttn):
        a = random.choice(self.dict_list)
        b = self.photo_list[str(a)]
        c = b[0]
        if len(self.photo_list[str(a)]) - 1 == 0:
            del self.photo_list[str(a)]
            self.dict_list.remove(a)
        else:
            del self.photo_list[str(a)]
            self.photo_list[str(a)] = [c]
        return c

    def flip(self):
        self.amt_showing = 0
        self.photo = PhotoImage(file="blank.gif")
        self.bttn_1a.config(text="a", command=lambda: self.switch_image(self.bttn_1a, self.photo1a))
        self.bttn_1a.photo = self.photo
        self.bttn_1b.config(text="a", command=lambda: self.switch_image(self.bttn_1b, self.photo1b))
        self.bttn_1b.photo = self.photo
        self.bttn_2a.config(text="a", command=lambda: self.switch_image(self.bttn_2a, self.photo2a))
        self.bttn_2a.photo = self.photo
        self.bttn_2b.config(text="a", command=lambda: self.switch_image(self.bttn_2b, self.photo2b))
        self.bttn_2b.photo = self.photo
        self.bttn_3a.config(text="a", command=lambda: self.switch_image(self.bttn_3a, self.photo3a))
        self.bttn_3a.photo = self.photo
        self.bttn_3b.config(text="a", command=lambda: self.switch_image(self.bttn_3b, self.photo3b))
        self.bttn_3b.photo = self.photo
        self.bttn_4a.config(text="a", command=lambda: self.switch_image(self.bttn_4a, self.photo4a))
        self.bttn_4a.photo = self.photo
        self.bttn_4b.config(text="a", command=lambda: self.switch_image(self.bttn_4b, self.photo4b))
        self.bttn_4b.photo = self.photo
        self.bttn_5a.config(text="a", command=lambda: self.switch_image(self.bttn_5a, self.photo5a))
        self.bttn_5a.photo = self.photo
        self.bttn_5b.config(text="a", command=lambda: self.switch_image(self.bttn_5b, self.photo5b))
        self.bttn_5b.photo = self.photo
        self.bttn_6a.config(text="a", command=lambda: self.switch_image(self.bttn_6a, self.photo6a))
        self.bttn_6a.photo = self.photo
        self.bttn_6b.config(text="a", command=lambda: self.switch_image(self.bttn_6b, self.photo6b))
        self.bttn_6b.photo = self.photo
        self.bttn_7a.config(text="a", command=lambda: self.switch_image(self.bttn_7a, self.photo7a))
        self.bttn_7a.photo = self.photo
        self.bttn_7b.config(text="a", command=lambda: self.switch_image(self.bttn_7b, self.photo7b))
        self.bttn_7b.photo = self.photo
        self.bttn_8a.config(text="a", command=lambda: self.switch_image(self.bttn_8a, self.photo8a))
        self.bttn_8a.photo = self.photo
        self.bttn_8b.config(text="a", command=lambda: self.switch_image(self.bttn_8b, self.photo8b))
        self.bttn_8b.photo = self.photo
        self.blank_bttn = Button(text="a")
        self.blank_bttn.photo = self.photo

    def switch_image(self, bttn, img):
        first_bttn = self.blank_bttn
        second_bttn = self.bttn_1a

        if self.amt_showing == 2:
            return

        if bttn.config(text = img):
            return

        if self.amt_showing < 2:
            bttn.config(text= img)
            bttn.text = img
            self.amt_showing += 1
            if self.amt_showing == 1:
                first_bttn = bttn
                self.image_1 = first_bttn.grid()
            elif self.amt_showing == 2:
                second_bttn = bttn
                self.image_2 = second_bttn.grid()

            if self.amt_showing == 2:
                if self.image_1 == self.image_2:
                    self.amt_showing = 0
                    self.score += 1
                    self.score_lbl.config(text="Score: %d" % self.score)

                else:
                    self.master.after(1000, self.flip)

    def timer_time(self):
        self.master.after(3000, self.start_timer())

    def reset(self):
        self.timeron = False
        self.t.set('00:00:00')

    def start_timer(self):

        self.timeron = True
        self.timer()

    def stop(self):
        self.timeron = False

    def timer(self):
        if self.timeron:
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))

            h = int(h)
            m = int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s == 59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    h += 1
            if h < 10:
                h = str(0) + str(h)
            else:
                h = str(h)
            if m < 10:
                m = str(0) + str(m)
            else:
                m = str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s = str(s)
            self.d = h + ":" + m + ":" + s

            self.t.set(self.d)

            self.after(930, self.timer)


root = Tk()
root.title("Memory")
root.geometry("400x575")
app = Application(root)
root.mainloop()
class Switch_image(object):
    def switch_image(self, bttn, img):
        if self.amt_showing == 0:
            self.first_bttn = self.blank_bttn
            self.second_bttn = self.bttn_1a

        if self.amt_showing == 2:
            return

        if bttn.photo == img:
            return

        if self.amt_showing < 2:
            bttn.config(image=img)
            bttn.photo = img
            self.amt_showing += 1
            if self.amt_showing == 1:
                self.first_bttn = bttn
                self.a = self.first_bttn.image_names()
            elif self.amt_showing == 2:
                self.second_bttn = bttn
                self.b = self.second_bttn.image_names()

            if self.amt_showing == 2:
                if self.a == self.b:
                    self.amt_showing = 0
                    self.score += 1
                    self.score_lbl.config(text="Score: %d" % self.score)

                else:
                    self.master.after(1000, self.flip)
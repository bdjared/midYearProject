import tkinter

class Screen_character_selector (tkinter.Frame):
    def __init__ (self, master, char_list, call_on_selected):
        super(Screen_character_selector, self).__init__(master)
        
        # Save the list of characters 
        self.char_list = char_list
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_selected
        
        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        
        The radio buttons on this page must use the variable "self.character".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character has been instantiated for your convenience below.
        
        Here is sample code for including an image on a page:   (char is a Character object)
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character = tkinter.StringVar()
        self.character.set(None)
        
        #
        # TO DO
        #
       
 
    def continue_clicked(self):
        ''' This method is called when the Next button is clicked. 
            Notice that it passes self.character back to the callback method. '''         
        self.call_on_selected(self.character.get())
            
        
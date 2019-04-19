'''
This programm asks you gessing the number.
'''

from tkinter import *

class Application (Frame):
    '''GUI-applocation who's play in number games'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.creat_widgets()
    
    def creat_widgets (self):
        '''Creating widgets.'''
        #Discription
        Label  (self,
                text = 'Я загадал число. Попытайтесь его угадать и ввести в полне ниже.'
                ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #Area for user input
        self.user_ent = Entry(self)
        self.user_ent.grid(row = 1, column = 0, sticky = W)
        #Starting bunnot
        Button(self,
               text = "Угадать число.",
               command = self.gess_number
               ).grid(row = 2, column = 1, sticky = W)
        #Text area.
        self.story_text = Text (self, width = 75, height = 10, wrap = WORD)
        self.story_text.grid(row = 3, column = 0, columnspan = 4)








        
def main ():
    root = Tk()
    root.title('Угадай число')
    app = Application (root)
    root.mainloop()
 
if __name__ == '__main__':
    main()

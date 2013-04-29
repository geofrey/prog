import socket
#import tictactoe #?
import tictactoetocol

from tkinter import *

class TicTacToeClient(Frame):
    
    def list_games(self):
        print(self.addy.get("0.0", END))

    def createWidgets(self):
        self.addy = Text(self)
        self.addy.configure({
            'height': 1,
            'width': 20
        })
        self.addy.pack({'side' : 'top'})

        self.player = Text(self)
        self.player.configure({
            'height': 1,
            'width': 20
        })
        self.player.pack({'side': 'left'})
        
        self.listgames = Button(self)
        self.listgames.configure({
            'text': 'List Games',
            'command': self.list_games
        })
        self.listgames.pack({'side': 'right'})
        
        self.QUIT = Button(self)
        self.QUIT.configure({
            'text': 'Quit',
            'command': self.quit # inherited from Frame
        })
        self.QUIT.pack({"side": "bottom"})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

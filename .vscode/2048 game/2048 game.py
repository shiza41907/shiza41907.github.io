#2048 python code - import modules
import tkinter as tk
import random
        
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 by TechVidvan")
 
        self.grid_main = tk.Frame(
            self, bg=Game.Color_grid, bd=3, width=600, height=600
        )
        self.grid_main.grid(pady=(110,0))
 
        self.GUI_maker()
        self.start_game()
 
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
 
        self.mainloop()
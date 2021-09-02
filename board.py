
import tkinter as tk
import turtle

class frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()     

    def create_widgets(self):

        self.init = tk.Button(self, text="Initialiser", fg='blue', command=board())
        self.hi_there = tk.Button(self, text="Hello World\n(click me)", command=self.say_hi)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)

        self.hi_there.pack(side="top")
        self.init.pack(side="top")
        self.quit.pack(side="bottom")
        

    def say_hi(self):
        print("hi there, everyone!")

class coordonates():

    def __init__(self,x,y):
        self.x = self.alpha_coord(x)
        self.y = str(y)
        
    def __str__(self):
        dump = "("+self.x+","+self.y+")"
        return dump

    def set_color(self):
        x=self.get_x_int()
        y=int(self.get_y())
        if abs(x-y)%2==0:
            return True
        else:
            return False

    def get_x(self):
        return self.x
    def get_x_int(self):
        return(self.int_coord(self.x))
    def get_y(self):
        return self.y

    def alpha_coord(self,x):
        letter = str(chr(x+96))
        return letter

    def int_coord(self,a):
        pos = int(ord(a)-96)
        return pos

class case():

    def __init__(self,x,y):
        self.coordonate = coordonates(int(x),int(y))
        self.color = self.coordonate.set_color()

    def __str__(self):
        dump = self.coordonate.__str__()
        return dump

    def get_coodonates(self):
        return self.coordonate
    def get_color(self):
        return self.color
    
class board():

    def __init__(self):
        self.cases = []
        for i in range(1,9):
            row = []
            for j in range(1,9):
                row.append(case(i,j))
        self.cases.append(row)
        print(self)

    def __str__(self):
        dump = ""
        for i in self.cases:
            for j in i:
                dump=dump + j.__str__()
        return dump




class piece():
    def __init__(self,type):
        self.type = type


root = tk.Tk()
app = frame(master=root)
app.mainloop()

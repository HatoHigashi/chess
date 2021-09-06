import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH

chess_piece_type = {('p',1),('n',2),('b',3),('r',4),('q',5),('k',6)}

class frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()     

    def create_widgets(self):

        self.master.title("Colours")
        canvas = Canvas(self, width=1600, height=900)
        x1=30
        y1=30
        positions = [x1,y1,x1+100,y1+100]
        for i in range(4):
            for j in range (4):
                case(8-i,2*j,canvas, positions)
                positions=[x1+100,y1,x1+200,y1+100]
                print(positions)
                case(8-i,2*j+1,canvas,positions)
                #canvas.create_rectangle(x1, y1, x1+100, y1+100,outline="brown", fill="#000") #(x1,y1,x2,y2), où (x1,y1) pos du top-left et (x2,y2) du bot-right
                #canvas.create_rectangle(x1+100 , y1, x1+200, y1+100,outline="brown", fill="#fff")
                x1 = x1 + 200
                print(positions)
            y1 = y1+100
            x1 = 30
            for k in range(4):   
                #canvas.create_rectangle(x1, y1, x1+100, y1+100,outline="brown", fill="#fff") #(x1,y1,x2,y2), où (x1,y1) pos du top-left et (x2,y2) du bot-right
                #canvas.create_rectangle(x1+100 , y1, x1+200, y1+100,outline="brown", fill="#000")  
                x1 = x1 + 200
            y1 = y1+100
            x1=30
                           
        
        self.init = tk.Button(self, text="Initialiser", fg='blue', command=board)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)

        self.init.pack(side="top")
        self.quit.pack(side="bottom")
        self.pack(fill=BOTH, expand=1)
        canvas.pack(fill=BOTH, expand=1)

def dump():
    print("Dump")
    return 1

class board(tk.Frame):

    def __init__(self):
        self.cases = []
        can = Canvas(self)
        for i in range(1,9):
            row = []
            for j in range(1,9):
                row.append(case(i,j,can))
            self.cases.append(row)
        print(self)

    def __str__(self):
        dump=""
        for i in self.cases:
            #print(i)
            dump2 = ""
            for j in i:
                #print(j)
                dump2=dump2 + j.__str__()
            dump = dump + dump2+"\n"
            #print(dump)
        return dump

class case():

    def __init__(self,x,y,canvas,positions):
        self.coordonate = coordonates(int(x),int(y))
        self.color = self.coordonate.set_color()
        x1 = positions[0]
        y1 = positions[1]
        x2 = positions[2]
        y2 = positions[3]
        self.case = canvas.create_rectangle(x1,y1,x2,y2,outline="brown", fill=self.color)

    def __str__(self):
        dump = self.coordonate.__str__()
        #print("STR CASE : "+dump)
        return dump

    def get_coodonates(self):
        return self.coordonate
    def get_color(self):
        return self.color
    
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
            return "#000"
        else:
            return "#fff"

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

class piece():
    def __init__(self,type):
        self.type = type

root = tk.Tk()
root.attributes('-fullscreen', True)
root.geometry("1920x1080")
app = frame(master=root)
app.mainloop()

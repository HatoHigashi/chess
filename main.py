import tkinter as tk
from tkinter import Label, StringVar, Tk, Canvas, Frame, BOTH
from tkinter.constants import OUTSIDE

class Fenetre(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent
        self.pack()
        self.parent.title("Chess")

    def create_widgets(self):
        board = Board(self)
        self.init_board = tk.Button(self, text="Initialiser Board", fg='blue', command=Board(self))
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.init_board.pack(side="top")
        self.quit.pack(side="bottom")
        self.pack(fill=BOTH, expand=1)
                   
class Board(tk.Frame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cases = []
        self.labels = []

        x1,y1=100,100
        x2,y2=x1+100,y1+100
        id = StringVar()

        for i in range(8):
            dump = []
            l_dump = []
            for j in range (4):

                id.set("("+str(i)+","+str(j)+")")
                l_dump_row_1 = tk.Label(self, bg="#ffffff", textvariable=id)
                l_dump.append(l_dump_row_1)
                l_dump_row_1.place(bordermode=OUTSIDE, height=x1, width=y1)
                positions = [x1,y1,x2,y2]
                dump.append(Case(8-i,2*j, positions, l_dump_row_1))

                x1,x2=x1+100,x2+100
                positions = [x1,y1,x2,y2]
                id.set("("+str(i)+","+str(j+1)+")")
                l_dump_row_2 = tk.Label(self, bg="#000000", textvariable=id)
                l_dump.append(l_dump_row_2)
                dump.append(Case(8-i,2*j+1, positions, l_dump_row_2))
                x1,x2=x1+100,x2+100

            self.cases.append(dump)
            self.labels.append(l_dump)
            x1,y1=100,y1+100
            x2,y2 = x1+100,y1+100
        
        # for i in range(len(self.cases)):
        #     for j in range(len(self.cases[i])):
        #         print(self.cases[i][j].get_pos_values())

        for i in range(len(self.cases)):
            if i==1 | i==6:
                for j in range(len(self.cases[i])):
                    self.cases[i][j].place_Pawn()
            elif i==0:
                self.cases[i][0].place_Piece(4)
                self.cases[i][1].place_Piece(2)
                self.cases[i][2].place_Piece(3)
                self.cases[i][3].place_Piece(5)
                self.cases[i][4].place_Piece(6)
                self.cases[i][5].place_Piece(3)
                self.cases[i][6].place_Piece(2)
                self.cases[i][7].place_Piece(4)
            elif i==7:
                self.cases[i][0].place_Piece(4)
                self.cases[i][1].place_Piece(2)
                self.cases[i][2].place_Piece(3)
                self.cases[i][3].place_Piece(6)
                self.cases[i][4].place_Piece(5)
                self.cases[i][5].place_Piece(3)
                self.cases[i][6].place_Piece(2)
                self.cases[i][7].place_Piece(4)
            else:
                for j in range(len(self.cases[i])):
                    self.cases[i][j].place_Piece(0)
                    
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

class Manager(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

class Case(tk.Frame):

    def __init__(self,x,y,positions, parent=None):
        self.coordonate = Coordonates(int(x),int(y))
        self.color = self.set_color()
        self.x1,self.y1,self.x2,self.y2 = positions[0],positions[1],positions[2],positions[3]
        self.lab = Label(self)
        self.can = Canvas(self)
        self.create_widgets()

    def __str__(self):
        dump = self.coordonate.__str__()
        #print("STR CASE : "+dump)
        return dump

    def get_coodonates(self):
        return self.coordonate
    def get_color(self):
        return self.color
    def get_pos_values(self):
        return("x1="+str(self.x1)+",x2="+str(self.x2)+",y1="+str(self.y1)+",y2="+str(self.y2))

    def set_color(self):
        x=int(self.coordonate.get_x_int())
        y=int(self.coordonate.get_y())
        if abs(x-y)%2==0:
            return "#000"
        else:
            return "#fff"

    def create_widgets(self):
        self.lab.pack()

    def place_Piece(self,num):
        pass

class Coordonates():

    def __init__(self,x,y):
        self.x = self.alpha_coord(x)
        self.y = str(y+1)
        
    def __str__(self):
        dump = "("+self.x+","+self.y+")"
        return dump

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

root = tk.Tk()
root.attributes('-fullscreen', True)
root.geometry("1920x1080")
app = Fenetre(parent=root)
app.create_widgets()
app.pack()
app.mainloop()

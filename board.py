import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH

chess_piece_type = {(1,'p'),(2,'n'),(3,'b'),(4,'r'),(5,'q'),(6,'k')}

class Fenetre(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Chess")
        self.cases = self.create_widgets() 

    def create_widgets(self):

        canvas_board = Canvas(self, width=1000, height=1080)
        canvas_manager = Canvas(self, width=920, height=1080)
        board = Board(self, canvas_board)
        manager = Manager(self, canvas_manager)
        self.init_board = tk.Button(self, text="Initialiser Board", fg='blue', command=Board(self,canvas_board))
        self.init_manager = tk.Button(self, text="Initialiser Manager", fg='black', command=Manager(self, canvas_manager))
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.init_board.pack(side="top")
        self.quit.pack(side="bottom")
        self.init_manager.pack(side='top')
        self.pack(fill=BOTH, expand=1)
        canvas_board.pack(fill=BOTH, expand=1)
        canvas_manager.pack(fill=BOTH, expand=1)
                   
class Manager():

    def __init__(self, frame, canvas):
        self.frame=frame
        self.canvas=canvas

class Board():

    def __init__(self, frame, canvas):

        self.frame = frame
        self.canvas = canvas
        self.cases = []
        
        x1,y1=100,100
        x2,y2=x1+100,y1+100
        for i in range(8):
            dump = []
            for j in range (4):
                positions = [x1,y1,x2,y2]
                #print(positions)
                dump.append(Case(8-i,2*j,canvas, positions))
                x1,x2=x1+100,x2+100
                positions = [x1,y1,x2,y2]
                #print(positions)
                dump.append(Case(8-i,2*j+1,canvas,positions))
                x1,x2=x1+100,x2+100
            self.cases.append(dump)
            x1,y1=100,y1+100
            x2,y2 = x1+100,y1+100
        
        # for i in range(len(self.cases)):
        #     for j in range(len(self.cases[i])):
        #         print(self.cases[i][j])

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

class Case():

    def __init__(self,x,y,canvas,positions):
        self.coordonate = Coordonates(int(x),int(y))
        self.color = self.coordonate.set_color()
        x1,y1,x2,y2 = positions[0],positions[1],positions[2],positions[3]
        self.case = canvas.create_rectangle(x1,y1,x2,y2,outline="brown", fill=self.color)
        self

    def __str__(self):
        dump = self.coordonate.__str__()
        #print("STR CASE : "+dump)
        return dump

    def get_coodonates(self):
        return self.coordonate
    def get_color(self):
        return self.color

    def place_Piece(self,num):
        pass
    
class Coordonates():

    def __init__(self,x,y):
        self.x = self.alpha_coord(x)
        self.y = str(y+1)
        
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

class Piece():
    def __init__(self,type,color,coordonates):
        if type == 1 :
            self.type = Pawn()
        elif type == 2 :
            self.type = Knight()
        elif type == 3 :
            self.type = Bishop()
        elif type == 4 :
            self.type = Rook()
        elif type == 5 :
            self.type = Queen()
        elif type == 6 :
            self.type = King()
        else:
            self.type = 0
        self.color = color #0 is black, 1 is white
        self.coordonates = coordonates

    def set_image(type):
        pass

class Pawn(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

class Mouvement():
    def __init__(self,start,x,y):
        self.start = start #Coordonates
        self.x = x #Horizontal mvt
        self.y = y #Vertical mvt



root = tk.Tk()
root.attributes('-fullscreen', True)
root.geometry("1920x1080")
app = Fenetre(master=root)
app.mainloop()

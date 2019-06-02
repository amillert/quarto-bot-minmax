import tkinter as tk
import os

setpole = False
chosepole = False
chosenFigure = ""
fields = []


class Tile(tk.Label):
    def __init__(self, parent, photo, figure):
        super(Tile, self).__init__(parent)
        self.bind('<Button-1>', self.chooseFigure)
        self.config(image=photo)
        self.figure = figure

    def chooseFigure(self, event):
        print(self.figure)
        global chosenFigure
        chosenFigure = self.figure
        print('Chosen: ')
        print(chosenFigure)


class Field(tk.Label):
    def __init__(self, parent, photo, number):
        super(Field, self).__init__(parent)
        self.bind('<Button-1>', self.setFigure)
        self.config(image=photo)
        self.number = number

    def setFigure(self, event):
        global chosenFigure
        if chosenFigure == "":
            print('Select figure first')
        else:
            print("Selected figure:")
            print(chosenFigure)
            script_dir = os.path.dirname(__file__)
            rel_path1 = "img/" + "1111" + ".png"
            print(rel_path1)
            abs_file_path1 = os.path.join(script_dir, rel_path1)
            newImage = tk.PhotoImage(file=abs_file_path1)
            fields[self.number]['image'] = newImage


class Main():

    def __init__(self, parent):
        self.parent = parent
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.createWidgets()

    def createWidgets(self):
        self.mainFrame = tk.Frame(self.parent)
        tk.Label(self.mainFrame, text="Quarto", font=("", 50)).pack()
        tk.Button(self.mainFrame, text='Player Start',
                  command=self.start).pack()
        tk.Button(self.mainFrame, text='Bot Start',
                  command=self.start).pack()
        self.mainFrame.pack(padx=10, pady=10)
        self.player1Frame = tk.Frame(self.parent)
        self.player2Frame = tk.Frame(self.parent)
        self.gameFrame = tk.Frame(self.parent)
        self.redBar = tk.Frame(width=70, height=680, background="red")
        self.greenBar = tk.Frame(width=70, height=680, background="green")
        self.chosenFigure = tk.Frame(self.parent)

    def loadFigureImg(self, figure):
        script_dir = os.path.dirname(__file__)
        rel_path1 = "img/" + figure + ".png"
        print(rel_path1)
        abs_file_path1 = os.path.join(script_dir, rel_path1)
        photo1 = tk.PhotoImage(file=abs_file_path1)
        return photo1, figure

    def createboard(self):
        photo0, wfigure0 = self.loadFigureImg("0010")
        photo1, wfigure1 = self.loadFigureImg("0011")
        photo2, wfigure2 = self.loadFigureImg("0111")
        photo3, wfigure3 = self.loadFigureImg("1111")
        photo4, wfigure4 = self.loadFigureImg("1010")
        photo5, wfigure5 = self.loadFigureImg("0110")
        photo6, wfigure6 = self.loadFigureImg("1110")
        photo7, wfigure7 = self.loadFigureImg("1011")
        Tile(self.player1Frame, photo0, wfigure0).grid(row=0, column=0)
        Tile(self.player1Frame, photo1, wfigure1).grid(row=0, column=1)
        Tile(self.player1Frame, photo2, wfigure2).grid(row=1, column=0)
        Tile(self.player1Frame, photo3, wfigure3).grid(row=1, column=1)
        Tile(self.player1Frame, photo4, wfigure4).grid(row=2, column=0)
        Tile(self.player1Frame, photo5, wfigure5).grid(row=2, column=1)
        Tile(self.player1Frame, photo6, wfigure6).grid(row=3, column=0)
        Tile(self.player1Frame, photo7, wfigure7).grid(row=3, column=1)
        #  WTF?
        # for i in range(4):
        #     for j in range(4):
        #         photo2 = self.loadFigureImg("empty")
        #         Tile(self.gameFrame, photo2).grid(row=i, column=j)

        empty, empty1 = self.loadFigureImg("empty")
        field0 = Field(self.gameFrame, empty, 0)
        field1 = Field(self.gameFrame, empty, 1)
        field2 = Field(self.gameFrame, empty, 2)
        field3 = Field(self.gameFrame, empty, 3)
        field4 = Field(self.gameFrame, empty, 4)
        field5 = Field(self.gameFrame, empty, 5)
        field6 = Field(self.gameFrame, empty, 6)
        field7 = Field(self.gameFrame, empty, 7)
        field8 = Field(self.gameFrame, empty, 8)
        field9 = Field(self.gameFrame, empty, 9)
        field10 = Field(self.gameFrame, empty, 10)
        field11 = Field(self.gameFrame, empty, 11)
        field12 = Field(self.gameFrame, empty, 12)
        field13 = Field(self.gameFrame, empty, 13)
        field14 = Field(self.gameFrame, empty, 14)
        field15 = Field(self.gameFrame, empty, 15)
        fields.append(field0)
        fields.append(field1)
        fields.append(field2)
        fields.append(field3)
        fields.append(field4)
        fields.append(field5)
        fields.append(field6)
        fields.append(field7)
        fields.append(field8)
        fields.append(field9)
        fields.append(field10)
        fields.append(field11)
        fields.append(field12)
        fields.append(field13)
        fields.append(field14)
        fields.append(field15)
        field0.grid(row=0, column=0)
        field1.grid(row=0, column=1)
        field2.grid(row=0, column=2)
        field3.grid(row=0, column=3)
        field4.grid(row=1, column=0)
        field5.grid(row=1, column=1)
        field6.grid(row=1, column=2)
        field7.grid(row=1, column=3)
        field8.grid(row=2, column=0)
        field9.grid(row=2, column=1)
        field10.grid(row=2, column=2)
        field11.grid(row=2, column=3)
        field12.grid(row=3, column=0)
        field13.grid(row=3, column=1)
        field14.grid(row=3, column=2)
        field15.grid(row=3, column=3)
        print(fields)
        black0, bfigure0 = self.loadFigureImg("0000")
        black1, bfigure1 = self.loadFigureImg("0001")
        black2, bfigure2 = self.loadFigureImg("0101")
        black3, bfigure3 = self.loadFigureImg("1101")
        black4, bfigure4 = self.loadFigureImg("1000")
        black5, bfigure5 = self.loadFigureImg("0100")
        black6, bfigure6 = self.loadFigureImg("1100")
        black7, bfigure7 = self.loadFigureImg("1001")
        Tile(self.player2Frame, black0, bfigure0).grid(row=0, column=0)
        Tile(self.player2Frame, black1, bfigure1).grid(row=0, column=1)
        Tile(self.player2Frame, black2, bfigure2).grid(row=1, column=0)
        Tile(self.player2Frame, black3, bfigure3).grid(row=1, column=1)
        Tile(self.player2Frame, black4, bfigure4).grid(row=2, column=0)
        Tile(self.player2Frame, black5, bfigure5).grid(row=2, column=1)
        Tile(self.player2Frame, black6, bfigure6).grid(row=3, column=0)
        Tile(self.player2Frame, black7, bfigure7).grid(row=3, column=1)

   # def createpoles(self):
   #     for

    def start(self):
        global setpole
        global chosepole
        setpole = False
        chosepole = True

        self.mainFrame.forget()
        self.createboard()
        self.player1Frame.grid(row=0, column=0)
        self.greenBar.grid(row=0, column=1)
        self.gameFrame.grid(row=0, column=2)
        self.redBar.grid(row=0, column=3)
        self.player2Frame.grid(row=0, column=4)
        return


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Quarto")
    Main(root)
    root.mainloop()

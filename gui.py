import tkinter as tk
import numpy as np
import os

setpole = False
chosepole = False
chosenFigure = ""
whiteFigures = []
blackFigures = []
fields = []
photos = []


class Tile(tk.Label):
    def __init__(self, parent, photo, figure):
        super(Tile, self).__init__(parent)
        self.bind('<Button-1>', self.chooseFigure)
        self.config(image=photo)
        self.figure = figure

    def chooseFigure(self, event):
        global chosenFigure
        chosenFigure = self.figure
        print('Chosen: ')
        print(chosenFigure)

    def getFigure(self):
        print(self.figure)


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
            newImage, figure = self.loadFigureImg(chosenFigure)
            self.config(image=photos[int(chosenFigure, 2)])
            chosenFigure = ""

    def loadFigureImg(self, figure):
        script_dir = os.path.dirname(__file__)
        rel_path1 = "img/" + figure + ".png"
        abs_file_path1 = os.path.join(script_dir, rel_path1)
        photo1 = tk.PhotoImage(file=abs_file_path1)
        return photo1, figure


class Main():

    def __init__(self, parent):
        self.parent = parent
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.createWidgets()

    def createWidgets(self):
        self.mainFrame = tk.Frame(self.parent)
        tk.Label(self.mainFrame, text="Quarto", font=("", 50)).pack()
        tk.Button(self.mainFrame, text='Start',
                  command=self.start).pack()
        self.mainFrame.pack(padx=10, pady=10)
        self.player1Frame = tk.Frame(self.parent)
        self.player2Frame = tk.Frame(self.parent)
        self.gameFrame = tk.Frame(self.parent)
        self.redBar = tk.Frame(width=70, height=680, background="red")
        self.greenBar = tk.Frame(width=70, height=680, background="green")
        self.chosenFigure = tk.Frame(self.parent)
        self.imagesToArray()

    def imagesToArray(self):
        script_dir = os.path.dirname(__file__)
        for i in range(16):
            numInBinary = np.binary_repr(i, width=4)
            rel_path = "img/" + numInBinary + ".png"
            abs_file_path = os.path.join(script_dir, rel_path)
            photo = tk.PhotoImage(file=abs_file_path)
            photos.append(photo)
        rel_path = "img/empty.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        photo = tk.PhotoImage(file=abs_file_path)
        photos.append(photo)

    def loadFigureImg(self, figure):
        script_dir = os.path.dirname(__file__)
        rel_path1 = "img/" + figure + ".png"
        abs_file_path1 = os.path.join(script_dir, rel_path1)
        photo1 = tk.PhotoImage(file=abs_file_path1)
        return photo1, figure

    def printFigures(self):
        for tile in blackFigures:
            print(tile.getFigure())

    def createboard(self):
        self.setFields()
        self.setBlackFigures()
        self.setWhiteFigures()

    def setFields(self):
        for i in range(4):
            for j in range(4):
                field = Field(self.gameFrame, photos[16], i+j)
                field.grid(row=i, column=j)
                fields.append(field)

    def setBlackFigures(self):
        for i, photo in enumerate(photos[:-1]):
            if i % 2 == 0:
                numInBinary = np.binary_repr(i, width=4)
                tile = Tile(self.player2Frame, photo, numInBinary)
                blackFigures.append(tile)

        blackFigures[0].grid(row=0, column=0)
        blackFigures[1].grid(row=0, column=1)
        blackFigures[2].grid(row=1, column=0)
        blackFigures[3].grid(row=1, column=1)
        blackFigures[4].grid(row=2, column=0)
        blackFigures[5].grid(row=2, column=1)
        blackFigures[6].grid(row=3, column=0)
        blackFigures[7].grid(row=3, column=1)

    def setWhiteFigures(self):
        for i, photo in enumerate(photos[:-1]):
            if i % 2 != 0:
                numInBinary = np.binary_repr(i, width=4)
                tile = Tile(self.player1Frame, photo, numInBinary)
                whiteFigures.append(tile)

        whiteFigures[0].grid(row=0, column=0)
        whiteFigures[1].grid(row=0, column=1)
        whiteFigures[2].grid(row=1, column=0)
        whiteFigures[3].grid(row=1, column=1)
        whiteFigures[4].grid(row=2, column=0)
        whiteFigures[5].grid(row=2, column=1)
        whiteFigures[6].grid(row=3, column=0)
        whiteFigures[7].grid(row=3, column=1)

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

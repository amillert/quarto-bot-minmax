import tkinter as tk
from tkinter.messagebox import showinfo
import sys
import numpy as np
import os
import gameplay.intelligent as intelligent
import play
import random
import utils.functions as f
from utils.setup import board, pos, pawns, pawn_picked_for_player, move, last_picked_pawn


block = 0
labels = []
figures = []
fields = []
photos = []

class Move:
    def __init__(self, board, rest_positions, rest_pawns, parent=None, level=0):
        self.board = board
        self.rest_positions = rest_positions
        self.rest_pawns = rest_pawns
        self.moves = []
        self.parent = parent
        self.level = level
        self.winning = f.check_board_result(self.board)
    
    def add_move(self, move):
        assert isinstance(move, Move), f"Single move must be of type `Move`, passed type: `{type(move)}`"
        self.moves.append(move)

class Tile(tk.Label):
    def __init__(self, parent, photo, figure):
        super(Tile, self).__init__(parent)
        self.bind('<Button-1>', self.chooseFigure)
        self.isEmpty = False
        self.config(image=photo)
        self.figure = figure

    def setIsEmpty(self):
        self.isEmpty = True
    
    def getIsEmpty(self):
        return self.isEmpty

    def chooseFigure(self, event):
        global pos
        global pawns
        global pawn_picked_for_player
        global board
        global last_picked_pawn
        global block
        if block == 1:
            if self.getIsEmpty() == True:
                changeNotificationText("Wybierz figurkę.")
                print("Choose pawn")
            else:
                pawn_picked_for_bot = self.figure
                pawns = [x for x in pawns if x != pawn_picked_for_bot]
                changeSelectedPawn(pawn_picked_for_bot)
                self.setPhoto(16)
                last_picked_pawn = pawn_picked_for_bot
                print("QUARTO-BOT's move.")
                changeNotificationText("Ruch Quarto Bot !")
                print(len(labels))
                pos, pawns, pawn_picked_for_player, board, bot_picked_position = intelligent.bot_move(
                    pos, pawns + [pawn_picked_for_bot], pawn_picked_for_bot, board)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Bot picked position")
                print(bot_picked_position)
                for idx, field in enumerate(fields):
                    if field.getPosition() == str(bot_picked_position):
                        field.setPhoto(int(last_picked_pawn, 2)) 
                        field.setIsNotEmpty()
                self.setIsEmpty()
                changeSelectedPawn('10000')
                printConsoleBoard()
                checkIsWinning("QUARTO BOT")
                userMove()
                block = 0     
        elif block == 0:
            changeNotificationText("Wybierz pole.")
            print("Choose field first")

    def getFigure(self):
        print(self.figure)
    
    def setPhoto(self, pickedPawnInDecimal):
        self.config(image=photos[pickedPawnInDecimal])


class Field(tk.Label):
    def __init__(self, parent, photo, number, i, j):
        super(Field, self).__init__(parent)
        self.bind('<Button-1>', self.setField)
        self.config(image=photo)
        self.isEmpty = True
        self.number = number
        self.X = i
        self.Y = j

    def setIsNotEmpty(self):
        self.isEmpty = False
    
    def getIsEmpty(self):
        return self.isEmpty

    def setPhoto(self, pickedPawnInDecimal):
        print("in field {pickedPawnInDecimal}")
        self.config(image=photos[pickedPawnInDecimal])

    def setField(self, event):
        global pos
        global pawns
        global pawn_picked_for_player
        global board
        global block
        if block == 0:
            if self.getIsEmpty() == False:
                changeNotificationText("Pole zajete.")
                print("Field is busy")
            else:
                changeNotificationText("Wybierz figurkę.")
                play.player_picked_position = str(self.X) + str(self.Y)
                self.setPhoto(int(str(pawn_picked_for_player), 2))
                changeSelectedPawn('10000')
                assert len(str(play.player_picked_position)) == 2, "You must pass positions on the board"
                pos = [x for x in pos if x != str(play.player_picked_position)]
                i, j = [int(x) for x in play.player_picked_position]
                board[i][j] = pawn_picked_for_player
                print("The board looks like so:")
                printConsoleBoard()
                checkIsWinning("USER")
                print(f"There are {pawns} possible pawns to choose from.")
                print("Which one do You wish to pick for the bot? ")
                self.setIsNotEmpty()
                block = 1
        elif block == 1:
            changeNotificationText("Wybierz figurkę.")
            print("Choose pawn first")


    def loadFigureImg(self, figure):
        script_dir = os.path.dirname(__file__)
        rel_path1 = "img/" + figure + ".png"
        abs_file_path1 = os.path.join(script_dir, rel_path1)
        photo1 = tk.PhotoImage(file=abs_file_path1)
        return photo1, figure

    def getPosition(self):
        return str(self.X) + str(self.Y)

    def getPhoto(self):
        return self.cget('image')

class Main():

    def __init__(self, parent):
        self.parent = parent
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()
        self.createWidgets()
        self.start()

    def createWidgets(self):
        self.player1Frame = tk.Frame(self.parent)
        self.selectFrame = tk.Frame(self.parent, background='#ececec')
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

    def createboard(self):
        self.setFields()
        self.setBoardFigures()

    def setFields(self):
        number = 0
        for i in range(4):
            for j in range(4):
                field = Field(self.gameFrame, photos[16], number, i, j)
                field.grid(row=i, column=j)
                fields.append(field)
                number = number + 1

    def setBoardFigures(self):
        for i, photo in enumerate(photos[:-1]):
            numInBinary = np.binary_repr(i, width=4)
            tile = Tile(self.player1Frame, photo, numInBinary)
            figures.append(tile)

        figures[0].grid(row=0, column=0)
        figures[1].grid(row=0, column=1)
        figures[2].grid(row=1, column=0)
        figures[3].grid(row=1, column=1)
        figures[4].grid(row=2, column=0)
        figures[5].grid(row=2, column=1)
        figures[6].grid(row=3, column=0)
        figures[7].grid(row=3, column=1)
        figures[8].grid(row=0, column=2)
        figures[9].grid(row=0, column=3)
        figures[10].grid(row=1, column=2)
        figures[11].grid(row=1, column=3)
        figures[12].grid(row=2, column=2)
        figures[13].grid(row=2, column=3)
        figures[14].grid(row=3, column=2)
        figures[15].grid(row=3, column=3)

        

    def start(self):
        self.createboard()
        notifi = tk.Label(text="Powiadomienie", font=("Roboto", 13))
        notifi.grid(row=0, column=2)
        labels.append(notifi)
        self.player1Frame.grid(row=1, column=0)
        self.greenBar.grid(row=1, column=1)
        self.gameFrame.grid(row=1, column=2)
        self.redBar.grid(row=1, column=3)
        self.createSelectFrame()
        userMove()
        return

    def createSelectFrame(self):
        self.selectFrame.grid(row=1, column=4)
        self.whiteBar = tk.Frame(self.selectFrame, height=220, background="#ececec")
        self.whiteBar.grid(row=0, column=0)
        self.whiteBar2 = tk.Frame(self.selectFrame, height=220, background="#ececec")
        self.whiteBar2.grid(row=3, column=0)
        tile = Tile(self.selectFrame, photos[16], 00000000)
        tile.grid(row=2, column=0)
        label = tk.Label(self.selectFrame, text="Aktualna figura", bg='#ececec', font=("Roboto", 13))
        label.grid(row=1, column=0)
        figures.append(tile)  

def changeNotificationText(text):
    labels[0]['text'] = text

def userMove():
    changeNotificationText("Twój Ruch !")
    changeSelectedPawn(pawn_picked_for_player)
    deletePawnFromChoose(pawn_picked_for_player)
    print(f"PLAYER has been given {pawn_picked_for_player} pawn.")
    figures[int(pawn_picked_for_player, 2)].setIsEmpty()
    global pos
    print(f"There are {pos} possible positions to place it.")
    print("Where do You wish to place the pawn? ")

def deletePawnFromChoose(pickedPawn):
    figures[int(pickedPawn, 2)].setPhoto(16)
    
def changeSelectedPawn(pickedPawn):
    figures[16].setPhoto(int(pickedPawn, 2))

def printConsoleBoard():
    global board
    play.f.print_board(board)

def checkIsWinning(who):
    global board
    if play.f.check_if_winning(board):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("It is a winning board:")
        play.f.print_board(board)
        print("The game has been won by the " + who)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if who == "QUARTO BOT":
            changeNotificationText("PRZEGRAŁEŚ !")
            popup_bonus(who)
        elif who == "USER":
            changeNotificationText("WYGRAŁEŚ !")
            popup_bonus(who)

def popup_bonus(who):
    win = tk.Toplevel()
    win.wm_title("Koniec gry")

    if who == "QUARTO BOT":
        l = tk.Label(win, text="PRZEGRAŁEŚ !")
        l.grid(row=0, column=0)
    elif who == "USER":
        l = tk.Label(win, text="WYGRAŁEŚ !")
        l.grid(row=0, column=0)
    

    b = tk.Button(win, text="Zakończ")
    b.bind('<Button-1>', end)
    b.grid(row=1, column=0)

def end(event):
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Quarto")
    Main(root)
    root.mainloop()

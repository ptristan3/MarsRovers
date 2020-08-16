from tkinter import *
COLOR_START = '#5fA'
COLOR_END = '#38f'


class Grid_Window:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.cellwidth = 60
        self.cellheight = 60
        self.rect = {}

    def draw_grid(self, rows, columns):
        self.myCanvas = Canvas(self.myContainer1)
        self.myCanvas.configure(width=self.cellheight *
                                rows+4, height=self.cellwidth*columns+4)

        self.myCanvas.pack(side=LEFT, expand=0)
        for column in range(rows):
            for row in range(columns):
                x1 = column * self.cellwidth+2
                y1 = row * self.cellheight+2
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row, column] = self.myCanvas.create_rectangle(
                    x1, y1, x2, y2, fill="#ccc", width=2)

    def draw_rover(self, x, y, h, number, cardinal, move):
        x1 = x * self.cellwidth
        y1 = self.cellheight*(h) - y * self.cellheight - self.cellheight
        x2 = x1 + self.cellwidth
        y2 = y1 + self.cellheight
        if move is 'Inicial':
            self.rect[x, y] = self.myCanvas.create_rectangle(
                x1+4, y1+4, x2, y2, fill=COLOR_START, width=2)
        else:
            self.rect[x, y] = self.myCanvas.create_rectangle(
                x1+4, y1+4, x2, y2, fill=COLOR_END, width=2)
        self.myCanvas.create_text(
            x1+30, y1+15, fill="#fff", font="Arial 14 bold", text=str(cardinal))
        self.myCanvas.create_text(
            x1+30, y1+35, fill="#fff", font="Arial 9 bold", text="Rover: "+str(number))
        self.myCanvas.create_text(
            x1+30, y1+50, fill="#fff", font="Arial 6 bold", text=str(move))
        self.myCanvas.update

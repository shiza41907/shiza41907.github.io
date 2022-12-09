import pygame
RED = (255, 0, 0)
BURLYWOOD = (222,184,135)
BURNTSIENNA = (138,54,15)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

class Board:
    def __init__(self,):
        self.board = []
        self.selected_piece= None
        self.red_left = self.black_left = 12
        self.red_kings = self.white_kings = 0

    def draw_squares(self, win): 
        win.fill(BURNTSIENNA)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BURLYWOOD, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS)
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
class Piece:
    PADDING = 15
    OUTLINE = 2
    WIDTH, HEIGHT = 600, 600
    ROWS, COLS = 8, 8
    SQUARE_SIZE = WIDTH//COLS

    #rgb
    RED = (255, 0, 0)
    BURLYWOOD = (222,184,135)
    BURNTSIENNA = (138,54,15)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    def _init_(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        if self.color == BLACK:
            self.direction = 1
        else:
            self.direction = -1

        self.x = 0
        self.y = 0
        
    def calc_pos(self):
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
            self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE)  
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def _repr_(self):
         return str(self.color)


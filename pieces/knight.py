from game.settings import white, black, brown, width, height, knight_icon_1, knight_icon_2
from pieces import Piece

class Knight(Piece):

    def __init__(self, tile, team):
        Piece.__init__(self, tile, team)

    def render(self):
        if (self.player.team == 1):
            self.current_tile.board.screen.blit(knight_icon_1, (self.x_pos, self.y_pos))
        else:
            self.current_tile.board.screen.blit(knight_icon_2, (self.x_pos, self.y_pos))
    
    def check_move(self, tile):

        # Check above-right
        if (self.y - 2 >= 0 and self.x + 1 < 8):
            c_tile = self.current_tile.board.board[self.y - 2][self.x + 1]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
        # Check above-left 
        if (self.y - 2 >= 0 and self.x - 1 >= 0):
            c_tile = self.current_tile.board.board[self.y - 2][self.x - 1]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True

        # Check below-right
        if (self.y + 2 < 8 and self.x + 1 < 8):
            c_tile = self.current_tile.board.board[self.y + 2][self.x + 1]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
        # Check below-left
        if (self.y + 2 < 8 and self.x - 1 >= 0):
            c_tile = self.current_tile.board.board[self.y + 2][self.x - 1]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True

        # Check right-above
        if (self.x + 2 < 8 and self.y - 1 >= 0):
            c_tile = self.current_tile.board.board[self.y - 1][self.x + 2]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
        # Check right-below
        if (self.x + 2 < 8 and self.y + 1 < 8):
            c_tile = self.current_tile.board.board[self.y + 1][self.x + 2]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True

        # Check left-above
        if (self.x - 2 >= 0 and self.y - 1 >= 0):
            c_tile = self.current_tile.board.board[self.y - 1][self.x - 2]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
        # Check left-below
        if (self.x - 2 >= 0 and self.y + 1 < 8):
            c_tile = self.current_tile.board.board[self.y + 1][self.x - 2]
            if (self.check_tile(c_tile)):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True


        return False
        

    def check_tile(self, c_tile):
        if (c_tile and not c_tile.piece):
            return (c_tile.x, c_tile.y)
        elif(c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
            return (c_tile.x, c_tile.y)
        return False


from game.settings import white, black, brown, width, height, queen_icon_1, queen_icon_2
from pieces import Piece

class Queen(Piece):

    def __init__(self, tile, team):
        Piece.__init__(self, tile, team)


    def render(self):
        if (self.player.team == 1):
            self.current_tile.board.screen.blit(queen_icon_1, (self.x_pos, self.y_pos))
        else:
            self.current_tile.board.screen.blit(queen_icon_2, (self.x_pos, self.y_pos))

    def check_move(self, tile):


        # Above
        y = self.y - 1
        while (y >= 0):
            above_tile = self.current_tile.board.board[y][self.x]
            if (above_tile and not above_tile.piece):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
            elif (above_tile and above_tile.piece and above_tile.piece.player.team != self.player.team):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else: 
                break
            y -= 1

        # Below
        y = self.y + 1
        while (y < 8):
            above_tile = self.current_tile.board.board[y][self.x]
            if (above_tile and not above_tile.piece):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
            elif (above_tile and above_tile.piece and above_tile.piece.player.team != self.player.team):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else: 
                break
            y += 1

        # Right
        x = self.x - 1
        while (x >= 0):
            above_tile = self.current_tile.board.board[self.y][x]
            if (above_tile and not above_tile.piece):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
            elif(above_tile and above_tile.piece and above_tile.piece.player.team != self.player.team):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else:
                break
            x -= 1

        # Left
        x = self.x + 1
        while (x < 8):
            above_tile = self.current_tile.board.board[self.y][x]
            if (above_tile and not above_tile.piece):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
            elif(above_tile and above_tile.piece and above_tile.piece.player.team != self.player.team):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else:
                break
            x += 1

        x, y = self.x + 1, self.y - 1
        while (x  < 8 and y >= 0):
            c_tile = self.current_tile.board.board[y][x]
            if (c_tile and not c_tile.piece):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else: 
                break
            x += 1
            y -= 1

        # Check above-left
        x, y = self.x - 1, self.y - 1
        while (x  >= 0 and y >= 0):
            c_tile = self.current_tile.board.board[y][x]
            if (c_tile and not c_tile.piece ):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True                
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else: 
                break
            x -= 1
            y -= 1

        # Check below-right
        x, y = self.x + 1, self.y + 1
        while (x  < 8 and y < 8):
            c_tile = self.current_tile.board.board[y][x]
            if (c_tile and not c_tile.piece):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else: 
                break
            x += 1
            y += 1

        # Check below-left
        x, y = self.x - 1, self.y + 1
        while (x  >= 0 and y < 8):
            c_tile = self.current_tile.board.board[y][x]
            if (c_tile and not c_tile.piece):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                if ((c_tile.x, c_tile.y) == (tile.x, tile.y)):
                    return True
                break
            else: 
                break
            x -= 1
            y += 1

        return False

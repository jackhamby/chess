
from game.settings import white, black, brown, width, height, bishop_icon_1, bishop_icon_2
from pieces import Piece

class Bishop(Piece):

    def __init__(self, tile, team):
        Piece.__init__(self, tile, team)


    def render(self):
        if (self.player.team == 1):
            self.current_tile.board.screen.blit(bishop_icon_1, (self.x_pos, self.y_pos))
        else:
            self.current_tile.board.screen.blit(bishop_icon_2, (self.x_pos, self.y_pos))

    def check_move(self, tile):

        available_moves = []
        # Check above-right
        x, y = self.x + 1, self.y - 1
        while (x  < 8 and y >= 0):
            c_tile = self.current_tile.board.board[y][x]
            if (c_tile and not c_tile.piece):
                available_moves.append((x, y))
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                available_moves.append((x, y))
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
                available_moves.append((x, y))
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                available_moves.append((x, y))
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
                available_moves.append((x, y))
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                available_moves.append((x, y))
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
                available_moves.append((x, y))
            elif (c_tile and c_tile.piece and c_tile.piece.player.team != self.player.team):
                available_moves.append((x, y))
                break
            else: 
                break
            x -= 1
            y += 1

        if ((tile.x, tile.y) in available_moves):
            return True


        return False
    
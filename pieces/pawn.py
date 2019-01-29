
import pygame, math
from pieces import Piece
from game.settings import white, black, brown, width, height, pawn_icon_1, pawn_icon_2


class Pawn(Piece):

    def __init__(self, tile, player):
        Piece.__init__(self, tile, player)
        self.is_first_move = True

    def render(self):
        if (self.player.team == 1):
            self.current_tile.board.screen.blit(pawn_icon_1, (self.x_pos, self.y_pos))
        else:
            self.current_tile.board.screen.blit(pawn_icon_2, (self.x_pos, self.y_pos))


    def check_move(self, tile):
        
        column, row = list(self.current_tile.id)
        available_moves = []

        direction = -1 if self.player.team == 2 else 1


        # Up
        if ((self.y + direction) < 8 and (self.y + direction) >= 0):
            above_tile = self.current_tile.board.board[self.y + direction][self.x]
            if (above_tile and not above_tile.piece):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    self.is_first_move = False
                    return True
                if (self.is_first_move and (self.y + (2 * direction)) < 8 and (self.y + (2 * direction)) >=0 ):
                    above_tile = self.current_tile.board.board[self.y + (2 * direction)][self.x]
                    if (above_tile and not above_tile.piece):
                        if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                            self.is_first_move = False
                            return True

        # Up - Right
        if ( (self.y + direction) < 8 and  (self.y + direction) >= 0 and self.x + 1 < 8):
            above_tile = self.current_tile.board.board[self.y + direction][self.x + 1]
            if (above_tile and above_tile.piece and tile.piece and tile.piece.player.team != self.player.team):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    self.is_first_move = False

                    return True

        # Up - Left
        if ( (self.y + direction) < 8 and (self.y + direction) >= 0 and self.x - 1 >= 0):
            above_tile = self.current_tile.board.board[self.y + direction][self.x - 1]
            if (above_tile and above_tile.piece and tile.piece and tile.piece.player.team != self.player.team):
                if ((above_tile.x, above_tile.y) == (tile.x, tile.y)):
                    self.is_first_move = False

                    return True


        return False

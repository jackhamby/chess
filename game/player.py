from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from network import Client, Server

class Player():

    def __init__(self, game, team):
        self.team = team
        self.game = game
        self.pieces = []
        self.selected_piece = None

    def setup(self):
        if (self.team == 1):
            self.pieces.append(Rook(self.game.board.board[0][0], self))
            self.pieces.append(Rook(self.game.board.board[0][7], self))
            self.pieces.append(Knight(self.game.board.board[0][6], self))
            self.pieces.append(Knight(self.game.board.board[0][1], self))
            self.pieces.append(Bishop(self.game.board.board[0][2], self))
            self.pieces.append(Bishop(self.game.board.board[0][5], self))
            self.pieces.append(Queen(self.game.board.board[0][4], self))
            self.pieces.append(King(self.game.board.board[0][3], self))
            for i in range(8):
                self.pieces.append(Pawn(self.game.board.board[1][i], self))
        else:
            self.pieces.append(Rook(self.game.board.board[7][0], self))
            self.pieces.append(Rook(self.game.board.board[7][7], self))
            self.pieces.append(Knight(self.game.board.board[7][1], self))
            self.pieces.append(Knight(self.game.board.board[7][6], self))
            self.pieces.append(Bishop(self.game.board.board[7][2], self))
            self.pieces.append(Bishop(self.game.board.board[7][5], self))
            self.pieces.append(Queen(self.game.board.board[7][3], self))
            self.pieces.append(King(self.game.board.board[7][4], self))
            for i in range(8):
                self.pieces.append(Pawn(self.game.board.board[6][i], self))
                
    def attack_piece(self, piece):
        opponent = self.game.player1 if self.team == 2 else self.game.player2
        if (piece in opponent.pieces):
            del opponent.pieces[opponent.pieces.index(piece)]

    def move_piece(self, tile):
        # Kill piece
        if (tile.piece):
            self.attack_piece(tile.piece)
        self.selected_piece.current_tile.piece = None
        self.selected_piece.current_tile = tile
        self.selected_piece.x = tile.x
        self.selected_piece.y = tile.y
        self.selected_piece.x_pos = tile.x_pos
        self.selected_piece.y_pos = tile.y_pos
        tile.piece = self.selected_piece
        self.selected_piece = None

    def reset_current_piece(self):
        if (self.selected_piece):
            self.selected_piece.x_pos = self.selected_piece.current_tile.x_pos
            self.selected_piece.y_pos = self.selected_piece.current_tile.y_pos

 




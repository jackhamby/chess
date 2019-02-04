import pygame, socket
from .game import Game
from network import Client
from threading import Thread

class NetworkGame(Game):


    def __init__(self, screen):
        Game.__init__(self, screen)
        self.client = Client()
        client_thread = Thread(target=self.client.start).start()
        self.running_player = None
        self.opponent = None


    def start(self):
        print('waiting for other player...')

        # Wait for game to start
        while(not self.client.last_message):
            pass 
        
        assigned_team = int(self.client.last_message.split('|')[1])
        self.running_player = self.player1 if assigned_team == 1 else self.player2
        self.opponent = self.player1 if self.running_player == self.player2 else self.player2
        print(f'started! you are player {self.running_player.team}')
        self.running = True
        self.board.setup()
        while self.running:
            if (not self.client.last_message):
                pass
            else:
                cmd = self.client.last_message.split('|')[0]

                # Game started
                if (cmd == 's' ):
                    self.client.last_message = None
                    pass

                # Opponent moved
                elif (cmd == 'm'):
                    self.handle_move()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_down(event.pos)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:     
                        self.handle_mouse_up(event.pos)
            
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event.pos)
            self.render()
            pygame.display.flip()

    def handle_move(self):
        from_x = int(self.client.last_message.split('|')[1])
        from_y = int(self.client.last_message.split('|')[2])
        to_x = int(self.client.last_message.split('|')[3])
        to_y = int(self.client.last_message.split('|')[4])
        from_tile = self.board.board[from_y][from_x]
        to_tile = self.board.board[to_y][to_x]
        self.opponent.selected_piece = from_tile.piece
        self.opponent.move_piece(to_tile)
        self.going_player = self.running_player
        self.client.last_message = None


    def handle_mouse_down(self, pos):
        tile = self.board.get_tile(pos[0], pos[1])
        # Check if is players turn
        if (tile.piece and tile.piece.player.team == self.going_player.team):

            # If network game, make sure going_player is running_player
            if (not self.running_player or (self.running_player == self.going_player)):
                self.going_player.selected_piece = tile.piece
                self.going_player.selected_piece.dragging = True
    
    def handle_mouse_up(self, pos):
        if (not self.going_player.selected_piece):
            return       
        self.going_player.selected_piece.dragging = False
        mouse_x, mouse_y = pos
        tile = self.board.get_tile(mouse_x, mouse_y)
        if (self.going_player.selected_piece.check_move(tile)):

            # Send move to server
            msg = f'm|{self.going_player.selected_piece.x}|{self.going_player.selected_piece.y}|{tile.x}|{tile.y}'
            self.client.send(msg)

            self.going_player.move_piece(tile)
            self.going_player = self.player1 if self.going_player.team == 2 else self.player2

        else:
            self.going_player.reset_current_piece()
   
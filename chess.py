
import sys, pygame, math
from game import Board, Game
from game.settings import size

### TODO
# - First pawn move 2
# - Castleing
# - Win condition

def run():
    pygame.init()
    screen = pygame.display.set_mode(size)
    game = Game(screen)
    game.start()

    while game.running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.stop()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_mouse_down(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:     
                    game.handle_mouse_up(event.pos)
        
            elif event.type == pygame.MOUSEMOTION:
                game.handle_mouse_motion(event.pos)

        game.render()

        pygame.display.flip()

if __name__ == "__main__":
    run()
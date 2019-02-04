
import sys, pygame, math
from game import Board, Game, NetworkGame
from game.settings import size

### TODO
# - Castleing
# - Win condition

def run(is_network=False):
    """
     if is_network flag is set, uses NetworkGame 
     and attempts to connect to default server. 
     otherwise, Game will be used for hotseat 2
     player game.
    """

    pygame.init()
    screen = pygame.display.set_mode(size)
    if (is_network):
        game = NetworkGame(screen)
    else:
        game = Game(screen)
    game.start()



if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        if (sys.argv[1] == "network"):
            run(True)
        else:
            print('invalid input, please try one of the following:')
            print('$ python3 chess.py')
            print('$ python3 chess.py network')
    else:

        run()
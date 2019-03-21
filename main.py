from game import world, game_start

from Boat import Boat

if __name__ == "__main__":
    boat_layer = Boat()
    world.add(boat_layer)
    game_start()

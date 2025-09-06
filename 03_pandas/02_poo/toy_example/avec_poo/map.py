
import numpy as np
class Map:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.obstacles = []

    def add_obstacle(self, x:int, y:int, obstacle)-> None:
        self.obstacles.append(((x, y), obstacle))

    def render(self)-> np.ndarray:
        # Create a 2D image of the map
        pass

    def get_terrain_type(self, x:int, y:int)-> str:
        # This method returns the type of terrain at the given coordinates
        pass


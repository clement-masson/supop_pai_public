import random


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


class Point:
    def __init__(self, x: int, y: int):
        pass

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        raise NotImplementedError("Méthode __add__ non implémentée")

    def __iadd__(self, other):
        raise NotImplementedError("Méthode __iadd__ non implémentée")

    def __sub__(self, other):
        raise NotImplementedError("Méthode __sub__ non implémentée")

    def __isub__(self, other):
        raise NotImplementedError("Méthode __isub__ non implémentée")
    
    def __eq__(self, value):
        raise NotImplementedError("Méthode __eq__ non implémentée")
    
    def __abs__(self):
        raise NotImplementedError("Méthode __abs__ non implémentée")


class Entity:
    def __init__(self, x: int, y: int, name: str):
        pass

    def __repr__(self):
        raise NotImplementedError("Méthode __repr__ non implémentée")

    def move(self, board):
        mvt = self._choose_mvt(board) # Choisir un déplacement
        if mvt:
            self._prev_pos = Point(self.pos.x, self.pos.y)  # Sauvegarder la position précédente
            self.pos += mvt  # Appliquer le déplacement
            # print(f"{self.name} chose {mvt} and moved to {self.pos}")
        if self._can_eat:
            for entity in board.entities:
                if (entity is not self) and (entity.pos == self.pos):
                    return entity  # Manger l'entité
        return None # Ne pas manger d'entité par défaut

    def _choose_mvt(self, board):
        raise NotImplementedError("Méthode _choose_mvt non implémentée")


class Board:
    def __init__(self, width: int, height: int):
        pass

    def is_obstacle_free(self, point: Point):
        return (0 <= point.x < self.width) and (0 <= point.y < self.height)
    
    def add_entity(self, entity: Entity):
        raise NotImplementedError("Méthode add_entity non implémentée")
    
    def run_one_step(self):
        raise NotImplementedError("Méthode run_one_step non implémentée")

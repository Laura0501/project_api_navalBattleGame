from model.ship import Ship


class ShipDistribution:
    def __init__(self, places:[], ship:Ship, orientation:int, state:str):
        self.places=places
        self.ship=ship
        self.orientation=orientation
        self.state=state
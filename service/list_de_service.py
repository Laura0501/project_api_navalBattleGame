from model.list_de import ListDe
from model.ship import Ship

class ListDeService:

    def __init__(self):
        self.ships = ListDe()

    def get_all_ships(self):
        return self.ships.get_all_ships()

    def add_ship(self, data):
        ship=Ship(data)
        self.ships.add_ship(ship)

    def add_to_start_ship(self, data):
        ship = Ship(data)
        self.students.add_to_start_de(ship)

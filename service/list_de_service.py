from model.list_de import ListDe
from model.ship import Ship
from model.ship_distribution import ShipDistribution

class ListDeService:

    def __init__(self):
        self.list_de = ListDe()

    def get_all_ships_distribution(self):
        if self.list_de.head==None:
            return{"message":"La lista esta vacia"}
        else:
            return self.list_de.get_all_ships_distribution()

    def add_ship_distribution(self, data:Ship):
        ship_distribution = ShipDistribution(data)
        self.list_de.add_ship_distribution(ship_distribution)
        return {"message":"Barco adicionado exitosamente"}

    def add_to_start_ship_distribution(self, data):
        ship_distribution = ShipDistribution(data)
        self.list_de.add_to_start_ship_distribution(ship_distribution)

    def clone_list(self):
        return self.list_de.clone_list().get_all_ships()

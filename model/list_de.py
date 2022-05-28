from model.node_de import NodeDe
from .ship_distribution import ShipDistribution


class ListDe:
    def __init__(self):
        self.head=None
        self.count=0

    def get_all_ships_distribution(self):
        list=[]
        temp=self.head
        while temp != None:
            list.append(temp.data)
            temp=temp.next
        return list


    def add_ship_distribution(self, data:ShipDistribution):
        if self.head == None:
            self.head = NodeDe(data)

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = NodeDe(data)
            temp.next.previous = temp
        self.count += 1

    def add_to_start_ship_distribution(self, data:ShipDistribution):
        if self.head == None:
            self.head = NodeDe(data)
        else:
            self.head.previous=NodeDe(data)
            self.head.previous.next=self.head
            self.head=self.head.previous
        self.count += 1


    def clone_list(self):
        list = ListDe()
        temp = self.head
        while temp != None:
            list.add_ship_distribution(temp.data)
            temp = temp.next
        return list

    def validate_coordinate_list_de(self, coordinates:[]):
        temp = self.head
        while temp != None:
            try:
                for coordinate in range(len(coordinates)):
                    if ShipDistribution(temp).define_location(coordinate['x'],coordinate['y'], coordinate['orientation']):
                        coordinates.state= True
                temp = temp.next

            except:
                raise Exception({"Coordenadas invalidas para ubicar el barco"})



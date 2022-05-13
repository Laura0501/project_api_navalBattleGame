from model.node_de import NodeDe


class ListDe:
    def __init__(self):
        self.head=None
        self.count=0

    def get_all_ships(self):
        list=[]
        temp=self.head
        while temp != None:
            list.append(temp.data)
            temp=temp.next

        list.append(temp)
        return list


    def add_ship(self, data):
        if self.head == None:
            self.head = NodeDe(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            new_node = NodeDe(data)
            temp.next = new_node
            new_node.previous = temp
        self.count += 1

    def add_to_start_ship(self, data):
        if self.head == None:
            self.head = NodeDe(data)
        else:
            temp = NodeDe(data)
            temp.next = self.head
            self.head.previous = temp
            self.head=temp
        self.count += 1
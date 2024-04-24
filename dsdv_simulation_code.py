class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}  # format: {destination: (cost, next_hop)}

    def add_neighbor(self, neighbor, cost):
        self.routing_table[neighbor.name] = (cost, neighbor.name)

    def receive_update(self, from_node):
        updated = False
        for destination, (cost, next_hop) in from_node.routing_table.items():
            if destination == self.name:
                continue
            new_cost = cost + self.routing_table[from_node.name][0]
            if destination not in self.routing_table or new_cost < self.routing_table[destination][0]:
                self.routing_table[destination] = (new_cost, from_node.name)
                updated = True
        if updated:
            self.send_update()

    def send_update(self):
        for neighbor in self.neighbors:
            neighbor.receive_update(self)

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

def simulate_network():
    # Create nodes
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    # Set neighbors and costs
    a.set_neighbors([b, d])
    a.add_neighbor(b, 1)
    a.add_neighbor(d, 4)
    b.set_neighbors([a, c])
    b.add_neighbor(a, 1)
    b.add_neighbor(c, 2)
    c.set_neighbors([b, d])
    c.add_neighbor(b, 2)
    c.add_neighbor(d, 1)
    d.set_neighbors([a, c])
    d.add_neighbor(a, 4)
    d.add_neighbor(c, 1)

    # Initial routing table updates
    a.send_update()
    b.send_update()
    c.send_update()
    d.send_update()

    # Print routing tables
    for node in [a, b, c, d]:
        print(f"Routing table for {node.name}: {node.routing_table}")

if __name__ == '__main__':
    simulate_network()
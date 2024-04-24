
# DSDV Routing Protocol Simulation

This repository contains a Python implementation of the Destination-Sequenced Distance Vector (DSDV) routing protocol, designed to simulate the behavior of DSDV in a network with predefined nodes and connections.

## Overview

The DSDV routing protocol is a table-driven routing scheme for ad-hoc mobile networks based on the Bellman-Ford algorithm. It aims to provide a robust and efficient routing system. This simulation is a basic model, demonstrating the core concepts of DSDV including routing table updates and routing table maintenance through periodic and triggered updates.

## Features

- Simulation of four nodes (A, B, C, D)
- Ability to set initial neighbors and link costs
- Periodic and triggered updates based on routing table changes
- Console output of routing tables for each node to visualize the simulation

## Requirements

The script requires Python 3.x. No external libraries are needed, and it can be run on any standard Python environment.

## Usage

To run the simulation, navigate to the directory containing the script and run:

```bash
python dsdv_simulation_code.py
```

This command will execute the simulation, and the final routing tables for each node will be displayed in the console, showing the costs and next hops for each destination.

## Simulation Setup

The network setup includes four nodes configured with specific neighbors and link costs as follows:

- Node A is connected to Node B and Node D.
- Node B is connected to Node A and Node C.
- Node C is connected to Node B and Node D.
- Node D is connected to Node A and Node C.

The cost of each link is defined in the `simulate_network` function, which can be adjusted as per requirement to test different scenarios.

## Understanding the Code

### Class `Node`

- `__init__(self, name)`: Constructor to initialize the node with a given name.
- `add_neighbor(self, neighbor, cost)`: Adds a neighbor and the cost of the link to this node.
- `receive_update(self, from_node)`: Processes routing table updates received from neighbors.
- `send_update(self)`: Sends the current routing table to all neighbors.
- `set_neighbors(self, neighbors)`: Sets the list of neighbor nodes for this node.

### Function `simulate_network()`

- This function sets up the network, initializes nodes, sets neighbors, and triggers the first set of updates to build the routing tables.

## Modifying the Simulation

To customize the simulation, you can modify the `simulate_network` function. This includes changing the number of nodes, the connections between them, and the costs associated with each link.

## Conclusions

The output will show the evolution of routing tables as the nodes exchange information. This simulation is an educational tool to understand how DSDV works in a controlled environment.

---

Feel free to adjust the content according to your specific needs or to add more sophisticated functionalities to the simulation script!

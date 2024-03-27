This is an algorithm project created by Omied Muhebi and Caroline Nkan
Graph Class Definition:

The Graph class represents an undirected graph and contains methods for adding nodes, adding edges between nodes, displaying the graph, and finding the shortest path using Dijkstra's algorithm.
Constructor (__init__):

Initializes an empty dictionary adj_list to store the adjacency list representation of the graph.
add_node Method:

Adds a node to the graph if it's not already present. It initializes the adjacency list for the new node with an empty list.
add_edge Method:

Adds an edge between two nodes with the specified weight.
Checks if both nodes are present in the graph's adjacency list.
Adds the second node and weight as a tuple to the adjacency list of the first node.
Since this is an undirected graph, it also adds the first node and weight to the second node's list.
display_graph Method:

Prints the adjacency list representation of the graph, showing each node and its connected nodes with corresponding weights.
dijkstra_shortest_path Method:

Implements Dijkstra's algorithm to find the shortest path from a specified starting node to all other nodes in the graph.
It initializes a dictionary distances to keep track of the shortest distance from the start node to each node in the graph. All distances are initialized to infinity except for the start node, which is set to 0.
It initializes a priority queue pq to store nodes and their tentative distances from the start node.
The algorithm iterates until the priority queue is empty:
It pops the node with the smallest tentative distance from the priority queue.
It iterates through the neighbors of the current node and calculates the tentative distance from the start node to each neighbor through the current node.
If the calculated distance is smaller than the current distance recorded in the distances dictionary, it updates the distance and pushes the neighbor and its new tentative distance into the priority queue.
Finally, it returns the distances dictionary containing the shortest distances from the start node to all other nodes.
Creating an Instance of the Graph Class (graph = Graph()):

Creates an instance of the Graph class.
Adding Nodes and Edges to the Graph:

Adds nodes "A" to "W" to the graph using the add_node method.
Adds edges between nodes with specified weights using the add_edge method.
Displaying the Graph (graph.display_graph()):

Displays the adjacency list representation of the graph.
Finding Shortest Paths Using Dijkstra's Algorithm:

Finds the shortest paths from node "A" to all other nodes in the graph using the dijkstra_shortest_path method.
Prints the shortest paths from node "A" to all other nodes along with their distances.

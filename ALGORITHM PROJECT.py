# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:50:16 2024

@author: User
"""

import heapq

 

class Graph:
   def __init__(self):


       # Initialize an empty dictionary to store the adjacency list
       self.adj_list = {}

   def add_node(self, node):


       # Add a node to the graph if it's not already present
       if node not in self.adj_list:


           # Initialize the adjacency list for the new node with an empty list
           self.adj_list[node] = []

   def add_edge(self, node1, node2, weight):


       # Add an edge between two nodes with the specified weight
       if node1 in self.adj_list and node2 in self.adj_list:


           # Add the second node and weight as a tuple to the adjacency list of the first node
           self.adj_list[node1].append((node2, weight))


           # Since this is an undirected graph, also add the first node and weight to the second node's list
           self.adj_list[node2].append((node1, weight))
       else:


           # If either of the nodes does not exist, print an error message
           print(f"One or both of the nodes {node1}, {node2} are not present in the graph.")

   def display_graph(self):


       # Print the adjacency list representation of the graph
       for node in self.adj_list:


           # For each node, print the node and its connected nodes with corresponding weights
           print(f"{node}: {self.adj_list[node]}")

   def dijkstra_shortest_path(self, start):


       # Initialize distances dictionary to keep track of the shortest distance from start to each node
       distances = {node: float('inf') for node in self.adj_list}
       distances[start] = 0

 

       # Initialize priority queue to store nodes and their tentative distances from start
       pq = [(0, start)]

       while pq:


           # Pop the node with the smallest tentative distance from the priority queue
           current_distance, current_node = heapq.heappop(pq)

 

           # Check if the current node's distance is already smaller than the current tentative distance
           if current_distance > distances[current_node]:
               continue

 

           # Iterate through the neighbors of the current node
           for neighbor, weight in self.adj_list[current_node]:


               # Calculate the tentative distance from start to the neighbor through the current node
               distance = current_distance + weight

 

               # Update the distance if it's smaller than the current distance recorded
               if distance < distances[neighbor]:
                   distances[neighbor] = distance


                   # Push the neighbor and its new tentative distance into the priority queue
                   heapq.heappush(pq, (distance, neighbor))

       return distances


# Create an instance of the Graph class
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_node("H")
graph.add_node("I")
graph.add_node("J")
graph.add_node("K")
graph.add_node("L")
graph.add_node("M")
graph.add_node("N")
graph.add_node("O")
graph.add_node("P")
graph.add_node("Q")
graph.add_node("R")
graph.add_node("S")
graph.add_node("T")
graph.add_node("U")
graph.add_node("V")
graph.add_node("W")


graph.add_edge("A", "B", 6)
graph.add_edge("A", "F", 5)
graph.add_edge("B", "G", 6)
graph.add_edge("B", "C", 5)
graph.add_edge("C", "G", 6)
graph.add_edge("F", "G", 8)
graph.add_edge("C", "D", 7)
graph.add_edge("D", "E", 7)
graph.add_edge("E", "I", 6)
graph.add_edge("I", "M", 10)
graph.add_edge("J", "O", 7)
graph.add_edge("K", "L", 7)
graph.add_edge("L", "P", 7)
graph.add_edge("M", "N", 9)
graph.add_edge("N", "R", 7)
graph.add_edge("O", "P", 13)
graph.add_edge("P", "U", 11)
graph.add_edge("U", "V", 8)
graph.add_edge("V", "W", 5)
graph.add_edge("R", "W", 10)
graph.add_edge("Q", "P", 8)
graph.add_edge("S", "T", 9)
graph.add_edge("H", "G", 9)
graph.add_edge("G", "K", 8)
graph.add_edge("H", "I", 12)
graph.add_edge("I", "D", 8)

 

graph.display_graph()
 

# Find the shortest path from node "A" using Dijkstra's algorithm
shortest_paths = graph.dijkstra_shortest_path("A")

 

# Print the shortest paths from node "A" to all other nodes
print("Shortest paths from node A:")
for node, distance in shortest_paths.items():
   print(f"To node {node}: Distance = {distance}")
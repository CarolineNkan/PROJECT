import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Initializes an empty dictionary to represent the adjacency list of the graph

    def add_edge(self, from_node, to_node, weight):
        # Adds a directed edge from from_node to to_node with the specified weight to the adjacency list
        if from_node not in self.adjacency_list:
            self.adjacency_list[from_node] = []  # If from_node is not in adjacency_list, initialize it with an empty list
        self.adjacency_list[from_node].append((to_node, weight))  # Append the to_node and weight as a tuple to from_node's list

    def full_network_data(self):
        # This function creates the full network based on the provided data and adds the corresponding edges
        # The dictionary network_data represents the full graph with nodes and weighted edges
        network_data = {
            # Each key-value pair in network_data represents a node and its connections (edges) to other nodes with weights
            # 'Node': {'ConnectedNode1': weight1, 'ConnectedNode2': weight2, ...}
            'A': {'B': 6, 'F': 5},
            'B': {'A': 6, 'G': 6},
            'C': {'B': 5, 'D': 7, "H": 5},
            'D': {'C': 7, 'E': 7, "I": 8},
            'E': {'D': 7, 'I': 6, "N": 15},
            'F': {'A': 5, 'G': 8, "J": 7},
            'G': {'B': 6, 'F': 8, "H": 9, "K": 8},
            'H': {'C': 5, 'G': 9, "I": 12},  # charging station
            'I': {'D': 8, 'E': 6, "H": 12, "M": 10},
            'J': {'F': 7, 'K': 5, "O": 7},
            'K': {'G': 8, 'J': 5, "L": 7},  # charging station
            'L': {'K': 7, 'M': 7, "P": 7},
            'M': {'I': 10, 'L': 7, "N": 9},
            'N': {'E': 15, 'M': 9, "R": 7},
            'O': {'J': 7, 'P': 13, "S": 9},
            'P': {'L': 7, 'O': 13, "Q": 8, "U": 11},
            'Q': {'P': 8, 'R': 9},  # charging station
            'R': {'N': 7, "Q": 9, "W": 10},
            'S': {'O': 9, 'T': 9},
            'T': {'S': 9, 'U': 8},  # charging station
            'U': {'P': 11, 'T': 8, "V": 8},
            'V': {'U': 8, 'W': 5},
            'W': {'R': 10, 'V': 5}
        }

        for from_node, edges in network_data.items():
            for to_node, weight in edges.items():
                self.add_edge(from_node, to_node, weight)  # Adds each edge in the network_data to the graph

    def dijkstra(self, start):
        queue = [(0, start, [])]  # Initializes the priority queue with a tuple containing the distance, start node, and an empty path
        visited = {}  # Initializes an empty dictionary to keep track of visited nodes and their distances
        paths = {}  # Initializes an empty dictionary to store the shortest paths to each node
        while queue:
            # Extracts the node in the queue with the smallest distance (current node)
            current_distance, current_node, current_path = heapq.heappop(queue)
            if current_node not in visited:
                visited[current_node] = current_distance  # Marks the current node as visited with the current distance
                current_path = current_path + [current_node]  # Adds the current node to the current path
                paths[current_node] = current_path  # Stores the current path in the paths dictionary
                for neighbor, weight in self.adjacency_list.get(current_node, []):
                    # For each neighbor of the current node, if it's not visited, add it to the queue with the updated distance and path
                    if neighbor not in visited:
                        heapq.heappush(queue, (current_distance + weight, neighbor, current_path))
        return visited, paths  # Returns the visited dictionary with distances and paths dictionary with shortest paths


    def shortest_paths_to_stations(self, start, charging_stations):
        distances, paths = self.dijkstra(start)  # Runs Dijkstra's algorithm from the start node
        station_paths = {}  # Initializes an empty dictionary to store paths to charging stations
        for station in charging_stations:
            if station in paths:
                # For each charging station, store its distance and path if it's reachable
                station_paths[station] = (distances[station], paths[station])
        return station_paths  # Returns the dictionary containing paths to the charging stations

    def recommend_efficient_route(self, start, charging_stations):
        # This function recommends the most efficient route to the nearest charging station
        station_paths = self.shortest_paths_to_stations(start,
                                                        charging_stations)  # Gets shortest paths to all charging stations
        recommended_station = None  # Initializes recommended_station with None
        min_distance = float('inf')  # Initializes min_distance with infinity
        for station, (distance, path) in station_paths.items():
            # Prints each charging station with its distance and path from the start node
            print(f"Charging station {station}: Distance = {distance}, Path = {path}")
            if distance < min_distance:
                # If the current station's distance is smaller than min_distance, update the recommended_station and min_distance
                min_distance = distance
                recommended_station = (station, path)
        print("\nRecommended Charging Station:")
        # Prints the recommended charging station with the shortest distance and path
        print(f"Charging station {recommended_station[0]}: Distance = {min_distance}, Path = {recommended_station[1]}")
        return recommended_station  # Returns the recommended charging station and path


graph = Graph()  # Instantiate the Graph object
graph.full_network_data()  # Populate the graph with the network data

charging_stations = {'H', 'K', 'Q', 'T'}  # Set of charging stations
start_node = 'W'  # Start node

# Call the recommend_efficient_route function to find and print the most efficient route to the nearest charging station
graph.recommend_efficient_route(start_node, charging_stations)



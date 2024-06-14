#Breadth-first search
def bfs(graph, start_node):
    visited = set()         # To keep track of visited nodes
    queue = [start_node]    # Initialize the queue with the start node
    result = []             # To store the BFS traversal order
    
    while queue:
        node = queue.pop(0)  # Dequeue a node from the front of the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            result.append(node)  # Append it to the result list
            
            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
    return result

# Define the graph using an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define the start node for BFS traversal
start_node = 'A'

# Print the result of BFS traversal
print("BFS Traversal starting from node A:")
print(bfs(graph, start_node))
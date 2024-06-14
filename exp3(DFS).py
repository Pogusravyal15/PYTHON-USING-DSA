#Depth-first search
def dfs(graph, start_node):
    visited = set()         # To keep track of visited nodes
    stack = [start_node]    # Initialize the stack with the start node
    result = []             # To store the BFS traversal order
    
    while stack:
        node = stack.pop()  # Destack a node from the front of the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            result.append(node)  # Append it to the result list
            
            # Enstack all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
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
print("DFS traversal order:", dfs(graph, start_node))

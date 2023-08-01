# Ozner Leyva Mariscal A01742377
# Carolina González Leal A01284948
# Erick Siller Ojeda A01382929
# Valeria Enríquez Limón A00832782
# Santiago Martínez Vallejo A00571878
from collections import deque

def read(file_path):
  graph = {}

  with open(file_path, 'r') as file:
    line = file.readline().strip()  # Read the first line
    line = line.replace(' ', '')  # Remove any whitespace
    line = line[1:-1]  # Remove the surrounding parentheses

    edges = line.split('),(')  # Split the line into edges

    for edge in edges:
      nodeFrom, nodeTo = edge.split(',')
      nodeFrom = nodeFrom.strip('(')
      nodeTo = nodeTo.strip(')')

      if nodeFrom in graph:
        graph[nodeFrom].append(nodeTo)
      else:
        graph[nodeFrom] = [nodeTo]

  return graph


def bfs(graph, start_node):
  visited = []
  queue = deque([start_node])
  visited.append(start_node)

  while queue:
    print("Nodes in the queue: ", list(queue))
    node = queue.popleft()
    print("Visiting the node: ", node)
    print("Visited nodes: ", visited, " \n")

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.append(neighbor)
        
graph = read("bfs.txt")
startNode = '1'

print("BFS Traversal: \n")
bfs(graph, startNode)

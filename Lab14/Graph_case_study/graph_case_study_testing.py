from graph import LinkedEdge, LinkedDirectedGraph, LinkedVertex
from algorithms import dfs, bfs, topoSort
from linkedstack import LinkedStack
def read_file(file_name):
    """
    Reads a file and build a graph
    """
    with open(file_name, 'r') as f:
        graph = LinkedDirectedGraph()
        for line in f.readlines()[1:]:
            destination, origin = line.split(' (')
            origin = origin[:-2]
            if ',' in origin:
                origin = origin.split(', ')
                graph.addUniqueVertex(destination)
                for i in origin:
                    if i != 'none':
                        graph.addUniqueVertex(i)
                        graph.addEdge(i, destination, weight=1)
            elif origin != 'none':
                graph.addUniqueVertex(origin)
                graph.addUniqueVertex(destination)
                graph.addEdge(origin, destination, weight=1)
            else:
                graph.addUniqueVertex(destination)
    return graph

if __name__ == '__main__':
    graph = read_file('stanford_cs.txt')
    bfs_stack = bfs(graph, 'MATH19')
    dfs_stack = dfs(graph, 'CS106A')
    print('bfs:', bfs_stack)
    print('dfs:', dfs_stack)
    topological = topoSort(graph)
    print('topological sort:', topological)
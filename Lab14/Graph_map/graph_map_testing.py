from graph import Graph
from bfs import BFS_complete
from dfs import DFS_complete
from topological_sort import topological_sort

def read_file(path):
    '''reads file and build a graph'''
    with open(path) as file:
        lines = file.readlines()
        graph = Graph(directed=True)
        for line in lines[1:]:
            destination, origin = line.split(' (')
            origin = origin[:-2]

            if ',' in origin:
                origin = origin.split(', ')
                destination = graph.insert_unique_vertex(destination)
                for i in origin:
                    if i != 'none':
                        i = graph.insert_unique_vertex(i)
                        graph.insert_edge(i, destination)

            elif origin != 'none':
                origin = graph.insert_unique_vertex(origin)
                destination = graph.insert_unique_vertex(destination)
                graph.insert_edge(origin, destination)

            else:
                graph.insert_unique_vertex(destination)
    return graph

def bfs_test(graph):
    '''tests bfs'''
    bfs_tree = BFS_complete(graph)
    print(bfs_tree)
    return bfs_tree

def dfs_test(graph):
    '''tests dfs'''
    dfs_tree = DFS_complete(graph)
    print(dfs_tree)
    return dfs_tree

def test_topological_sort(graph):
    '''tests topological sort'''
    topological = topological_sort(graph)
    print(topological)
    return topological

if __name__ == '__main__':
    graph = read_file('stanford_cs.txt')
    bfs_test(graph)
    dfs_test(graph)
    test_topological_sort(graph)

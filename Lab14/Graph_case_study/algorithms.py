"""
File: algorithms.py

Graph processing algorithms
"""

from linkedstack import LinkedStack
from linkedqueue import LinkedQueue


def topoSort(g, startLabel=None):
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs_recurse(g, v, stack)
    return stack


def dfs_recurse(g, v, dfs_stack):
    v.setMark()
    dfs_stack.push(v.getLabel())
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs_recurse(g, w, dfs_stack)


def dfs(g, startLabel):
    g.clearVertexMarks()
    dfs_stack = LinkedStack()
    start = g.getVertex(startLabel)
    dfs_recurse(g, start, dfs_stack)
    return dfs_stack


def bfs(g, startLabel):
    '''breath-first search'''
    queue = LinkedQueue()
    bfs_vertices = LinkedStack()
    g.clearVertexMarks()
    start = g.getVertex(startLabel)
    queue.add(start)
    while not queue.isEmpty():
        v = queue.pop()
        if not v.isMarked():
            v.setMark()
            bfs_vertices.push(v.getLabel())
            for adjacent in g.neighboringVertices(v.getLabel()):
                queue.add(adjacent)
    return bfs_vertices


def shortestPaths(g, startLabel):
    # Exercise
    return ["Under development"]

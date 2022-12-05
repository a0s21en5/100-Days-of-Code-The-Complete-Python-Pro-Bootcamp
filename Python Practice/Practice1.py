from collections import defaultdict
graph = defaultdict(list)


def addedge(graph, u, v):
    graph[u].append(v)


def edge(graph):
    edge1 = []
    for vex in graph:
        for fri in graph[vex]:
            edge1.append((vex, fri))
    return edge1


addedge(graph, 'a', 'c')
addedge(graph, 'b', 'a')
addedge(graph, 'b', 'c')
addedge(graph, 'b', 'c')
addedge(graph, 'c', 'd')
addedge(graph, 'c', 'e')
print(edge(graph))

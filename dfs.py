def DFS(graph, vertex, stack, net):
    stack.append(vertex)

    for v in graph[vertex]:
        if v not in stack:
            net.add_edge(vertex, to=v)
            DFS(graph, v, stack, net)
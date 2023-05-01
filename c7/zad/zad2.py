class Node:
    def __init__(self, name, weight, neighbourNames):
        self.name = name
        self.weight = weight
        self.neighbourNames = neighbourNames

    def __str__(self):
        return "{}-{}".format(self.name, self.weight)


class Graph:
    def __init__(self, nodes, showSteps=False):
        self.nodes = nodes
        self.showSteps = showSteps

    def countDistancesFor(self, startNodeName):
        distances, unvisitedNodes = {}, [node for node in nodes]
        for node in self.nodes:
            distances[node.name] = float("inf")
        distances[startNodeName] = 0

        while unvisitedNodes:
            currentNode = None
            for node in unvisitedNodes:
                if currentNode is None or distances[node.name] < distances[currentNode.name]:
                    currentNode = node
            unvisitedNodes.remove(currentNode)

            for neighbourName in currentNode.neighbourNames:
                distance = distances[currentNode.name] + currentNode.weight
                if distance < distances[neighbourName]:
                    distances[neighbourName] = distance
        return distances


nodes = [
    Node('A', 2, {'B', 'C'}),
    Node('B', 4, {'A', 'F', 'E'}),
    Node('C', 1, {'A', 'D'}),
    Node('D', 3, {'C'}),
    Node('F', 2, {'B'}),
    Node('E', 3, {'B'})
]
graph = Graph(nodes, showSteps=True)
print(graph.countDistancesFor("A"))

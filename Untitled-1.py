import re
import sys

class GraphGet:

    def __init__(self):
        kwargs = {
            x.split('=')[0] : x.split('=') for x in sys.argv
        }
        with open(kwargs['filepath'][1], 'r') as f:
            text = f.readlines()
            self.nodes = [int(i) for i in re.split(' ', text[0])]
            self.ribs = [[int(i) for i in re.split(',', i)] for i in re.split(' ', text[1])]

    # def writeGraph(self, ribs, nodes):
    #     with open('C://Users/Oleg/Desktop/file.txt', 'w') as f:
    #         f.write(f'{nodes}\n{ribs}')

    # def rewriteGraph(self, ribs, nodes):
    #     with open('C://Users/Oleg/Desktop/file.txt', 'w') as f:
    #         f.write(f'{nodes}\n{ribs}')


class RibsEdit(GraphGet):
        
    def getRibs(self):
        return self.ribs

    def deleteRibs(self, node_1, node_2):
        try:
            self.ribs.remove([node_1, node_2])
        except ValueError: 
            raise 'Такого ребра нет'

    def addRibs(self, node_1, node_2):
        if [node_1, node_2] in self.ribs:
            print('Такое ребро уже есть')
        else:
            self.ribs.append([node_1, node_2])


class NodesEdit(GraphGet):

    def getNodes(self):
        return self.nodes

    def deleteNodes(self, node):
        try:
            self.nodes.remove(node)
            for i in range(len(self.ribs)-1,-1,-1):
                if node in self.ribs[i]:
                    self.ribs.remove(self.ribs[i])
        except ValueError:
            raise 'Такой вершины нет'

    def addNodes(self, node):
        self.nodes.append(node)


class ListNeig(RibsEdit, NodesEdit):
    visited = set()
    queue = 0
    graph = {}
    Q = []  
    BFS = []

    # @classmethod
    def getList(self):
        print(self.ribs)
        for i in self.nodes:
            for j in self.ribs:
                if i in j:
                    if i in self.graph.keys():
                        self.graph[i] += [x for x in j if x!=i and x not in self.graph[i]]
                    else: 
                        self.graph[i] = [x for x in j if x!=i]
                
        print(self.graph)
        return self.graph
    
            
    def getGlubSearch(self, root):
        # graph = self.getList()
        if root in self.visited:  
            return
        self.visited.add(root) 
        for i in self.graph[root]:
            if not i in self.visited:
                self.getGlubSearch(i)
                
    def getShirSearch(self, root):
        graph = self.getList()
        print(graph)
        if root in self.visited:  
            return
        self.visited.add(root) 
        self.BFS.append(root) 
        for i in graph[root]:  
            if not i in self.visited:
                self.Q.append(i)
        while self.Q:
            self.getShirSearch(self.Q.pop(0))
        

class MatrNeig(RibsEdit, NodesEdit):

    # @classmethod
    def getMatr(self):
        matr = [[0 for i in self.nodes] for i in self.nodes]
        for i in self.ribs:
            m = int(i[0])
            n = int(i[1])
            matr[m][n] = 1
            matr[n][m] = 1
        return matr

if __name__ == "__main__":
    graph = ListNeig()
    print(graph.getList())
    graph.addRibs(7,10)
    print(graph.getList())





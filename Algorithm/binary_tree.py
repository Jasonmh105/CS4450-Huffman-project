class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.word = ""
        self.weight = 0

    def set_word(self, word):
        self.word = word

    def set_weight(self, weight):
        self.weight = weight

    def get_word(self):
        return self.word
    
    def get_weight(self):
        return self.weight
    
    # Displayes raw data of called node and all those under it in DFS
    def __str__(self):
        return f'node({self.left}, {self.right}, {self.word}, {self.weight})'

class BinaryTree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root
    
    def tuples_to_nodes(self, tuples):

        nodes = []
        for each in tuples:
            new_node = Node()
            new_node.set_word(each[0])
            new_node.set_weight(each[1])
            nodes.append(new_node)

        return nodes
    
    def merge(self, node1, node2):
        new_root = Node()
        new_root.left = node1
        new_root.right = node2
        new_root.set_weight(node1.get_weight() + node2.get_weight())

        return new_root
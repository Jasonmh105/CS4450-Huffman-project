class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.word = ""
        self.weight = 0

    def setWord(self, word):
        self.word = word

    def setWeight(self, weight):
        self.weight = weight

    def getWord(self):
        return self.word
    
    def getWeight(self):
        return self.weight
    
    # Displayes raw data of called node and all those under it in DFS
    def __str__(self):
        return f'node({self.left}, {self.right}, {self.word}, {self.weight})'

class BinaryTree():
    def __init__(self):
        self.root = None

    # Handle new node in huffman tree
    def insert(self, tuple):

        # New node is formed from given tuple
        newNode = Node()
        newNode.setWord(tuple[0])
        newNode.setWeight(tuple[1])
        
        # New root is generated, old root becomes the left child of the new root, inserted node becomes the right child
        newRoot = Node()
        newRoot.setWeight(self.root.getWeight()+newNode.getWeight())
        newRoot.left = self.root
        newRoot.right = newNode
        self.root = newRoot
        print("PRINTING NODES AT INSERTION:         ", self.root)

    # Generate tree root and nodes
    def startTree(self, tuple1, tuple2):

        # Start with clean root node, weight is sum of child nodes
        self.root = Node()
        self.root.left = Node()
        self.root.right = Node()
        self.root.weight = tuple1[1]+tuple2[1]

        # Tuple1 becomes root's left child node
        self.root.left.setWord(tuple1[0])
        self.root.left.setWeight(tuple1[1])

        # Tuple2 becomes root's left child node
        self.root.right.setWord(tuple2[0])
        self.root.right.setWeight(tuple2[1])

        print("PRINTING NODES AT GENERATION:        ", self.root)
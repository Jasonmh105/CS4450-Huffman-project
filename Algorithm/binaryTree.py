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
        newNode = Node()
        newNode.setWord(tuple[0])
        newNode.setWeight(tuple[1])
        #continue with insertion logic

    # Generate tree root and nodes
    def startTree(self, tuple1, tuple2):
        self.root = Node()
        self.root.left = Node()
        self.root.right = Node()
        self.root.weight = tuple1[1]+tuple2[1]

        self.root.left.setWord(tuple1[0])
        self.root.left.setWeight(tuple1[1])

        self.root.right.setWord(tuple2[0])
        self.root.right.setWeight(tuple2[1])

        print(self.root)
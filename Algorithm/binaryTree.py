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

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, tuple):
        newNode = Node()
        newNode.setWord(tuple[0])
        newNode.setWeight(tuple[1])
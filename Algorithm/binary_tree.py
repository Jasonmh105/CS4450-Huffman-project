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

    # Handle new node in huffman tree
    def insert(self, tuple):

        if(self.root is None):
            raise TypeError("CANNOT INSERT BEFORE GENERATING A TREE, TRY USING start_tree() INSTEAD")
        else:
            # New node is formed from given tuple
            new_node = Node()
            new_node.set_word(tuple[0])
            new_node.set_weight(tuple[1])
            
            # New root is generated, old root becomes the left child of the new root, inserted node becomes the right child
            new_root = Node()
            new_root.set_weight(self.root.get_weight()+new_node.get_weight())
            new_root.left = self.root
            new_root.right = new_node
            self.root = new_root
            print("PRINTING NODES AT INSERTION:         ", self.root)

    # Generate tree root and nodes
    def start_tree(self, tuple1, tuple2):

        # Start with clean root node, weight is sum of child nodes
        self.root = Node()
        self.root.left = Node()
        self.root.right = Node()
        self.root.weight = tuple1[1]+tuple2[1]

        # Tuple1 becomes root's left child node
        self.root.left.set_word(tuple1[0])
        self.root.left.set_weight(tuple1[1])

        # Tuple2 becomes root's left child node
        self.root.right.set_word(tuple2[0])
        self.root.right.set_weight(tuple2[1])

        print("PRINTING NODES AT GENERATION:        ", self.root)

    # def merge(tuple1, tuple2):
    #     # Start with clean root node, weight is sum of child nodes
    #     root = Node()
    #     root.left = Node()
    #     root.right = Node()
    #     root.weight = tuple1[1]+tuple2[1]

    #     if(type(tuple1[0]) == "<class 'str'>"):
    #         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #     else:
    #         root.left = tuple1[0]

    #     print(type(tuple2[0]))
    #     if(type(tuple2[0]) == "<class 'str'>"):
    #         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #     else:
    #         root.right = Node()
    #         root.right.set_word(tuple2[0])
    #         root.right.set_weight(tuple2[1])

    #     return root
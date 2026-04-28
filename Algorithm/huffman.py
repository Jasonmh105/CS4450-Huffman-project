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
    
    # operator overloading so that nodes can be compared
    def __lt__(self, other):
        return self.get_weight() < other.get_weight()
    def __gt__(self, other):
        return self.get_weight() > other.get_weight()

def tuples_to_nodes(tuples):

        nodes = []
        for each in tuples:
            new_node = Node()
            new_node.set_word(each[0])
            new_node.set_weight(each[1])
            nodes.append(new_node)

        return nodes

def merge(node1, node2):
        new_root = Node()
        new_root.left = node1
        new_root.right = node2
        new_root.set_weight(node1.get_weight() + node2.get_weight())

        return new_root

def pre_order_search(root, code_list, current_code):

    # Leaf node is reached
    if root.left is None and root.right is None:
        code_list.append((root.word, root.get_weight(),current_code))
        return
        
    pre_order_search(root.left, code_list, current_code + "0")
    pre_order_search(root.right, code_list, current_code + "1")

def huffman_algorithm(tuples):
    
    # Sort tuples by frequency
    tuples_sorted = sorted(tuples, key=lambda element: element[1])
    print(tuples_sorted, "\n")

    # Convert each tuple to a tree node
    node_list = tuples_to_nodes(tuples_sorted)

    # Recursivly merge nodes until only one is left
    while(len(node_list) > 1):
        # Make new root node from first 2 in node_list, then remove merged nodes, reinsert new root, and sort
        # print(huffman_tree.merge(node_list[0],node_list[1]), "\n")
        # Append to node_list, the root of merged first 2 nodes in list
        node_list.append(merge(node_list[0],node_list[1]))
        # Remove the 2 nodes that have been merged together
        node_list.pop(0)
        node_list.pop(0)
        # Re-sort node_list so that the new tree is in the proper place
        node_list.sort()

    # Will print only one node object if merges are successful
    # print("\n\n", node_list)
    # print(node_list[0], "\n")

    # Root node of final merged tree
    final_tree = node_list[0]

    # Array of 3-element tuples : (word, frequency, codeword)
    code_list = []

    # Pre order search that takes root of huffman tree and appends each (word, frequency, codeword) tuple to code_list
    # Needs 3rd parameter to track current codeword while iterating
    pre_order_search(final_tree, code_list, "")

    return(code_list)
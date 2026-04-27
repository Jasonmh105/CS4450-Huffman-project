from Algorithm.binary_tree import BinaryTree

def huffman_algorithm(tuples):
    
    # Sort tuples by frequency
    tuples_sorted = sorted(tuples, key=lambda element: element[1])
    print(tuples_sorted, "\n")

    # Start tree and convert each tuple to a tree node
    huffman_tree = BinaryTree()
    node_list = huffman_tree.tuples_to_nodes(tuples_sorted)

    # Recursivly merge nodes until only one is left
    while(len(node_list) > 1):
        # Make new root node from first 2 in node_list, then remove merged nodes, reinsert new root, and sort
        print(huffman_tree.merge(node_list[0],node_list[1]), "\n")
        # Append to node_list, the root of merged first 2 nodes in list
        node_list.append(huffman_tree.merge(node_list[0],node_list[1]))
        # Remove the 2 nodes that have been merged together
        node_list.remove(node_list[0])
        node_list.remove(node_list[0])
        # Re-sort node_list so that the new tree is in the proper place
        node_list.sort()

    # Will print only one node object if merges are successful
    print("\n\n", node_list)
    print(node_list[0], "\n")

    return
from Algorithm.binary_tree import BinaryTree

def huffman_algorithm(tuples):
    
    # Sort tuples by frequency
    tuples_sorted = sorted(tuples, key=lambda element: element[1])
    print(tuples_sorted)

    # Start tree and convert each tuple to a tree node
    huffman_tree = BinaryTree()
    node_list = huffman_tree.tuples_to_nodes(tuples_sorted)

    # print(huffman_tree.merge(node_list[0],node_list[1]), "\n\n\n")
    # print(node_list, "\n\n\n")

    print(huffman_tree.merge(node_list[0],node_list[1]), "\n")
    node_list.append(huffman_tree.merge(node_list[0],node_list[1]))
    node_list.remove(node_list[0])
    node_list.remove(node_list[0])
    # node_list.sort()
    


    # while(len(node_list) > 2):
    #     print(huffman_tree.merge(node_list[0],node_list[1]), "\n\n")
    #     node_list.remove(node_list[0])
    #     node_list.remove(node_list[0])
    #     node_list.insert(0, huffman_tree.merge(node_list[0],node_list[1]))

    return
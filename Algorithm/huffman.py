from Algorithm.binary_tree import BinaryTree

def huffman_algorithm(tuples):
    
    # Sort tuples by frequency
    tuples_sorted = sorted(tuples, key=lambda element: element[1])

    # Start tree with first 2 sorted tuples, and then remove those 2 tuples from list
    huffman_tree = BinaryTree()
    huffman_tree.start_tree(tuples_sorted[0],tuples_sorted[1])
    tuples_sorted.remove(tuples_sorted[0])
    tuples_sorted.remove(tuples_sorted[0])

    # Generate the working set using current tree, and remaining sorted tuples
    working_set = [(huffman_tree,huffman_tree.root.get_weight())]
    for i in range(0,len(tuples_sorted)):
        working_set.append(tuples_sorted[i])

    # Resort list so that tree tuple is in proper position
    working_set = sorted(working_set, key=lambda element: element[1])

    # Add next tuple to huffman tree, then remove it from list of remaining tuples
    # huffman_tree.insert(working_set[1])
    # working_set.remove(working_set[1])

    # Merge first 2 elements in working set
    print("PRINTING WORKING SET:                ", working_set)
    print("PRINTING MERGE:                      ", BinaryTree.merge(working_set[0],working_set[1]))

    # Resort list so that tree tuple is in proper position
    working_set = sorted(working_set, key=lambda element: element[1])

    print("PRINTING WORKING SET:                ", working_set)
    return
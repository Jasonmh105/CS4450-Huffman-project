from Algorithm.binaryTree import BinaryTree

def huffmanAlgorithm(tuples):
    
    # Sort tuples by frequency
    tuplesSorted = sorted(tuples, key=lambda element: element[1])

    # Start tree with first 2 sorted tuples, and then remove those 2 tuples from list
    huffmanTree = BinaryTree()
    huffmanTree.startTree(tuplesSorted[0],tuplesSorted[1])
    tuplesSorted.remove(tuplesSorted[0])
    tuplesSorted.remove(tuplesSorted[0])

    # Generate the working set using current tree, and remaining sorted tuples
    # NOTE !!!!!!!!! this must be changed to insert tree into working set in proper sorted position, not always on left
    workingSet = [huffmanTree]
    for i in range(0,len(tuplesSorted)):
        workingSet.append(tuplesSorted[i])

    # Add next tuple to huffman tree, then remove it from list of remaining tuples
    huffmanTree.insert(workingSet[1])
    workingSet.remove(workingSet[1])

    print("PRINTING WORKING SET:                ", workingSet)
    return
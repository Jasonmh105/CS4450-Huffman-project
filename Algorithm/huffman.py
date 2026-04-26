from Algorithm.binaryTree import BinaryTree

def huffmanAlgorithm(tuples):
    
    # Sort tuples by frequency
    tuplesSorted = sorted(tuples, key=lambda element: element[1])

    huffmanTree = BinaryTree()
    huffmanTree.startTree(tuplesSorted[0],tuplesSorted[1])

    workingSet = [huffmanTree]
    for i in range(0,len(tuplesSorted)):
        workingSet.append(tuplesSorted[i])
    print(workingSet)

    return
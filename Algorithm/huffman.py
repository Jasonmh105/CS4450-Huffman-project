from Algorithm.binaryTree import BinaryTree

def huffmanAlgorithm(tuples):
    
    # Sort tuples by frequency
    tuplesSorted = sorted(tuples, key=lambda element: element[1])

    testTree = BinaryTree()
    testTree.insert(tuplesSorted[0])

    return tuplesSorted
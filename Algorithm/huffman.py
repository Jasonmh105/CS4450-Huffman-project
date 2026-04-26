from Algorithm.binaryTree import BinaryTree

def huffmanAlgorithm(tuples):
    
    # Sort tuples by frequency
    tuplesSorted = sorted(tuples, key=lambda element: element[1])

    return tuplesSorted
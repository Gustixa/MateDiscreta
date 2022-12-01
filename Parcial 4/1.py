import numpy as np

relationSet = [0, 1, 2]


def main():

    # S o R
    # [[(0,1)],[(1,0),(1,1),(1,2)],[(2,0)]] adjacencyList S
    compositionRelations([[1], [0, 1, 2], [0]], [[1], [1, 2], [0, 1, 2]])
    # R o S
    # [[(0,1)],[(1,1),(1,2)],[(2,0),(2,1),(2,2)]] adjacencyList R
    # compositionRelations([[1], [1, 2], [0, 1, 2]], [[1], [0, 1, 2], [0]])


def compositionRelations(adjacency1: list, adjacency2: list):
    iterationKey = 0
    result, valuesAdjacency, tempAdjacency2, tempComposition = [], [], [], []
    dictionary1 = getDictionary(adjacency1)
    dictionary2 = getDictionary(adjacency2)
    print(dictionary1)
    print(dictionary2)
    for key, values in dictionary1.items():
        for i in range(len(values)):
            for values in dictionary2.values():
                pass
    # print(result)


def getDictionary(adjacency: list):
    dictionary = {}
    for i in range(len(adjacency)):
        dictionary[relationSet[i]] = adjacency[i]
    return dictionary


if __name__ == "__main__":
    main()

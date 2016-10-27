import numpy as np
import random
import hashlib


def rowPermutation(matrix):
    """permute the row of the matrix"""

    # the row sequence set
    seqSet = [i for i in range(matrix.shape[0])]

    randomSeq = random.choice(seqSet)
    new_matrix = np.array([matrix[randomSeq]])
    seqSet.remove(randomSeq)

    while len(seqSet) != 0:
        r = random.choice(seqSet)
        new_matrix = np.row_stack((new_matrix, matrix[r]))
        seqSet.remove(r)

    return new_matrix


def sigGen(matrix):
    """generate the signature vector"""

    result = []

    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[0]):

            # find the first row of i column whose value is not 0(is 1)
            if matrix[j][i] != 0:
                result.append(j)
                break

    # return a list
    return result


# n is the row number of sig matrix which we set
def sigMatrixGen(input_matrix, n):
    """generate the sig matrix"""

    result = []

    for i in range(n):
        new_matrix = rowPermutation(input_matrix)
        result.append(sigGen(new_matrix))

    # return a ndarray
    return np.array(result)


def minHash(input_matrix, b, r):
    """map the sim vector into same hash bucket"""
    # b: the number of bands
    # r: the row number of a band

    hashBuckets = {}

    n = b * r
    sigMatrix = sigMatrixGen(input_matrix, n)

    # begin and end of band row
    begin, end = 0, r

    while end <= sigMatrix.shape[0]:

        # traverse the column of sig matrix
        for colNum in range(sigMatrix.shape[1]):

            hashObj = hashlib.md5()
            hashObj.update(str(sigMatrix[begin: begin + r, colNum]).encode())

            # use hash value as bucket tag
            tag = hashObj.hexdigest()

            if tag not in hashBuckets:
                hashBuckets[tag] = [colNum]
            elif colNum not in hashBuckets[tag]:
                hashBuckets[tag].append(colNum)
        begin += r
        end += r

    # return a dictionary
    return hashBuckets

# data = np.array([[1, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 0]])
# print(rowPermutation(data))
# print(data)



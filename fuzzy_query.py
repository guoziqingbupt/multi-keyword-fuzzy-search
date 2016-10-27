import min_hash
import Unigram
import numpy as np


# index: a list of keywords
# query: a keyword
def fuzzyQuery(query, index):
    """find the word in index which is similar to query"""

    # sim keywords sequences set
    simKeywordsSeq = set()

    # input matrix
    mat = [Unigram.bitArrayGen(query)]
    for keyword in index:
        mat.append(Unigram.bitArrayGen(keyword))

    # transpose the matrix
    mat = np.array(mat).T
    hashBucket = min_hash.minHash(mat, 20, 5)

    # the first col denotes query
    for i in hashBucket:
        if 0 in hashBucket[i]:
            simKeywordsSeq.update(hashBucket[i])

    # remove the query seq
    simKeywordsSeq.remove(0)

    return [index[i - 1] for i in simKeywordsSeq]


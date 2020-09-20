import math


def prob(n, p):
    return p * (1.0 - p) ** (n - 1)


def infoMeasure(n, p):
    return -1.0 * math.log2(prob(n, p))


def sumProb(N, p):
    """
    :param N: limit number of symbols
    :param p: probability of "head" event
    :return: Sum probability of symbols from 1 ... N
    - sumProb(N, p) is asymptotic to one when N approaches infinity
    - sumProb(N, p) can be used to verify sum of geometric probability is one
    Examples:
    >>> sumProb(500, 0.5)
    1.0
    >>> sumProb(1000, 0.5)
    1.0
    """
    return sum([prob(i, p) for i in range(1, N + 1)])


def approxEntropy(N, p):
    """
    :param N: limit number of symbols
    :param p: probability of "head" event
    :return: Approximate entropy
    - approxEntropy(N, p) is asymptotic to the correct entropy when N approaches infinity
    Examples:
    >>>approxEntropy(100, 0.5)
    1.9999999999999998
    >>> approxEntropy(500, 0.5)
    1.9999999999999998
    >>> approxEntropy(1000, 0.5)
    1.9999999999999998
    """
    probs = [prob(i, p) for i in range(1, N + 1)]
    return sum([-1.0 * x * math.log2(x) for x in probs])

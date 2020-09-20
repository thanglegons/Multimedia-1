import math


class Combination:
    """
    class to calculate combination
    """

    memo = {}



    @classmethod
    def calc(cls, n, k):
        # Use dynamic programming to calculate combination
        if n == k or k == 0:
            return 1
        if (n, k) in cls.memo.keys():
            return cls.memo[(n, k)]
        result = cls.calc(n - 1, k - 1) + cls.calc(n - 1, k)
        cls.memo[(n, k)] = result
        return result


def prob(n, p, r):
    return Combination.calc(n - 1, r - 1) * p ** r * (1 - p) ** (n - r)


def infoMeasure(n, p, r):
    return -1.0 * math.log2(prob(n, p, r))


def sumProb(N, p, r):
    """
    :param N: limit number of symbols
    :param p: probability of "head" event
    :param r: number of heads to stop
    :return: Sum probability of symbols from r ... N
    - sumProb(N, p, r) is asymptotic to one when N approaches infinity
    - sumProb(N, p) can be used to verify sum of geometric probability is one
    Examples:
    >>> sumProb(500, 0.8, 15)
    1.0
    >>> sumProb(900, 0.5, 3)
    1.0
    """
    return sum([prob(i, p, r) for i in range(r, N + 1)])


def approxEntropy(N, p, r):
    """
    :param N: limit number of symbols
    :param p: probability of "head" event
    :param r: number of heads to stop
    :return: Approximate entropy
    - approxEntropy(N, p) is asymptotic to the correct entropy when N approaches infinity
    Examples:
    >>> approxEntropy(500, 0.5, 3)
    3.1156477963110514
    >>> approxEntropy(800, 0.5, 3)
    3.1156477963110514
    >>> approxEntropy(1000, 0.5, 3)
    3.1156477963110514
    """
    probs = [prob(i, p, r) for i in range(r, N + 1)]
    return sum([-1.0 * x * math.log2(x) for x in probs])
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


def prob(n, p, N):
    return Combination.calc(N, n) * p ** n * (1 - p) ** (N - n)


def infoMeasure(n, p, N):
    return -1.0 * math.log2(prob(n, p, N))


def sumProb(N, p):
    """
    :param N: number of bernoulli trials
    :param p: probability of "head" event
    :return: Sum probability of symbols from 0 ... N
    - sumProb(N, p) can be used to verify sum of geometric probability is one
    Examples:
    >>> sumProb(500, 0.2)
    1.0000000000000275
    """
    return sum([prob(i, p, N) for i in range(0, N + 1)])


def approxEntropy(N, p):
    """
    :param N: number of bernoulli trials
    :param p: probability of "head" event
    :return: entropy
    - approxEntropy(N, p) gives exactly entropy
    Examples:
    >>> approxEntropy(1, 0.5)
    1.0
    >>> approxEntropy(2, 0.5)
    1.5
    >>> approxEntropy(3, 0.5)
    1.811278124459133
    >>> approxEntropy(4, 0.5)
    2.0306390622295662
    """
    probs = [prob(i, p, N) for i in range(N + 1)]
    return sum([-1.0 * x * math.log2(x) for x in probs])

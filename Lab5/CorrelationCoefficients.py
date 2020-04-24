import numpy
import scipy.stats as stats
import StatisticalCharacteristics as statchars


def pearson_correlation(samples):
    assert(len(samples) == 2)
    x = numpy.array(samples[0]) - statchars.mean(samples[0])
    y = numpy.array(samples[1]) - statchars.mean(samples[1])
    return statchars.mean(x * y) / numpy.sqrt(statchars.mean(x * x) * statchars.mean(y * y))


def spearman_correlation(samples):
    assert(len(samples) == 2)
    ranksdiff = stats.rankdata(samples[0], method='ordinal') - stats.rankdata(samples[1], method='ordinal')
    return 1.0 - 6.0 * statchars.mean(ranksdiff * ranksdiff) / (len(samples[0]) * len(samples[0]) - 1.0)


def quadrant_correlation(samples):
    assert(len(samples) == 2)
    medx = statchars.median(samples[0])
    medy = statchars.median(samples[1])
    n1 = n2 = n3 = n4 = 0
    n = len(samples[0])
    for i in range(0, n):
        if samples[0][i] > medx:
            if samples[1][i] > medy:
                n1 += 1
            else:
                n4 += 1
        else:
            if samples[1][i] > medy:
                n2 += 1
            else:
                n3 += 1
    return float((n1 + n3) - (n2 + n4)) / n

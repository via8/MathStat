from numpy import array


def mean(samples):
    assert(len(samples) != 0)
    return sum(samples) / len(samples)


def dispersion(samples):
    s = array(samples) - mean(samples)
    return mean(s * s)


def excess(samples):
    temp1 = array(samples) - mean(samples)
    temp2 = mean(temp1 ** 4)
    return temp2 / (dispersion(samples) ** 2) - 3

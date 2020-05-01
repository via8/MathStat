from numpy import exp, sqrt, pi, array


def normal(x, mu, sigma):
    return exp(-(x - mu) * (x - mu) / (2.0 * sigma * sigma)) / (sigma * sqrt(2.0 * pi))


def mean(samples):
    return sum(samples) / len(samples)


def dispersion(samples):
    s = array(samples) - mean(samples)
    return mean(s * s)
import numpy
import statistics


def median(samples):
    return statistics.median(numpy.array(samples))


def mean(samples):
    return statistics.mean(samples)


def square_mean(samples):
    array = numpy.array(samples)
    return mean(array * array)


def dispersion(samples):
    s = numpy.array(samples) - mean(samples)
    return mean(s * s)

import statistics


def median(samples):
    return statistics.median(samples)


def mean(samples):
    return statistics.mean(samples)


def square_mean(samples):
    return mean(samples * samples)


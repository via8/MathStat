from StatisticalCharacteristics import mean, square_mean, median
from numpy import sign


def reference(x):
    return 2.0 + 2.0 * x


def leastSquaresMethod(x, y):
    assert(len(x) == len(y))
    mean_x = mean(x)
    mean_y = mean(y)
    square_mean_x = square_mean(x)
    determinant = square_mean_x - mean_x * mean_x
    assert(determinant > 0)
    beta1 = (mean(x * y) - mean_x * mean_y) / determinant
    beta0 = mean_y - mean_x * beta1
    return beta0 + beta1 * x, beta0, beta1


def leastAbsolutesMethod(x, y):
    assert (len(x) == len(y))
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    n = len(x)
    l = n // 4 - 1 if n % 4 == 0 else n // 4
    j = n - l - 1
    assert(sorted_x[j] - sorted_x[l] > 0)
    beta1 = mean(sign(x - median(x)) * sign(y - median(y))) * (sorted_y[j] - sorted_y[l]) / (sorted_x[j] - sorted_x[l])
    beta0 = median(y) - beta1 * median(x)
    return beta0 + beta1 * x, beta0, beta1

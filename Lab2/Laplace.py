import numpy
import math
import scipy.stats
import statistics

TESTS = 1000
N = [10, 100, 1000]
length = len(N)
mu = 0
sigma = 1.0 / numpy.sqrt(2.0)

for i in range(length):
    sum_mean = 0
    sum_median = 0
    sum_z_r = 0
    sum_z_q = 0
    sum_z_tr = 0

    sum_mean_sq = 0
    sum_median_sq = 0
    sum_z_r_sq = 0
    sum_z_q_sq = 0
    sum_z_tr_sq = 0

    for j in range(TESTS):
        samples = scipy.stats.laplace.rvs(mu, sigma, N[i])
        samples.sort()
        pos_lq = N[i] / 4
        pos_uq = N[i] * 3 / 4
        if not pos_lq.is_integer():
            pos_lq = math.floor(pos_lq) + 1
        if not pos_uq.is_integer():
            pos_uq = math.floor(pos_uq) + 1
        lq = samples[int(pos_lq)]
        uq = samples[int(pos_uq)]

        mean = statistics.fmean(samples)
        median = statistics.median(samples)
        z_r = (samples[0] + samples[N[i] - 1]) / 2
        z_q = (lq + uq) / 2
        z_tr = scipy.stats.trim_mean(samples, 0.1)

        sum_mean += mean
        sum_median += median
        sum_z_r += z_r
        sum_z_q += z_q
        sum_z_tr += z_tr

        sum_mean_sq += mean * mean
        sum_median_sq += median * median
        sum_z_r_sq += z_r * z_r
        sum_z_q_sq += z_q * z_q
        sum_z_tr_sq += z_tr * z_tr

    sum_mean /= TESTS
    sum_median /= TESTS
    sum_z_r /= TESTS
    sum_z_q /= TESTS
    sum_z_tr /= TESTS

    sum_mean_sq /= TESTS
    sum_median_sq /= TESTS
    sum_z_r_sq /= TESTS
    sum_z_q_sq /= TESTS
    sum_z_tr_sq /= TESTS

    print("N = " + str(N[i]))
    print("E(sum_mean) = " + str(sum_mean))
    print("E(sum_median) = " + str(sum_median))
    print("E(sum_z_r) = " + str(sum_z_r))
    print("E(sum_z_q) = " + str(sum_z_q))
    print("E(sum_z_tr) = " + str(sum_z_tr))
    print("D(sum_mean) = " + str(sum_mean_sq - sum_mean * sum_mean))
    print("D(sum_median) = " + str(sum_median_sq - sum_median * sum_median))
    print("D(sum_z_r) = " + str(sum_z_r_sq - sum_z_r * sum_z_r))
    print("D(sum_z_q) = " + str(sum_z_q_sq - sum_z_q * sum_z_q))
    print("D(sum_z_tr) = " + str(sum_z_tr_sq - sum_z_tr * sum_z_tr))
    print("\n")

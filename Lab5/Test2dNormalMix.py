from StatisticalCharacteristics import *
from CorrelationCoefficients import *
import scipy.stats as stats
from scipy import signal

# parameters
TESTS = 1000
N = [20, 60, 100]
a_coeff = 0.9
b_coeff = 0.1
a_rho = 0.9
b_rho = -0.9
a_sigma = 1
b_sigma = 10
CORRELATIONS = [pearson_correlation, spearman_correlation, quadrant_correlation]
CHARACTERISTICS = [mean, square_mean, dispersion]

# temp data for tests calculation
temp = [None] * len(CORRELATIONS)
for corr in range(0, len(CORRELATIONS)):
    temp[corr] = [None] * TESTS

# start experiment
for n in range(0, len(N)):
    print("n = " + str(N[n]))
    for test in range(0, TESTS):
        # generate samples
        a_samples = stats.multivariate_normal.rvs(mean=[0, 0],
                                                  cov=[[a_sigma * a_sigma, a_rho * a_sigma * a_sigma],
                                                       [a_rho * a_sigma * a_sigma, a_sigma * a_sigma]],
                                                  size=N[n])
        b_samples = stats.multivariate_normal.rvs(mean=[0, 0],
                                                  cov=[[b_sigma * b_sigma, b_rho * b_sigma * b_sigma],
                                                       [b_rho * b_sigma * b_sigma, b_sigma * b_sigma]],
                                                  size=N[n])
        samples = a_coeff * numpy.array(a_samples) + b_coeff * numpy.array(b_samples)

        # samples = stats.multivariate_normal.rvs(mean=[0, 0],
        #                                         cov=[[a_sigma * a_sigma * a_coeff + b_sigma * b_sigma * b_coeff,
        #                                               a_rho * a_sigma * a_sigma * a_coeff + b_rho * b_sigma * b_sigma * b_coeff],
        #                                              [a_rho * a_sigma * a_sigma * a_coeff + b_rho * b_sigma * b_sigma * b_coeff,
        #                                               a_sigma * a_sigma * a_coeff + b_sigma * b_sigma * b_coeff]],
        #                                         size=N[n])

        # calculate correlations
        for corr in range(0, len(CORRELATIONS)):
            temp[corr][test] = CORRELATIONS[corr](samples.T)

    # calculate statistical characteristics of correlations
    for corr in range(0, len(CORRELATIONS)):
        print(CORRELATIONS[corr].__name__.ljust(16))
        for char in range(0, len(CHARACTERISTICS)):
            print(CHARACTERISTICS[char].__name__.ljust(16) + " = " + str(CHARACTERISTICS[char](temp[corr])))
    print('\n')

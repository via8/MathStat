from StatisticalCharacteristics import *
from CorrelationCoefficients import *
import scipy.stats as stats

# parameters
TESTS = 100
N = [20, 60, 100]
RHO = [0.0, 0.5, 0.9]
CORRELATIONS = [pearson_correlation, spearman_correlation, quadrant_correlation]
CHARACTERISTICS = [mean, square_mean, dispersion]

# temp data for tests calculation
temp = [None] * len(CORRELATIONS)
for corr in range(0, len(CORRELATIONS)):
    temp[corr] = [None] * TESTS

# start experiment
for n in range(0, len(N)):
    print("n = " + str(N[n]))
    for rho in range(0, len(RHO)):
        print("rho = " + str(RHO[rho]))
        for test in range(0, TESTS):
            # generate samples
            samples = stats.multivariate_normal.rvs(mean=[0, 0],
                                                    cov=[[1.0, RHO[rho]], [RHO[rho], 1.0]],
                                                    size=N[n])
            # calculate correlations
            for corr in range(0, len(CORRELATIONS)):
                temp[corr][test] = CORRELATIONS[corr](samples.T)

        # calculate statistical characteristics of correlations
        for corr in range(0, len(CORRELATIONS)):
            print(CORRELATIONS[corr].__name__.ljust(16))
            for char in range(0, len(CHARACTERISTICS)):
                print(CHARACTERISTICS[char].__name__.ljust(16) + " = " + str(CHARACTERISTICS[char](temp[corr])))
    print('\n')

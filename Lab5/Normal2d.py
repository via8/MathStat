from StatisticalCharacteristics import *
from CorrelationCoefficients import *

# parameters
TESTS = 100
N = [20, 60, 100]
RHO = [0.0, 0.5, 0.9]
CORRELATIONS = [pearson_correlation, spearman_correlation, quadrant_correlation]
CHARACTERISTICS = [mean, square_mean, dispersion]

# initialization
results = [None] * len(N)
for n in range(0, len(N)):
    results[n] = [None] * len(RHO)
    for rho in range(0, len(RHO)):
        results[n][rho] = [None] * len(CORRELATIONS)
        for corr in range(0, len(CORRELATIONS)):
            results[n][rho][corr] = [None] * len(CHARACTERISTICS)

# temp data for tests calculation
temp = [None] * len(CORRELATIONS)
for corr in range(0, len(CORRELATIONS)):
    temp[corr] = [None] * TESTS

# start experiment
for n in range(0, len(N)):
    for rho in range(0, len(RHO)):
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
            for char in range(0, len(CHARACTERISTICS)):
                results[n][rho][corr][char] = CHARACTERISTICS[char](temp[corr])

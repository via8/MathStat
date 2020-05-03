from numpy import sqrt
from scipy.stats import norm, t, chi2
from util import *

alpha = 0.05
N = [20, 100]
loc = 0
scale = 1

for n in N:
    print("n = " + str(n))
    x = norm.rvs(loc=loc, scale=scale, size=n)
    mu = mean(x)
    sigma = sqrt(dispersion(x))

    # classic
    temp1 = sigma * t.ppf(1 - alpha / 2, n - 1) / sqrt(n - 1)
    temp2 = sigma * sqrt(n)
    mu_a_classic = mu - temp1
    mu_b_classic = mu + temp1
    sigma_a_classic = temp2 / sqrt(chi2.ppf(1 - alpha / 2, n - 1))
    sigma_b_classic = temp2 / sqrt(chi2.ppf(alpha / 2, n - 1))

    # asymptotic
    temp1 = norm.ppf(1 - alpha / 2, loc=loc, scale=scale) / sqrt(n)
    temp2 = temp1 * sigma
    temp3 = temp1 * sqrt(excess(x) + 2)
    mu_a_asymptotic = mu - temp2
    mu_b_asymptotic = mu + temp2
    sigma_a_asymptotic = sigma / sqrt(1 + temp3)
    sigma_b_asymptotic = sigma / sqrt(1 - temp3)

    print("mu interval (class): (%.2f, %.2f)" % (mu_a_classic, mu_b_classic))
    print("mu interval (asymp): (%.2f, %.2f)" % (mu_a_asymptotic, mu_b_asymptotic))
    print("sigma interval (class): (%.2f, %.2f)" % (sigma_a_classic, sigma_b_classic))
    print("sigma interval (asymp): (%.2f, %.2f)" % (sigma_a_asymptotic, sigma_b_asymptotic))

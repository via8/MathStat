from scipy.stats import norm, chi2
from numpy import sqrt, inf, log10, array
from util import *

n = 100
x = norm.rvs(0, 1, n)
mu = mean(x)
sigma = sqrt(dispersion(x))
print("selective mu = %.2f" % mu)
print("selective sigma = %.2f" % sigma)

k = int(1.0 + 3.3 * log10(n))  # Sturges formula
hypothet_probs = [None] * k
relative_probs = [None] * k
a = [None] * (k + 1)
a[0] = -inf
a[k] = inf

interval = 2.5  # length of main interval [a_1, a_k-1]
step = 0.5      # selected step between intervals [a_i, a_i+1]
start = mu - interval / 2.0

# determine intervals
for i in range(1, k):
    a[i] = start + step * (i - 1)

# calculate probabilities
x_sorted = sorted(x)
curr = 0
for i in range(0, k):
    prev = curr
    while curr < n and x_sorted[curr] < a[i + 1]:
        curr += 1
    relative_probs[i] = float(curr - prev)  # divide by n to get probabilities
    hypothet_probs[i] = norm.cdf(a[i + 1], mu, sigma) - norm.cdf(a[i], mu, sigma)

# comparing chi2 quantiles
alpha = 0.05
temp1 = n * array(hypothet_probs)
temp2 = array(relative_probs) - temp1
chi2_percentile_select = sum(temp2 * temp2 / temp1)
chi2_percentile_actual = chi2.ppf(1.0 - alpha, k - 1)
print("chi2 selective criterion: %.2f" % chi2_percentile_select)
print("chi2 hypothetical %.2f percentile: %.2f" % (1.0 - alpha, chi2_percentile_actual))

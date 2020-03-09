import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots

N = [10, 50, 1000]
length = len(N)
minProbability = 0.001
maxProbability = 0.990
mu = 10
minX = stats.poisson.ppf(minProbability, mu)
maxX = stats.poisson.ppf(maxProbability, mu)

x = numpy.arange(minX, maxX)
y = stats.poisson.pmf(x, mu)
plots.subplots(ncols=length)
plots.suptitle('Poisson distribution, mu = ' + str(mu))

binCount = maxX - minX
binWidth = 1
for i in range(length):
    plots.subplot(1, length, i + 1)
    plots.xlim(minX, maxX)
    plots.ylim(0, 0.7)
    plots.xlabel("random variate value")
    plots.ylabel("probability density")
    plots.title("n = " + str(N[i]))
    plots.grid()
    plots.plot(x, y)

    samples = stats.poisson.rvs(mu, size=N[i])
    print(samples)
    bins = numpy.arange(min(samples), max(samples) + binWidth, binWidth)
    plots.hist(samples, bins, density=True)
    plots.legend(('theoretical', 'actual'), loc='upper left')

plots.show()

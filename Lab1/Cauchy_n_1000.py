import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots

n = 1000
points = 1000

mu = 0
sigma = 1

plots.suptitle('Cauchy distribution, mu = ' + str(mu) + ', sigma = ' + str(sigma))

binCount = 1000
plots.xlabel("random variate value")
plots.ylabel("probability density")
plots.title("n = " + str(n))
plots.grid()

samples = stats.cauchy.rvs(mu, sigma, n)
minX = min(samples)
maxX = max(samples)
x = numpy.linspace(minX, maxX, points)
y = stats.cauchy.pdf(x, mu, sigma)
binWidth = (maxX - minX) / binCount
bins = numpy.arange(minX, maxX + binWidth, binWidth)
plots.plot(minX, 0, 'D')
plots.plot(maxX, 0, 'D')
plots.plot(x, y)
plots.hist(samples, bins, density=True)
plots.ylim(-0.2, 0.4)
plots.legend(('minimum sample', 'maximum sample', 'theoretical', 'actual'), loc='best')

plots.show()
import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots

N = [10, 50, 1000]
length = len(N)
lborder = -10.0
rborder = 10.0
bborder = 0.0
tborder = 0.7
points = 100

mu = 0
sigma = 1
x = numpy.linspace(lborder, rborder, points)
y = stats.cauchy.pdf(x, mu, sigma)

plots.subplots(ncols=length)
plots.suptitle('Cauchy distribution, mu = ' + str(mu) + ', sigma = ' + str(sigma))

binCount = 64
binWidth = (rborder - lborder) / binCount
for i in range(length):
    plots.subplot(1, length, i + 1)
    plots.xlim(lborder, rborder)
    plots.ylim(bborder, tborder)
    plots.xlabel("random variate value")
    plots.ylabel("probability density")
    plots.title("n = " + str(N[i]))
    plots.grid()
    plots.plot(x, y)

    samples = stats.cauchy.rvs(mu, sigma, N[i])
    bins = numpy.arange(min(samples), max(samples) + binWidth, binWidth)
    plots.hist(samples, bins, density=True)
    plots.legend(('theoretical', 'actual'), loc='upper left')

plots.show()
import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots

N = [10, 50, 1000]
length = len(N)
lborder = -5.0
rborder = 5.0
bborder = 0.0
tborder = 1.2
points = 100

mu = 0
sigma = 1.0 / numpy.sqrt(2.0)
x = numpy.linspace(lborder, rborder, points)
y = stats.laplace.pdf(x, mu, sigma)

plots.subplots(ncols=length)
plots.suptitle('Laplace distribution, mu = ' + str(mu) + ', sigma = 1 / sqrt(2)')

binCount = 64
binWidth = (rborder - lborder) / binCount
for i in range(length):
    plots.subplot(1, length, i + 1)
    plots.xlim(lborder, rborder)
    plots.ylim(bborder, tborder)
    plots.xlabel('random variate value')
    plots.ylabel('probability density')
    plots.title('n = ' + str(N[i]))
    plots.grid()
    plots.plot(x, y)

    samples = stats.laplace.rvs(mu, sigma, N[i])
    bins = numpy.arange(min(samples), max(samples) + binWidth, binWidth)
    plots.hist(samples, bins, density=True)
    plots.legend(('theoretical', 'actual'), loc='upper left')

plots.show()
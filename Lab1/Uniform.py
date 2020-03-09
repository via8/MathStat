import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots

SQRT_3 = numpy.sqrt(3.0)

N = [10, 50, 1000]
length = len(N)
lborder = -2 * SQRT_3
rborder = SQRT_3
bborder = 0.0
tborder = 1.2
points = 100

mu = -SQRT_3
sigma = SQRT_3
x = numpy.linspace(lborder, rborder, points)
y = stats.uniform.pdf(x, mu, sigma)

plots.subplots(ncols=length)
plots.suptitle('Uniform distribution, mu = -sqrt(3), sigma = sqrt(3)')

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

    samples = stats.uniform.rvs(mu, sigma, N[i])
    bins = numpy.arange(min(samples), max(samples) + binWidth, binWidth)
    plots.hist(samples, bins, density=True)
    plots.legend(('theoretical', 'actual'), loc='upper left')

plots.show()
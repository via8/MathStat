import numpy
import scipy.stats
import matplotlib.pyplot

# initialization
mu = 10
N = [20, 100]
length = len(N)

# box plots
matplotlib.pyplot.subplots(nrows=length)
matplotlib.pyplot.suptitle('Poisson distribution, mu = ' + str(mu))
for i in range(length):
    matplotlib.pyplot.subplot(length, 1, i + 1)
    matplotlib.pyplot.title("n = " + str(N[i]))
    matplotlib.pyplot.grid()
    samples = scipy.stats.poisson.rvs(mu, size=N[i])
    matplotlib.pyplot.boxplot([samples], vert=False)
matplotlib.pyplot.show()

# outliers calculation
TESTS = 1000
for i in range(length):
    outliers = 0
    for j in range(TESTS):
        samples = scipy.stats.poisson.rvs(mu, size=N[i])
        lq = numpy.quantile(samples, 0.25)
        uq = numpy.quantile(samples, 0.75)
        iqr = uq - lq
        xl = max(samples.min(), lq - 3 / 2 * iqr)
        xu = min(samples.max(), uq + 3 / 2 * iqr)

        for k in range(0, N[i]):
            if samples[k] < xl or samples[k] > xu:
                outliers += 1
    outlierProbability = outliers / TESTS / N[i]
    print('outlierProbability n = ' + str(N[i]) + ' : ' + str(outlierProbability))

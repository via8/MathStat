import numpy
import scipy.stats
import statistics
import matplotlib.pyplot


def empF(n):
    res = [0] * n
    for k in range(0, n):
        res[k] = k / n
    return res


def bandwidth(s, n):
    return 1.06 * s * numpy.power(n, -1 / 5)


def kernel(u):
    return (1 / numpy.sqrt(2 * numpy.pi)) * numpy.exp(-(u * u) / 2)


def empf(x, samples, n, h):
    sum = 0
    for k in range(1, n):
        sum += kernel((x - samples[k]) / h)
    return sum / (n * h)


# initialization
lborder = -4.0
rborder = 4.0
points = 1000
mu = 0
sigma = 1
x = numpy.linspace(lborder, rborder, points)
F = scipy.stats.cauchy.cdf(x, mu, sigma)
f = scipy.stats.cauchy.pdf(x, mu, sigma)
N = [20, 60, 100]
length = len(N)

# F plots
matplotlib.pyplot.subplots(ncols=length)
matplotlib.pyplot.suptitle('Cauchy distribution, mu = ' + str(mu) + ', sigma = ' + str(sigma))
for i in range(length):
    matplotlib.pyplot.subplot(1, length, i + 1)
    matplotlib.pyplot.title("n = " + str(N[i]))
    matplotlib.pyplot.grid()
    matplotlib.pyplot.xlim([lborder, rborder])

    samples_x = scipy.stats.cauchy.rvs(mu, sigma, size=N[i])
    samples_x.sort()
    condition = lborder < samples_x
    samples_x = numpy.extract(condition, samples_x)
    condition = samples_x < rborder
    samples_x = numpy.extract(condition, samples_x)

    samples_x = list(samples_x)
    samples_F = empF(len(samples_x))
    samples_x.insert(len(samples_x), rborder)
    samples_x.insert(0, lborder)
    samples_F.insert(len(samples_F), 1)
    samples_F.insert(0, 0)
    matplotlib.pyplot.plot(x, F)
    matplotlib.pyplot.step(samples_x, samples_F)
    matplotlib.pyplot.legend(('theoretical', 'empirical'), loc='upper left')

matplotlib.pyplot.show()

# f plots
for i in range(length):
    matplotlib.pyplot.subplots(ncols=length)
    matplotlib.pyplot.suptitle('Cauchy distribution, mu = ' + str(mu) + ', sigma = ' + str(sigma) + ', n = ' + str(N[i]))

    samples_x = scipy.stats.cauchy.rvs(mu, sigma, size=N[i])
    samples_x.sort()
    samples_x = list(samples_x)

    H = bandwidth(statistics.stdev(samples_x), len(samples_x))
    samples_f = [None] * len(x)
    h = [None] * 3
    h[0] = H / 2
    h[1] = H
    h[2] = H * 2

    for l in range(0, len(h)):
        matplotlib.pyplot.subplot(1, length, l + 1)
        matplotlib.pyplot.grid()
        matplotlib.pyplot.xlim([lborder, rborder])
        matplotlib.pyplot.ylim([0.0, 1.0])
        for j in range(0, len(x)):
            samples_f[j] = empf(x[j], samples_x, len(samples_x), h[l])

        matplotlib.pyplot.plot(x, f)
        matplotlib.pyplot.plot(x, samples_f)
        matplotlib.pyplot.legend(('theoretical', 'empirical'), loc='upper left')
        if l == 0:
            hstr = 'h_n / 2'
        elif l == 1:
            hstr = 'h_n'
        else:
            hstr = 'h_n * 2'
        matplotlib.pyplot.title('h = ' + hstr)

    matplotlib.pyplot.show()

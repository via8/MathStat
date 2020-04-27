import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots
import matplotlib.patches as patches
import StatisticalCharacteristics as statchars


def plot_dispersion_ellipse(samples, corr_coeff, subplot):
    assert (len(samples) == 2)
    mean_x = statchars.mean(samples[0])
    mean_y = statchars.mean(samples[1])
    dispersion_x = statchars.dispersion(samples[0])
    dispersion_y = statchars.dispersion(samples[1])
    sigma_x = numpy.sqrt(dispersion_x)
    sigma_y = numpy.sqrt(dispersion_y)
    angle_rad = numpy.pi / 4
    if abs(dispersion_x - dispersion_y) > 1e-3:
        angle_rad = numpy.arctan(2.0 * corr_coeff * sigma_x * sigma_y / (dispersion_x - dispersion_y)) / 2.0
    # mean_x = 0
    # mean_y = 0
    # dispersion_x = 1
    # dispersion_y = 1
    # sigma_x = 1
    # sigma_y = 1
    # angle_rad = numpy.pi / 4.0
    cos = numpy.cos(angle_rad)
    sin = numpy.sin(angle_rad)
    A = 1 / (dispersion_x * (1 - corr_coeff * corr_coeff))
    B = 1 / (dispersion_y * (1 - corr_coeff * corr_coeff))
    C = corr_coeff / (sigma_x * sigma_y * (1 - corr_coeff * corr_coeff))
    a = 2 / numpy.sqrt(A * cos * cos + B * sin * sin - 2 * C * sin * cos)
    b = 2 / numpy.sqrt(A * cos * cos + B * sin * sin + 2 * C * sin * cos)
    ellipse = patches.Ellipse((mean_x, mean_y), a * 2, b * 2, numpy.rad2deg(angle_rad))
    subplot.set_title("$\\rho$ = " + str(corr_coeff))
    subplot.plot(samples[0], samples[1], 'ro', markersize=2)
    subplot.add_patch(ellipse)
    subplot.axis('scaled')


# parameters
N = [20, 60, 100]
RHO = [0.0, 0.5, 0.9]

# start experiment
for n in range(0, len(N)):
    fig, ax = plots.subplots(1, ncols=len(RHO))
    for rho in range(0, len(RHO)):
        # generate samples
        samples = stats.multivariate_normal.rvs(mean=[0, 0], cov=[[1.0, RHO[rho]], [RHO[rho], 1.0]], size=N[n])
        # draw ellipse
        fig.suptitle('normal distribution n = ' + str(N[n]))
        plot_dispersion_ellipse(samples.T, RHO[rho], ax[rho])
plots.show()

import numpy
import scipy.stats as stats
import matplotlib.pyplot as plots
import matplotlib.patches as patches
import StatisticalCharacteristics as statchars


def plot_dispersion_ellipse(samples, corr_coeff, subplot):
    assert (len(samples) == 2)
    dispersion_x = statchars.dispersion(samples[0])
    dispersion_y = statchars.dispersion(samples[1])
    sigma_x = numpy.sqrt(dispersion_x)
    sigma_y = numpy.sqrt(dispersion_y)
    angle_rad = numpy.arctan(2.0 * corr_coeff * sigma_x * sigma_y / (dispersion_x - dispersion_y)) / 2.0
    cos_sq = numpy.cos(angle_rad)
    sin_sq = numpy.sin(angle_rad)
    cos_sq *= cos_sq
    sin_sq *= sin_sq
    sin_2 = numpy.sin(2.0 * angle_rad)
    width = 4 * numpy.sqrt(dispersion_x * cos_sq + corr_coeff * sigma_x * sigma_y * sin_2 + dispersion_y * sin_sq)
    height = 4 * numpy.sqrt(dispersion_x * sin_sq - corr_coeff * sigma_x * sigma_y * sin_2 + dispersion_y * cos_sq)
    ellipse = patches.Ellipse((statchars.mean(samples[0]), statchars.mean(samples[1])), width, height, numpy.rad2deg(angle_rad))
    subplot.set_title("$\\rho$ = " + str(corr_coeff))
    subplot.plot(samples[0], samples[1], 'ro')
    subplot.add_patch(ellipse)


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

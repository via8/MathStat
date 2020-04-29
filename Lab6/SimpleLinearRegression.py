from numpy import linspace, array
from scipy.stats import norm
from Samples import *
from Dependencies import *
import matplotlib.pyplot as plots

n = 20
x = array(linspace(-1.8, 2.0, n))
errors = array(norm.rvs(0, 1, n))

samples_default = array(defaultSamples(x, errors))
samples_disturbed = array(disturbedSamples(x, errors))

y_ref = reference(x)

fig, ax = plots.subplots(1, 2)

# default samples plots
y_lsm, beta0_lsm, beta1_lsm = leastSquaresMethod(x, samples_default)
y_lam, beta0_lam, beta1_lam = leastAbsolutesMethod(x, samples_default)
ax[0].set_title("default samples\n"
                "lsm: $\\beta_0 \\approx$ %.2f $\\beta_1 \\approx$ %.2f\n"
                "lam: $\\beta_0 \\approx$ %.2f $\\beta_1 \\approx$ %.2f\n"
                % (beta0_lsm, beta1_lsm, beta0_lam, beta1_lam))
ax[0].plot(x, samples_default, 'ro')
ax[0].plot(x, y_ref)
ax[0].plot(x, y_lsm)
ax[0].plot(x, y_lam)
ax[0].legend(('samples', 'reference', 'lsm', 'lam'), loc='upper left')

# disturbed samples plots
y_lsm, beta0_lsm, beta1_lsm = leastSquaresMethod(x, samples_disturbed)
y_lam, beta0_lam, beta1_lam = leastAbsolutesMethod(x, samples_disturbed)
ax[1].set_title("disturbed samples\n"
                "lsm: $\\beta_0 \\approx$ %.2f $\\beta_1 \\approx$ %.2f\n"
                "lam: $\\beta_0 \\approx$ %.2f $\\beta_1 \\approx$ %.2f\n"
                % (beta0_lsm, beta1_lsm, beta0_lam, beta1_lam))
ax[1].plot(x, samples_disturbed, 'ro')
ax[1].plot(x, y_ref)
ax[1].plot(x, y_lsm)
ax[1].plot(x, y_lam)
ax[1].legend(('samples', 'reference', 'lsm', 'lam'), loc='upper right')

plots.show()



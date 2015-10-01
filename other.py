# encoding: utf-8

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def rnd(i):
    return np.random.random(i)


x = np.random.random(10)
y = np.random.random(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

sizes = 1000 * rnd(10)
colors = rnd(10)

fit_x = np.linspace(0, 1, 100)
fit_y = slope * fit_x + intercept

plt.scatter(x, y, sizes, colors, alpha=0.5)
plt.plot(fit_x, fit_y, '--r')

plt.title("That looks familiar", fontsize=16)
plt.show()

print("r-squared: " + str(r_value ** 2))

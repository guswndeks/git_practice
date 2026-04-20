from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

data = norm.rvs(10.0, 3, size = 1000)
plt.hist(data, bins = 20, density = True, alpha = 0.6, color = 'b')
mu, std = norm.fit(data)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x,p,'r',linewidth = 2)

plt.show()

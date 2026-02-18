import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)
n = 10 ** 5
p = .35

geometry = rng.random(size=n) < p
estimate = np.cumsum(geometry) / np.arange(1, n+1)

plt.plot(range(1, n+1), estimate)
plt.show()
plt.hist(geometry.astype('int'), bins=2)
plt.show()
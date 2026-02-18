import numpy.random as rnd
import matplotlib.pyplot as plt

rng = rnd.default_rng(seed=42)
n = 10**6
uniform = rng.random(size=n)
normal = rng.normal(size=n)

plt.hist(uniform, bins=20)
plt.show()
plt.hist(normal, bins=20, range=(-3, 3), density=True)
plt.show()

print(f"uniform distribution under 0.5: {sum(uniform < 0.5) / n}")
print(f"normal distribution under 0.5: {sum(normal < 0.5) / n}")
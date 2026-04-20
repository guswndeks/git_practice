import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi)
ysin = np.sin(x)
ycos = np.cos(x)

fig, ax = plt.subplots(2, 1)

ax[0].plot(x,ysin,'r--', label='sin')
ax[0].set_title("Sin Function")
ax[0].grid(True)
ax[0].legend(loc='upper right')
ax[0].set_xlabel("x")
ax[0].set_ylabel("y")

ax[1].plot(x,ycos,'b-', label='cos')
ax[1].set_title("Cos Function")
ax[1].grid(True)
ax[1].legend(loc='lower left')
ax[1].set_xlabel("x")
ax[1].set_ylabel("y")

plt.tight_layout()
fig.savefig("Sin Cos Function")
plt.show()
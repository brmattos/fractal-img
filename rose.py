from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


def update(val):
    n = int(slider_n.val)
    d = int(slider_d.val)
    k = n / d
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = np.cos(k * theta)
    line.set_data(theta, r)
    fig.canvas.draw_idle()


fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.set_title("Rose Curve", pad=20)

n, d = 3, 2
k = n / d
theta = np.linspace(0, 2 * np.pi, 1000)
r = np.cos(k * theta)
line, = ax.plot(theta, r, color='red')

plt.subplots_adjust(left=0.25, bottom=0.3)
slider_n_ax = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_d_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_n = Slider(slider_n_ax, 'n', 1, 20, valinit=n, valstep=1)
slider_d = Slider(slider_d_ax, 'd', 1, 20, valinit=d, valstep=1)
slider_n.on_changed(update)
slider_d.on_changed(update)

plt.show()

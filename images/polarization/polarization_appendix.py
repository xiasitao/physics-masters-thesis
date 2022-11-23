# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import patches
cm = 1/2.54
thesis_red = "#FF0000"
thesis_gray = "#474847"
thesis_rebecca = "#693EA3"
thesis_fuchsia = "#9A5B91"
thesis_blue = "#50BDE9"
thesis_color_map = matplotlib.colors.LinearSegmentedColormap.from_list("Custom", [thesis_gray, thesis_red], N=1000)
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[thesis_red, thesis_blue, thesis_rebecca, thesis_gray, thesis_fuchsia])
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

# %%

def ellipse_points(a, e, steps = 100):
    parameters = np.linspace(0, 2*np.pi, steps)
    phi = np.arctan(np.tan(2*e) / np.sin(2*a)) if a != 0 else 0
    X = np.cos(parameters)
    Y = np.sin(parameters) * np.tan(e)

    alpha = a
    X_rot = X * np.cos(alpha) - Y * np.sin(alpha)
    Y_rot = X * np.sin(alpha) + Y * np.cos(alpha)

    return X_rot, Y_rot

def plot_sphere(ax, a, e, label=None, show_angles=False):
    X, Y = ellipse_points(a, e)
    plot = ax.plot(X, Y, label=label)

    if show_angles:
        color = plot[0].get_color()
        center = (0, 0)
        azimuth_point = np.array([np.cos(a), np.sin(a)])
        ax.plot(*zip(center, azimuth_point), color=color, linestyle='dashed')
        ax.text(x=0.2, y=0.2*np.tan(a/2.3), s=r'$\alpha$', color=color)
        ax.plot(0.3*np.cos(np.linspace(0, a, 100)), 0.3*np.sin(np.linspace(0, a, 100)), color=color, linewidth=1)

        short_axis_point = np.array([np.sin(a), -np.cos(a)]) * np.tan(e)
        ax.plot(*zip(center, short_axis_point), color=color, linestyle='dashed')
        ax.plot(*zip(azimuth_point, short_axis_point), color=color, linestyle='dashed')

        ax.text(x=azimuth_point[0]-(0.2), y=azimuth_point[1]-(0.2*(np.tan(a+e/2))), s=r'$\epsilon$', color=color)
        ax.plot(
            azimuth_point[0]+0.3*np.cos(np.pi+a+np.linspace(0, e, 100)),
            azimuth_point[1]+0.3*np.sin(np.pi+a+np.linspace(0, e, 100)),
            color=color, linewidth=1
        )

fig = plt.figure(figsize=(10.5*cm, 10.5*cm))
ax = fig.add_subplot(111, aspect='equal')

ax.plot((-1, 1), (0, 0), (0, 0), (-1, 1), color=thesis_gray)

plot_sphere(ax, np.pi/6, np.pi/8, r'ellipse $\left(\alpha={\pi}/{6}, \epsilon={\pi}/{8}\right)$', True)
plot_sphere(ax, -3*np.pi/8, 0, r'linear $\left(\alpha=-{3\pi}/{8}, \epsilon=0\right)$')
plot_sphere(ax, 0, np.pi/4, r'circular $\left(\mathrm{any}~ \alpha, \epsilon={\pi}/{4}\right)$')



ax.grid()
ax.legend(loc='lower left')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel('horizontal component')
ax.set_ylabel('vertical component')
fig.savefig('img/azimuth_ellipticity_visualization.pgf', bbox_inches='tight')
fig.show()
# %%

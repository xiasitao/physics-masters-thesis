# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
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

# From GaussianBeam
wavelength = 671e-9

input_beam_waist_position = -27.4e-3
input_beam_waist = 500e-6
in_telescope_beam_waist = 31.97e-6
in_telescope_beam_waist_position = 47.29e-3
after_telescope_beam_waist = 290.74e-6
after_telescope_beam_waist_position = 173.824e-3
after_focusing_lens_waist = 327.888e-6
after_focusing_lens_waist_position = 720.857e-3

telescope_first_lens_position = -27.4e-3
telescope_second_lens_position = 0.0e-3
first_AOM_position = 125e-3
focusing_lens_position = 475e-3
first_PBS_after_first_AOM_position = 480e-3
second_PBS_after_first_AOM_position = 567.5e-3
second_AOMS_position = 727.5e-3

# %%

def  plot_beam(axis, from_position, to_position, waist, waist_position):
    z_R = np.pi * waist**2 * 1 / wavelength
    def w(position):
        return waist * np.sqrt(1 + ((position-waist_position)/z_R)**2)
    positions = np.arange(from_position, to_position, 1e-3)
    radii = w(positions)

    axis.fill_between(positions*1e3, radii*1e6, color=thesis_red)
    axis.fill_between(positions*1e3, -radii*1e6, color=thesis_red)

def plot_position(axis: plt.Axes, position, label):
    axis.vlines(position*1e3, -500, 570, color=thesis_gray, linewidth=1, linestyles='dashed')
    axis.text(position*1e3, 570, s=label, horizontalalignment='center', fontdict={'size': 8})

fig = plt.figure(figsize=(15*cm, 6*cm))
ax = fig.subplots()
ax.set_xlabel('distance from telescope in mm')
ax.set_ylabel('beam $1/e^2$ extent in $\mu$m')
ax.grid()
ax.set_xlim([-70, 830])
ax.set_ylim([-530, 530])
plot_beam(ax, -70e-3, telescope_first_lens_position, input_beam_waist, input_beam_waist_position)
plot_beam(ax, telescope_first_lens_position, telescope_second_lens_position, in_telescope_beam_waist, in_telescope_beam_waist_position)
plot_beam(ax, telescope_second_lens_position, focusing_lens_position, after_telescope_beam_waist, after_telescope_beam_waist_position)
plot_beam(ax, focusing_lens_position, 830e-3, after_focusing_lens_waist, after_focusing_lens_waist_position)

for position, label in zip(
    [(telescope_first_lens_position + telescope_second_lens_position)/2, first_AOM_position, focusing_lens_position, second_PBS_after_first_AOM_position, second_AOMS_position],
    ['telescope (g)', 'AOM (h)', 'lens (k)', 'PBS (o)', 'AOMs (p/q)']
    ):
    plot_position(ax, position, label)

fig.tight_layout()
fig.savefig('beam_diameter_evolution_outline.pgf', bbox_inches='tight')
fig.show()
# %%

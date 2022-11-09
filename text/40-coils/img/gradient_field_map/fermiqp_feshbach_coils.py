#%%
import sys
import numpy as np
import matplotlib.pyplot as plt
cm = 1/2.54
thesis_red = "#FF0000"
thesis_gray = "#474847"
thesis_rebecca = "#693EA3"
thesis_fuchsia = "#9A5B91"
thesis_blue = "#50BDE9"
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[thesis_red, thesis_blue, thesis_rebecca, thesis_gray, thesis_fuchsia])
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

sys.path.insert(0, '..')
import coil_simulation_lib as csl
import magpylib as mpl

#%%

# FERMIQP_COIL_PROPERTIES = {
#     'windings_axis': 6,
#     'windings_cross_axis': 5,
#     'cone_angle': np.arctan(1),
#     'current': 400,
#     'gradient': False,
#     'radius': 78e-3,
#     'wire_spacing': 5.3e-3,
#     'on_axis_coil_distance': 80e-3
# }

FERMIQP_COIL_PROPERTIES = {
    'windings_axis': 6,
    'windings_cross_axis': 5,
    'cone_angle': np.arctan(1),
    'current': 400,
    'gradient': True,
    'radius': 83e-3,
    'wire_spacing': 5.3e-3,
    'on_axis_coil_distance': 85.5e-3,
    'non_conducting_cross_section_area': (1.5e-3)**2*np.pi + 4 * (5e-3 * 0.15e-3)
}

#%%
arrangement = csl.ConeShapedCoilArrangement(**FERMIQP_COIL_PROPERTIES)

arrangement.plot_arrangement_schematic(figsize=(9.5*cm, 7*cm), filename='img/max_thesis/csl_sketches_cross_section.pgf')
arrangement.display_in_3D(figsize=(9.5*cm, 9.5*cm), filename='img/max_thesis/csl_sketches_3d.pgf')
curvature_analyzer = csl.CurvatureAnalyzer().from_arrangement(arrangement=arrangement, steps=100)
print(f'x trap freq: {curvature_analyzer.get_trap_frequency_on_axis("x"):.2f} Hz')
print(f'x gradient: {curvature_analyzer.get_gradient_on_axis("x")*1e2:.2f} G/cm')
print(f'y trap freq: {curvature_analyzer.get_trap_frequency_on_axis("y"):.2f} Hz')
print(f'y gradient: {curvature_analyzer.get_gradient_on_axis("y")*1e2:.2f} G/cm')
print(f'field at center: {arrangement.field_at_center() * 1e4} G')


#%%
"""Field maps"""
field_map_xy = csl.FieldMap(arrangement, 'xy', 100)
field_map_xy.plot_map(
    filename=f'img/max_thesis/{"gradient" if arrangement.gradient else "feshbach"}_field_map_xy.pgf',
    line_color=thesis_gray,
    colormap_colors=[thesis_blue, thesis_red],
    width=15*cm,
    show_title=False
)
def _zoom_config():
    plt.xlim(-3, +3)
    plt.ylim(1250, 1350)
field_map_xy.plot_slices(
    filename=f'img/max_thesis/{"gradient" if arrangement.gradient else "feshbach"}_field_slices_xy.pgf',
    show_title=False,
    figsize=(15*cm, 6*cm)
    # mpl_config_callback=_co_zoom_confignfig
)

#field_map_xz = csl.FieldMap(arrangement, 'xz', 200)
#field_map_xz.plot_map(filename=f'img/{"gradient" if arrangement.gradient else "feshbach"}_field_map_xz.png')
#field_map_xz.plot_slices(filename=f'img/{"gradient" if arrangement.gradient else "feshbach"}_field_slices_xz.png')

# %%
"""Coil properties"""
print(f'==== Coil properties ({"gradient" if arrangement.gradient else "Feshbach"}) ====')
print(f'wire length: l = {arrangement.get_total_coil_length()/2:.2f} m')
print(f'resistance: R = {arrangement.get_single_coil_resistance()*1000:.2f} mOhm')
print(f'single winding pair + supply line resistance: R ~ {arrangement.get_single_coil_resistance(supply_line_length=3.1, coil_length_factor=1/3)*1000:.2f} mOhm')
print(f'inductance (single): L = {arrangement.estimate_single_coil_self_inductance()*1000:.2f} mH')
print(f'L/R time (single): L/R = {arrangement.get_single_coil_L_over_R_time()*1000:.2f} ms')
print(f'inductance (all): L = {arrangement.estimate_all_coils_self_inductance()*1000:.2f} mH')
print(f'L/R time (all): L/R = {arrangement.get_all_coils_L_over_R_time()*1000:.2f} ms')
print(f'magnetic dipole moment: m = {arrangement.get_magnetic_dipole_moment():.2f} Am^2')
print(f'magnetic dipole moment (single coil): m = {arrangement.get_magnetic_dipole_moment(coil_index=0):.2f} Am^2')
print(f'outward force: {arrangement.get_total_outward_force_on_single_coil()}')
# %%
"""Fields"""
print(f'field at center: {arrangement.get_absolute_field_at([0, 0, 0])/1e-4:.2f} G')
print(f'gradient at center: {arrangement.get_field_gradient_at((0e-2, 0e-2, 0e-2))}')
print(f'field at SryLab: {arrangement.get_absolute_field_at([5, 0, 0])/1e-7:.1f} mG')
print(f'field at Single atoms: {arrangement.get_absolute_field_at([0, 2, 5])/1e-7:.1f} mG')
print(f'field vector at Single atoms: {arrangement.get_field_at([0, 2, 5])/1e-7} mG')
print(f'field at MQV lab: {arrangement.get_absolute_field_at([5, 0, 5])/1e-7:.1f} mG')


# %%
# Varying coil distance
distances = np.linspace(80e-3, 90e-3, 200)
def calculate_trap_frequency(distance):
    properties = {**FERMIQP_COIL_PROPERTIES}  # copy
    properties['on_axis_coil_distance'] = distance
    arrangement = csl.ConeShapedCoilArrangement(**properties)
    return np.array([
        arrangement.get_trap_frequency_on_axis(axis='y'),
        arrangement.get_trap_frequency_on_axis(axis='x')
    ])

trap_frequencies_on_axis, trap_frequencies_cross_axis = np.zeros(shape=distances.shape), np.zeros(shape=distances.shape)
for i, distance in enumerate(distances):
    on_axis, cross_axis = calculate_trap_frequency(distance)
    trap_frequencies_on_axis[i] = on_axis
    trap_frequencies_cross_axis[i] = cross_axis

plt.figure(figsize=(12*cm, 6*cm))
plt.ylabel('trap frequency in Hz')
plt.xlabel(r'$\pm$ coil position in mm')
plt.xticks(ticks=np.arange(40, 45.5, 0.5))
for i, label in enumerate(plt.gca().xaxis.get_ticklabels()):
    if i % 2:
        label.set_visible(False)
plt.plot(distances*1e3/2, trap_frequencies_on_axis, label='on-axis')
plt.plot(distances*1e3/2, trap_frequencies_cross_axis, label='cross-axis')
plt.hlines(y=0, xmin=40, xmax=45, colors=thesis_gray,linestyles='dashed')
plt.text(x=40.1, y=1.1, s='trapping for hfs')
plt.text(x=40.1, y=-1.7, s='anti-trapping for hfs')
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()
plt.savefig('img/max_thesis/feshbach_field_trap_frequencies.pgf', bbox_inches='tight')
plt.show()

# %%

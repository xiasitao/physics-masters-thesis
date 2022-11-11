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
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[thesis_red, thesis_blue, thesis_rebecca, thesis_gray, thesis_fuchsia, 'green', 'pink', 'orange', 'gray', 'violet'])
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

def rad_to_deg(rad):
    return rad/np.pi * 180

def deg_to_rad(deg):
    return deg/180 * np.pi

c = 299792458  # m/s
g = 2
mu_B = 9.2740100783e-24
hbar = 1.054571817e-34  # Js
m_6Li = 9.98e-27  # kg
lambda_D1 = 670.992421e-9  # m
k_D1 = 2*np.pi/lambda_D1
omega_D1 = c*k_D1
lambda_D2 = 670.977338e-9  # m
k_D2 = 2*np.pi/lambda_D2
omega_D2 = c*k_D2
Gamma = 5.8724e6  # Hz
theta_recapture = deg_to_rad(30) # rad

print(
f'''Properties of 6Li:
m = {m_6Li} kg
lambda_D1 = {lambda_D1*1e9:.3f} nm
k_D1 = {k_D1} 1/m
omega_D1 = {omega_D1/(2*np.pi)/1e12:.3f} 2pi THz
lambda_D2 = {lambda_D2*1e9} nm
k_D2 = {k_D2} 1/m
omega_D2 = {omega_D2/(2*np.pi)/1e12:.3f} 2pi THz
Gamma = {Gamma/1e6}  MHz
'''
)

# %%
# Definitions 
def rho_ee(s_0, delta):
    return (
        s_0/2
        / (
            1 + s_0 + (2*delta/Gamma)**2
        )
    )

def F_scatter(s_0, delta, k):
    return (
        Gamma * rho_ee(s_0=s_0, delta=delta) * hbar * k
    )

def F_optical_molasses(s_0, delta_laser, k, v, theta):
    effective_omega_backward = delta_laser - k*v*np.cos(theta)
    effective_omega_forward = delta_laser + k*v*np.cos(theta)
    return (
        F_scatter(s_0=s_0, k=k, delta=effective_omega_backward)
        - F_scatter(s_0=s_0, k=k, delta=effective_omega_forward)
    )

def alpha(k, s_0, delta):
    return (
        -8*hbar*k**2 * s_0 * 
        (
            delta/Gamma
            /
            (1 + s_0 + (2*delta/Gamma)**2)**2
        )
    )


def v_capture_high(r_trap):
    return np.sqrt(hbar * k_D2 *Gamma*2*r_trap/m_6Li)

def v_capture_low(k, s_0, delta, theta, r_trap):
    return 2 * alpha(k, s_0, delta) * np.cos(theta) * r_trap / m_6Li

def v_resonance(k, theta, grad, r_trap, delta):
    value = (
        1 / (k * np.cos(theta))
        * (
            g * mu_B / hbar * grad * r_trap
            - delta
        )
    )
    return value if value <= v_capture_high(r_trap=r_trap) else np.nan
v_resonance = np.vectorize(v_resonance)

# %%
# Scattering force
plt.figure(figsize=(10*cm, 5*cm))
plt.xlabel(r'speed in $\Gamma/k$')
plt.ylabel(r'scattering rate in $1/\Gamma$')
speeds_by_Gamma_by_k = np.linspace(-5, 7, 300)
speeds = speeds_by_Gamma_by_k * (Gamma/k_D2)
detunings_by_Gamma = np.arange(-3, 3.5, 3)

for detuning_by_Gamma in detunings_by_Gamma:
    fs = rho_ee(s_0=1, delta=detuning_by_Gamma * Gamma + k_D2*speeds)  # + for towards
    plt.plot(speeds_by_Gamma_by_k, fs, label=rf'$\delta = {"+" if detuning_by_Gamma >= 0 else ""}{detuning_by_Gamma:.0f} \Gamma$')
    if detuning_by_Gamma == -3:
        v_max = -(detuning_by_Gamma*Gamma) / k_D2
        plt.vlines(v_max, 0, 0.28, linestyles='dashed', linewidth=1)
        plt.arrow(v_max/2, 0.29, -v_max/2, 0, length_includes_head=True, linewidth=0.4, head_length=0.1, head_width=0.01, color=thesis_red)
        plt.arrow(v_max/2, 0.29, +v_max/2, 0, length_includes_head=True, linewidth=0.4, head_length=0.1, head_width=0.01, color=thesis_red)
        plt.text(v_max/2-0.12, 0.24, s=r'$\frac{\delta}{k}$', color=thesis_red)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('img/scattering_rate.pgf', bbox_inches='tight')
plt.show()
# %%
# Optical molasses forces
plt.figure(figsize=(10*cm, 7*cm))
plt.xlabel(r'speed in $\Gamma/k$')
plt.ylabel(r'$F_\mathrm{MO}$ in $1/(\hbar k \Gamma)$')
speeds_by_Gamma_by_k = np.linspace(-2, 2, 300)
speeds = speeds_by_Gamma_by_k * (Gamma/k_D2)
detunings_by_Gamma = np.linspace(-1.5, -0.5, 3)
for detuning_by_Gamma in detunings_by_Gamma:
    fs = F_optical_molasses(s_0=0.1, delta_laser=detuning_by_Gamma*Gamma, k=k_D2, v=speeds, theta=0)
    plt.plot(speeds_by_Gamma_by_k, fs/(hbar*k_D2*Gamma), label=rf'$\delta = {detuning_by_Gamma:.1f} \Gamma$', color=thesis_red, alpha=(3+detuning_by_Gamma*1.8)/2.5)

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('img/optical_molasses_force.pgf', bbox_inches='tight')
plt.show()

# %%
# Capture velocity
## Comparing Lunden and my own
r_trap = 7e-3
s_0s = np.linspace(0, 1.3, 100)
v_high = v_capture_high(r_trap=r_trap) * np.ones(shape=s_0s.shape)
v_low = v_capture_low(s_0=s_0s, k=k_D2, delta=-5*Gamma, r_trap=r_trap, theta=0)

plt.figure(figsize=(10*cm, 4*cm))
plt.ylabel('$v_\mathrm{max, capture}$ in m/s')
plt.xlabel('saturation $s_0$')
plt.plot(s_0s, v_high, label=r'$v_\mathrm{max, capture}^\mathrm{high}$')
plt.plot(s_0s, v_low, label=r'$v_\mathrm{max, capture}^\mathrm{low}$')
plt.legend()
plt.grid()
# plt.tight_layout()
plt.savefig('img/capture_velocity_comparison.pgf', bbox_inches='tight')
plt.show()

print(f'v_high(r_trap=7mm) = {v_capture_high(7e-3)} m/s')

# %%
# Resonance velocity
gradients = np.linspace(0, 80, 400)*1e-2  # T/m
deltas = np.linspace(-20, -1, 200)

G, D = np.meshgrid(gradients, deltas)
V = v_resonance(k=k_D2, delta=D*Gamma, grad=G, r_trap=7e-3, theta=deg_to_rad(0))

fig = plt.figure(figsize=(8*cm, 6*cm))
plt.xlabel('gradient in G/cm')
plt.ylabel('detuning in $\Gamma$')
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("Custom", [thesis_gray, thesis_rebecca, thesis_fuchsia, thesis_blue], N=1000)
plt.contourf(G*1e2, D, V, 8, cmap=cmap)

cax = make_axes_locatable(plt.gca()).append_axes('right', size='5%', pad=0.5*cm)
plt.colorbar(cax=cax, label=r'$v_\mathrm{max, resonance}$ in m/s')
plt.savefig('img/resonance_velocity_map.pgf', bbox_inches='tight')
plt.show()

print(v_resonance(k=k_D2, delta=-5*Gamma, grad=57/1e2, r_trap=7e-3, theta=deg_to_rad(30)))
# %%

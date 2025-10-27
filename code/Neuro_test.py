import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
N = 400
dt = 0.02
t_total = 100000 * dt
time = np.arange(0, t_total, dt)
tme = 20
tmi = 10
tms = 10
taue = 2
taui = 7.5
taus = 15
mue = 1.25
mui = -0.5
mus = -2
dele = 0.1
deli = 0.1
dels = 0.1
ampe = 2
ampi = 0
amps = 0
wid = 60
tone = 1000
toni = 0
tons = 0
ld = 0.85
gee = 1.5
gei = 2
ges = 4.25
gie = 1
gii = 0.5
gis = 0
gse = 2
gsi = 0.5
gss = 0

# Initialize the matrices for the network
def generate_normalized_matrix(N, sigma=2):
    X = np.linspace(0, 1, N)
    X = X[:, np.newaxis]
    M = np.exp(-(X - X.T) ** 2 / sigma**2)
    row_sums = M.sum(axis=1, keepdims=True)
    M_normalized = M / row_sums
    return M_normalized

sigmae = 0.5
sigmai = sigmas = 0.1
Mee = generate_normalized_matrix(N, sigmae)
Mei = generate_normalized_matrix(N, sigmai)
Mes = generate_normalized_matrix(N, sigmas)
Mie = generate_normalized_matrix(N, sigmae)
Mii = generate_normalized_matrix(N, sigmai)
Mis = generate_normalized_matrix(N, sigmas)
Mse = generate_normalized_matrix(N, sigmae)
Msi = generate_normalized_matrix(N, sigmai)
Mss = generate_normalized_matrix(N, sigmas)

# For the small limit cycle.
ae = 1.196257
be = 0.302558
ai = 0.165609
bi = -0.31882
as_ = 0.069508  # 'as' is a Python keyword, so use 'as_' instead
bs = -0.782826

rand_e = np.tan(np.pi * np.random.rand(N) - np.pi / 2)
rand_i = np.tan(np.pi * np.random.rand(N) - np.pi / 2)
rand_s = np.tan(np.pi * np.random.rand(N) - np.pi / 2)

v_e = be + ae * rand_e
v_i = bi + ai * rand_i
v_s = bs + as_ * rand_s

qe = 2 * np.arctan(v_e)
qi = 2 * np.arctan(v_i)
qs = 2 * np.arctan(v_s)

se = np.full(N, 0.358599)
si = np.full(N, 0.084618)
ss = np.full(N, 0.035599)

# Given initial conditions for synaptic variables
sebar = np.zeros(len(time))  # Assuming all start with the same initial condition
sibar = np.zeros(len(time))
ssbar = np.zeros(len(time))

se_heatmap = np.zeros((len(time), N))  # For storing se values over time

def bump(t):
    return (t > 0) & (t < wid)

nstim = 200
z = np.zeros(N)
z[:nstim] = 1

xie = np.tan(-np.pi / 2 + np.pi * np.random.rand(N))
xii = np.tan(-np.pi / 2 + np.pi * np.random.rand(N))
xis = np.tan(-np.pi / 2 + np.pi * np.random.rand(N))

for j in range(1, len(time)):
    t = j * dt
    ie = ampe * bump(t - tone) * z
    ii = ampi * bump(t - toni) * z
    is_ = amps * bump(t - tons) * z

    qpe = qe + dt * (1 - np.cos(qe) + (1 + np.cos(qe)) * (mue + ie + gee * np.dot(Mee, se) - gie * np.dot(Mie, si) - ld * gse * np.dot(Mse, ss) + dele * xie)) / tme
    qpi = qi + dt * (1 - np.cos(qi) + (1 + np.cos(qi)) * (mui + ii + gei * np.dot(Mei, se) - gii * np.dot(Mii, si) - ld * gsi * np.dot(Msi, ss) + deli * xii)) / tmi
    qps = qs + dt * (1 - np.cos(qs) + (1 + np.cos(qs)) * (mus + is_ + ges * np.dot(Mes, se) - gis * np.dot(Mis, si) - gss * np.dot(Mss, ss) + dels * xis)) / tms

    fe = qpe > np.pi
    fi = qpi > np.pi
    fs = qps > np.pi

    se = (1 - dt / taue) * se + fe * tme / taue
    si = (1 - dt / taui) * si + fi * tmi / taui
    ss = (1 - dt / taus) * ss + fs * tms / taus

    se_heatmap[j] = se  # Store the current se values
    
    sebar[j] = np.sum(se)/N #I thik the normal code and this one is different as here all the se entries are summed. 
    sibar[j] = np.sum(si)/N
    ssbar[j] = np.sum(ss)/N

    qe = qpe - 2 * np.pi * fe
    qi = qpi - 2 * np.pi * fi
    qs = qps - 2 * np.pi * fs


# # Plot the excitable variable `se` versus time
# plt.figure(figsize=(10, 6))
# plt.plot(time, sebar, label='se')
# plt.title('sebar vs. Time')
# plt.xlabel('Time')
# plt.ylabel('se')
# plt.legend()
# plt.show()

# # Plotting the heatmap for synaptic variable 'se'
# plt.figure(figsize=(10, 8))
# plt.imshow(se_heatmap.T, aspect='auto', origin='lower', cmap='viridis', extent=[0, time[-1], 0, N])
# plt.colorbar(label='Synaptic variable se')
# plt.xlabel('Time (s)')
# plt.ylabel('Neuron index')
# plt.title('200 is excited')
# plt.show()


fig, axs = plt.subplots(2, 1, figsize=(10, 14))

# Plot the excitable variable `se` versus time on the first subplot
axs[0].plot(time, sebar, label='se')
axs[0].set_title('sebar vs. Time')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('se')
axs[0].legend()

# Plotting the heatmap for synaptic variable 'se' on the second subplot
cax = axs[1].imshow(se_heatmap.T, aspect='auto', origin='lower', cmap='viridis', extent=[0, time[-1], 0, N])
fig.colorbar(cax, ax=axs[1], label='Synaptic variable se')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Neuron index')
axs[1].set_title('200 is excited')

# Adjust layout to make space for titles and labels
fig.tight_layout()

# Show the combined figure
plt.show()
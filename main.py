# Heekyung Lee 
# ~2024.05.23 Computer Graphics Lab Research Project (POSTECH, prof. Beak Seung-Hwan)

import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data, extract_elements
from utils import sphere_coordinates, convert_num2rad, extract_mueller_values

pi = 3.14159265358979323846

#file_path = '/write your .mat file path here/'
pbrdf_mat_data = load_data(file_path)

pbrdf_T, pbrdf_T_f, phi_d, theta_d, theta_h, wavelengths = extract_elements(pbrdf_mat_data)
pbrdf_reshaped = np.reshape(pbrdf_T_f, (len(phi_d), len(theta_d), len(theta_h), len(wavelengths), 16))
mueller_matrix = pbrdf_reshaped

########### fix input vector 
phi_i = convert_num2rad(45) ## change input vector phi
theta_i = convert_num2rad(270) ## change input vector theta

x_i, y_i, z_i = sphere_coordinates(1, phi_i, theta_i)
in_vector = np.array([x_i, y_i, z_i]) # fixed input vector

########### mueller element, wavelengths index
wavelength_index = 0 ## change the index of wavelengths [450, 500, 550, 600, 650]
mueller_element_index = 15 ## change the index of mueller elements [0~15]
mueller_element = mueller_matrix[:,:,:,wavelength_index,mueller_element_index]

###########out_vector = phi: 0~360, theta: 0~90

########### pBRDF coordinate coordinate base vectors
p = np.array([0, 0, 0]) #p :(0,0,0)
t = np.array([0, -1, 0]) #t :(0,-1, 0)
n = np.array([0, 0, 1]) #n: (0, 0, 1)
b = np.array([1, 0, 0]) #b: (1, 0, 0)

fig, ax = plt.subplots(figsize = (6,6),subplot_kw={'aspect': 'equal'})
norm = plt.Normalize(vmin=-0.01, vmax=0.01) #mueller element value range - normalize can be done differently
mueller_values = extract_mueller_values(in_vector, n, mueller_element, phi_d, theta_d, theta_h) 

x_vals = []
y_vals = []
z_vals = []
colors = []

for i in range (0, 361):
    for j in range(0, 91):
        x, y, z = sphere_coordinates(1, i, j)
        x_vals.append(x)
        y_vals.append(y)
        z_vals.append(z)
        colors.append(mueller_values[j][i])

colors = np.array(colors)
scatter= ax.scatter(x_vals, y_vals, z_vals, c= colors, cmap= 'bwr', norm=norm)

t_end = p + t
n_end = p + n
b_end = p + b
in_vector_end = p + in_vector

# pbrdf coordinate vector point
ax.plot(p[0], p[1], 'go', label='p')
ax.plot(t_end[0], t_end[1], 'ro', label='t')
ax.plot(n_end[0], n_end[1], 'bo', label='n')
ax.plot(b_end[0], b_end[1], 'o', color='orange', label='b')
ax.plot(in_vector_end[0], in_vector_end[1], 'ko', label='in_vector')

#phi index line
for phi in range(0, 360, 45):
    phi_rad = np.radians(phi)
    x_line = np.cos(phi_rad)
    y_line = np.sin(phi_rad)
    ax.plot([0, x_line], [0, y_line], color='gray')

circle = plt.Circle((0, 0), 1, color='white', fill=False)
ax.add_artist(circle)

ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
cbar = plt.colorbar(scatter, ax=ax, shrink=1, aspect=15)
cbar.set_label('mueller element value')
plt.show()


# for i in range(16):
#     print("==================mueller element: [", i+1 ,"] ======================")
#     mueller_element = mueller_matrix[:,:,:,wavelength_index,i]
#     mueller_values = extract_mueller_values(in_vector, n, mueller_element, phi_d, theta_d, theta_h)
#     plot_mueller_values(mueller_values, p, t, n, b, in_vector)

# for i in range(5):
#     mueller_element = mueller_matrix[:,:,:,i,15]
#     mueller_values = extract_mueller_values(in_vector, n, mueller_element, phi_d, theta_d, theta_h)
#     plot_mueller_values(mueller_values, p, t, n, b, in_vector)

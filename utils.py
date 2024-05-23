# function definitions for calculation of vectors, plot

import numpy as np
import matplotlib.pyplot as plt
pi = 3.14159265358979323846

def sphere_coordinates(radius,phi, theta):
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    return x,y,z

def convert_num2rad(num):
    rad = num * pi / 180
    return rad

def calculate_angles(in_vector, out_vector, n):
    #cacluation of phi_d, theta_d, theta_h
    #consider pBRDF definition
    h = (in_vector + out_vector) / np.linalg.norm(in_vector + out_vector) #h = half vector
    theta_h = np.arccos(np.dot(h, n) / (np.linalg.norm(h) * np.linalg.norm(n)))  # theta_h
    theta_d = np.arccos(np.dot(h, in_vector) / (np.linalg.norm(h) * np.linalg.norm(in_vector)))  # theta_d
    phi_d = np.arccos(np.dot(n, in_vector) / (np.linalg.norm(n) * np.linalg.norm(in_vector)))  # phi_d

    return phi_d, theta_h, theta_h

def find_closest_index(array, value):
    # linear interpolation to find closest matching index
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def find_mueller_index(phi_d, theta_d, theta_h, target_phi, target_theta_d, target_theta_h, mueller_element):
    phi_d_index = find_closest_index(phi_d, target_phi)
    theta_d_index = find_closest_index(theta_d, target_theta_d)
    theta_h_index = find_closest_index(theta_h, target_theta_h)
    mueller_index = mueller_element[phi_d_index, theta_d_index, theta_h_index]
    return mueller_index

def calculate_colors(z):
    colors = z / np.max(z)
    return colors

def extract_mueller_values(in_vector, n, mueller_element, phi_d, theta_d, theta_h):
    count =0
    mueller_values = np.zeros((91, 361)) #mueller value 저장 2차원 배열

    for phi in range(0,361):
        for theta in range(0,91):
            #####output vector fixed for all phi, theta
            phi_o= phi
            theta_o = theta
            x_o, y_o, z_o = sphere_coordinates(1, phi_o, theta_o)
            out_vector = np.array([x_o, y_o, z_o]) # out_vector

            calculated_phi_d, calculated_theta_h, calculated_theta_d = calculate_angles(in_vector, out_vector, n)
            mueller_value = find_mueller_index(phi_d, theta_d, theta_h, calculated_phi_d, calculated_theta_d, calculated_theta_h, mueller_element)
            # print("[",theta,"]","[",phi,"]","mueller value: ", index)

            mueller_values[theta][phi] = mueller_value #mueller value 저장
            count +=1

    # print(mueller_values.shape)
    return mueller_values

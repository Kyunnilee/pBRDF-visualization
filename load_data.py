# file to load .mat file and extract elements

import scipy.io
import numpy as np

def load_data(filepath) -> np.ndarray:
    pbrdf_mat_data = scipy.io.loadmat(filepath)
    return pbrdf_mat_data

def print_shape(pbrdf_T, phi_d, theta_d, theta_h, wavelengths):
    print('=======pbrdf_array size=======')
    print('pbrdf_T shape: ', pbrdf_T.shape)
    print('phi_d shape: ', phi_d.shape)
    print('theta_d shape: ', theta_d.shape)
    print('theta_h shape: ', theta_h.shape)
    print('wavelengths shape: ', wavelengths.shape)
    print('=========================')

def extract_elements(data: np.ndarray) -> tuple:
    # extract each elements in .mat file
    pbrdf_T = data['pbrdf_T']
    pbrdf_T_f = data['pbrdf_T_f']
    phi_d = data['phi_d'][0]
    theta_d = data['theta_d'][0]
    theta_h = data['theta_h'][0]
    wavelengths = data['wvls'][0]
    print_shape(pbrdf_T_f, phi_d, theta_d, theta_h, wavelengths)
    
    return pbrdf_T, pbrdf_T_f, phi_d, theta_d, theta_h, wavelengths


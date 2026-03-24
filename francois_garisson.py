import numpy as np
def boric_acid_contribution(c, S, T, z, pH):
    A1 = 8.86 / c * 10 ** (0.78 * pH - 5)
    P1 = 1
    f1 = 2.8 * np.sqrt(S / 35) * 10 ** (4 - 1245 / (T + 273))
    c = 1412 + 3.21 * T + 1.19 * S + 0.0167 * z
    return A1, P1, f1, c

def magnesium_sulfate_contribution(c, S, T, z):
    A2 = 21.44 * S / c * (1 + 0.025 * T)
    P2 = 1 - 1.37e-4 * z + 6.2e-9 * z**2
    f2 = 8.17 * 10 ** (8 - 1990 / (T + 273)) / (1 + 0.0018 * (S - 35))
    return A2, P2, f2

def pure_water_contribution(T, z):
    P3 = 1 - 3.83e-5 * z + 4.9e-10 * z**2
    if T <= 20: 
        A3 = 4.937e-4 - 2.59e-5 * T + 9.11e-7 * T**2 - 1.5e-8 * T**3 
    else:
        A3 = 3.964e-4 - 1.146e-5 * T + 1.45e-7 * T**2 - 6.5e-10 * T**3
    return A3, P3

def compute_alpha(c, S, T, z, f, pH = 7.5): 
    A1, P1, f1, c =  boric_acid_contribution(c, S, T, z, pH)
    A2, P2, f2 = magnesium_sulfate_contribution(c, S, T, z)
    A3, P3 = pure_water_contribution(T, z)
    return A1 * P1 * (f1 * f**2 / (f1**2 + f**2)) + A2 * P2 * (f2 * f**2 / (f2**2 + f**2)) + A3 * P3 * f**2 

print(compute_alpha(1500, 35, 10, 1000, 40))
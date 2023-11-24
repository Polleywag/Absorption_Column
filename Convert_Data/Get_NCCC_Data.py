import pandas as pd
import numpy as np


def get_NCCC_data(index=0, average=False):

    data = pd.read_csv(r'C:\Users\364265\Documents\Absorption_Column_7.0\data\NCCC_Data.csv', index_col=0)
    data = data.dropna(how='all')
    data = data.dropna(how='all', axis=1)

    if average:
        m_T_l = np.array(data['L'])      # Liquid Mass Flow Rate (kg/s)
        m_T_v = np.array(data['G'])      # Vapor Mass Flow Rate (kg/s)
        alpha = np.array(data['alpha'])  # CO2 Loading in Lean Solvent
        w_MEA = np.array(data['w_MEA'])  # MEA weight fraction in Lean Solvent
        y_CO2 = np.array(data['y_CO2'])  # Vapor Mole Fraction of CO2

        X = np.array([np.mean(m_T_l), np.mean(m_T_v), np.mean(alpha), np.mean(w_MEA), np.mean(y_CO2)])
        X = np.round(X, 4)
        return X

    else:
        i = index
        m_T_l = np.array(data['L'])[i]      # Liquid Mass Flow Rate (kg/s)
        m_T_v = np.array(data['G'])[i]      # Vapor Mass Flow Rate (kg/s)
        alpha = np.array(data['alpha'])[i]  # CO2 Loading in Lean Solvent
        w_MEA = np.array(data['w_MEA'])[i]  # MEA weight fraction in Lean Solvent
        y_CO2 = np.array(data['y_CO2'])[i]  # Vapor Mole Fraction of CO2

        X = [m_T_l, m_T_v, alpha, w_MEA, y_CO2]
        return X

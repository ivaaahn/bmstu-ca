import numpy as np

def read_table(path: str) -> np.ndarray:
    return np.loadtxt(path)
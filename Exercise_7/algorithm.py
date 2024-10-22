import numpy as np

def algorithm(xn: np.ndarray, fs: int, N: int = 1024)->float:
    freq_content = np.fft.fft(xn,fs=fs)

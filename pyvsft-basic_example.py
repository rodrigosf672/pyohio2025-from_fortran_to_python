import numpy as np
import cracker
import timeit

# Fortran version
def run_fortran():
    y0 = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    h = 0.1
    n = 1000
    cracker.rk4g_solver(n, h, y0)

# Python version
def run_python():
    y0 = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    h = 0.1
    n = 1000

    A = (np.sqrt(2) - 1) / 2
    B = (2 - np.sqrt(2)) / 2
    C = -np.sqrt(2) / 2
    D = (2 + np.sqrt(2)) / 2

    def dydz(y):
        dy = np.zeros(3)
        k1, k2 = 1.0, 0.5
        dy[0] = -k1 * y[0]
        dy[1] = k1 * y[0] - k2 * y[1]
        dy[2] = k1 * y[0] + k2 * y[1]
        return dy

    y = np.zeros((n+1, 3))
    y[0] = y0
    for i in range(n):
        K1 = dydz(y[i])
        K2 = dydz(y[i] + 0.5 * h * K1)
        K3 = dydz(y[i] + h * (A * K1 + B * K2))
        K4 = dydz(y[i] + h * (C * K2 + D * K3))
        y[i+1] = y[i] + (h/6)*(K1 + K4) + (h/3)*(B*K2 + D*K3)

# Benchmarking
time_fortran = timeit.timeit("run_fortran()", globals=globals(), number=10)
time_python = timeit.timeit("run_python()", globals=globals(), number=10)

print(f"Fortran average time: {time_fortran:.6f} seconds")
print(f"Python average time:  {time_python:.6f} seconds")
print(f"Speedup: Fortran is {time_python / time_fortran:.2f}x faster")

import numpy as np
import cracker
import timeit
import matplotlib.pyplot as plt

# Fortran version
def run_fortran(n, h=0.1):
    y0 = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    cracker.rk4g_solver(n, h, y0)

# Python version
def run_python(n, h=0.1):
    y0 = np.array([1.0, 0.0, 0.0], dtype=np.float64)

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
ns = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
python_times = []
fortran_times = []

for n in ns:
    tf = timeit.timeit(lambda: run_fortran(n), number=5)
    tp = timeit.timeit(lambda: run_python(n), number=5)
    fortran_times.append(tf)
    python_times.append(tp)
    print(f"n={n} | Fortran: {tf:.4f}s | Python: {tp:.4f}s | Speedup: {tp/tf:.2f}x")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(ns, python_times, marker='o', label='Python (Runge-Kutta-Gill)')
plt.plot(ns, fortran_times, marker='s', label='Fortran (f2py)')
plt.xlabel("Number of Steps (n)")
plt.ylabel("Time (seconds) over 5 runs")
plt.title("Runtime Comparison: Python vs Fortran")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

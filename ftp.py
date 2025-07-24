import importlib.util
import numpy as np
import matplotlib.pyplot as plt

# Path to compiled .so file
path = "./cracker.cpython-312-darwin.so"

# Load the cracker module manually
spec = importlib.util.spec_from_file_location("cracker", path)
cracker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cracker)

# Simulation parameters
h = 0.1
n_steps = 100
y0 = np.array([1.0, 0.0, 0.0], dtype=np.float64)
y_out = np.zeros((3, n_steps + 1), dtype=np.float64)

# Call Fortran subroutine
y_out = cracker.rk4g_solver(n_steps, h, y0)

# Plot results
z = np.linspace(0, h * n_steps, n_steps + 1)
plt.plot(z, y_out[0], label="EDC")
plt.plot(z, y_out[1], label="MVC")
plt.plot(z, y_out[2], label="HCl")
plt.xlabel("z")
plt.ylabel("Concentration")
plt.title("Thermal Cracking of EDC (Fortran + Python)")
plt.legend()
plt.grid(True)
plt.show()

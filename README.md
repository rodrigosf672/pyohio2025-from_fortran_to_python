# From Fortran to Python: A Conversation Across Generations of Scientific Computing

This project demonstrates how to integrate legacy Fortran code with Python to solve a system of ordinary differential equations (ODEs) modeling the thermal cracking of Ethylene Dichloride (EDC). We compare the performance of a compiled Fortran implementation with a pure Python version using the Runge-Kutta-Gill method.

> This project accompanies a talk at [PyOhio 2025](https://www.pyohio.org/2025/program/talks/from-fortran-to-python/).

## Problem Overview

We model a two-step reaction system:

```
EDC → MVC + HCl         (rate constant k1 = 1.0)
MVC → HCl               (rate constant k2 = 0.5)
```

Expressed as ODEs:

\[
\begin{aligned}
\frac{dy_1}{dz} &= -k_1 y_1 \\
\frac{dy_2}{dz} &= k_1 y_1 - k_2 y_2 \\
\frac{dy_3}{dz} &= k_1 y_1 + k_2 y_2
\end{aligned}
\]

Initial condition:
\[
y(0) = [1.0,\ 0.0,\ 0.0]
\]

## Project Structure

```
.
├── cracker.cpython-312-darwin.so       # Compiled Fortran module (Python 3.12)
├── cracker.cpython-313-darwin.so       # Compiled Fortran module (Python 3.13)
├── SummaryResults-FortranvsPython.pdf  # PDF report for performance results (summarized)
├── fortran-code.f90                    # Fortran source code
├── ftp.py                              # Run and plot the Fortran-based simulation
├── pyvsft-basic_example.py             # Benchmark Fortran vs Python (single value of n)
├── pyvsft-with_steps.py                # Benchmark across multiple values of n
├── requirements.txt                    # Python dependencies
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rodrigosf672/pyohio2025-from_fortran_to_python.git
cd pyohio2025-from_fortran_to_python
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Compile the Fortran Code

Make sure you have `gfortran` installed. Then run:

```bash
f2py -c fortran-code.f90 -m cracker
```

This generates a `.so` file that Python can import. In case you have problems with this step, you can find two already compiled `.so` files for Python 3.12 and 3.13 in this repo.

## Usage

- **Plot chemical concentration profile**:
  ```bash
  python ftp.py
  ```

- **Run basic benchmark (n=1000)**:
  ```bash
  python pyvsft-basic_example.py
  ```

- **Run benchmark over multiple step sizes - takes a long time!**:
  ```bash
  python pyvsft-with_steps.py
  ```

## Key Takeaways

- Fortran provides significant performance advantages for numerical solvers.
- Python offers ease of prototyping, visualization, and benchmarking.
- Together, they demonstrate the power of using the right tool for the right job.
- Our Fortran implementation runs up to **700× faster** than the pure Python version.

## License

This project is licensed under the MIT License.

## References

This work was inspired by the following publication:

Schirmeister, R., Kahsnitz, J., & Träger, M. (2009). Influence of EDC cracking severity on the marginal costs of vinyl chloride production. 
Industrial & Engineering Chemistry Research, 48(6), 2801–2809. https://doi.org/10.1021/ie8006903

## Authors

- [Rodrigo Silva Ferreira](https://www.pyohio.org/2025/program/speakers/rodrigo-silva-ferreira/)
- [Prof. Helianildes Silva Ferreira](https://www.pyohio.org/2025/program/speakers/helianildes-silva-ferreira/)

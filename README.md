# From Fortran to Python: A Conversation Across Generations of Scientific Computing

This project demonstrates how to integrate legacy Fortran code with Python to solve a system of ordinary differential equations (ODEs) modeling the thermal cracking of Ethylene Dichloride (EDC). We compare the performance of a compiled Fortran implementation with a pure Python version using the Runge-Kutta-Gill method.

> This project accompanies a talk at [PyOhio 2025](https://www.pyohio.org/2025/program/talks/from-fortran-to-python/).

## Problem Overview

We model a two-step reaction system:

```
EDC → MVC + HCl         (rate constant k1 = 1.0)
MVC → HCl               (rate constant k2 = 0.5)
```

<img width="866" height="335" alt="image" src="https://github.com/user-attachments/assets/4531c1eb-a52e-4fe0-a13c-2c8a3c42d234" />


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

To compile the fortran code, you need to have `f2py` installed, which comes with NumPy. However, the backend Fortran compiler for Python versions 3.12 and above has changed, hence being necessary to install `meson` and `ninja`:

```bash
brew install meson ninja  # macOS (use equivalent commands for Ubuntu/Windows)
```
> Meson reads the Fortran file and generates a Ninja build script.
> Ninja runs the compilation commands (e.g., using gfortran) to build the `.so` file.

Then, you can compile the Fortran code using `f2py`:

```bash
f2py -c fortran-code.f90 -m cracker
```

This generates a `.so` file that Python can import. 

> In case you have problems with this step, you can find two already compiled `.so` files for Python 3.12 and 3.13 in this repo.

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

This project was inspired by prior studies that modeled the cracking of Ethylene Dichloride (EDC), particularly:

- Ferreira, H. S. (2003).  
  **Métodos matemáticos em modelagem e simulação do craqueamento térmico do 1,2-Dicloroetano.**  
  *Doctoral dissertation, University of Campinas, Brazil.*
  [https://repositorio.unicamp.br/Busca/Download?codigoArquivo=477111](https://repositorio.unicamp.br/Busca/Download?codigoArquivo=477111)

- Schirmeister, R., Kahsnitz, J., & Träger, M. (2009).  
  **Influence of EDC cracking severity on the marginal costs of vinyl chloride production.**  
  *Industrial & Engineering Chemistry Research*, 48(6), 2801–2809.  
  [https://doi.org/10.1021/ie8006903](https://doi.org/10.1021/ie8006903)

- Fahiminezhad, A., Peyghambarzadeh, S. M., & Rezaeimanesh, M. (2020).  
  **Numerical Modelling and Industrial Verification of Ethylene Dichloride Cracking Furnace.**  
  *Journal of Chemical and Petroleum Engineering*, 54(2), 165–185.  
  [https://doi.org/10.22059/jchpe.2020.286558.1291](https://doi.org/10.22059/jchpe.2020.286558.1291)

These works provided a foundation for understanding the chemical and engineering significance of EDC cracking.  
What we present here is a **highly simplified model**, focusing on the reaction kinetics and solver performance. Hence, this work does not explore industrial-scale reactor behavior, fluid dynamics, or heat transfer, which are crucial in the real-world systems studied in the references above.

## Authors

- [Rodrigo Silva Ferreira](https://www.pyohio.org/2025/program/speakers/rodrigo-silva-ferreira/)
- [Prof. Helianildes Silva Ferreira](https://www.pyohio.org/2025/program/speakers/helianildes-silva-ferreira/)

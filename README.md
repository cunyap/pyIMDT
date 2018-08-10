## Scope of the inertial mass determination module

Calculation of the mass from txt and tdms data files

## Minimal needed functions

### Import functions

```python
def read_initial_frequency_shift(file):
# get intial frequency shift
# beforeCell = initial(txt_file1)
# afterCell = initial(txt_file2)

return [frequency, phase]
```

```python
def read_tdms_data(file):

if sweep_mode:
# faa = Sweeps(tmds_file)
else:
# faa = PLL(tdms_file)
return data_frame
```

### Analysis functions
```python
def calculate_function_fit(frequency, phase):
# fb = fitting(beforeCell)
# fa = fitting(afterCell)
return resonance_frequency_array
```

```python
def calculate_mass(fa, fb, ffa):
# mass as a function of frequency
return mass   
```

```python
def calculate_resonance_frequencies(tdms_data):
# loops over fitting (calculate_function_fit)
return [resonance_frequency_array] 
```

### Ploting functions
```python
def plot_mass(fa, fb, faa):
# mass = mass(fb,fa,faa)
```

test
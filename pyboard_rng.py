# pyboard_rng.py
"""
Random Number Generator

RNG Library (Call to Pyboard chip hard-coded RNG function) 
"""

import pyb

# Open the output file
filename = '200000_RNG.csv'

# Open the file for writing
with open(filename, 'w') as f:
    # Write the header of the file
    f.write("Iteration ; Random Number\n")
    
    # Generate and save 200,000 random numbers
    for i in range(1, 200001):
        rng_value = pyb.rng()              # Generate a random number using the pyb.rng() method
        f.write(f"{i} ; {rng_value}\n")    # Write the iteration and random number to the file

print(f"Results written to {filename}")

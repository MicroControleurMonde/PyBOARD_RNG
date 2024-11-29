# PyBOARD_RNG

![pic](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/MicroPython.jpg)

**Abstract:** Micro-python implementation of the **`pyb.rng()`** function to generate random numbers. The function specifically calls the hardcoded RNG in the chip directly (*as for the ESP32*)

## Generator coding:

Here is a typical example of use :

    import pyb
    random_number = pyb.rng()  # Returns a 32-bit random number
    print(random_number)
    
    Output: 112922794
I made a very basic code that makes 200'000 calls to the 'pyb.rng()' function. Here: [pyboard_rng.py](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/pyboard_rng.py)

The output file is a csv (200000_RNG.csv)

## Performance:

- Time spent to generate 200'000 values: 108 seconds (avg)
- Throughput: 7,407 bytes/sec
- 1847 random values / sec.

## Ent Test Report:

## Dieharder Test Report

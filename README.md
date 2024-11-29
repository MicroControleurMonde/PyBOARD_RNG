# PyBOARD_RNG

![pic](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/MicroPython.jpg)

**Abstract:** Micro-python implementation of the **`pyb.rng()`** function to generate random numbers. The function specifically calls the hardcoded RNG in the chip directly (*as for the ESP32*)

Here is a typical example of use :

    import pyb
    random_number = pyb.rng()  # Returns a 32-bit random number
    print(random_number)
    
    Output: 112922794

## Performance:

- Time spent to generate 200'000 values: 108 seconds (avg)
- Throughput: 7,407 bytes/sec
- 1847 random values / sec.

## Ent Test Report:

## Dieharder Test Report

# PyBOARD_RNG

![Pic](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/MicroPython.jpg)

**Abstract:** Micro-python implementation of the **`pyb.rng()`** function to generate random numbers. The function specifically calls the hardcoded RNG in the chip directly (*as for the ESP32*)

Here is a typical example of use :

    import pyb
    random_number = pyb.rng()  # Returns a 32-bit random number
    print(random_number)
    
Output: 112922794

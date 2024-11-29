# PyBOARD_RNG

![pic](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/MicroPython.jpg)

**Abstract:** Micro-python implementation of the **`pyb.rng()`** function to generate random numbers. 

The function specifically calls the hardcoded RNG in the chip directly (*as for the ESP32*)

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

(www.fourmilab.ch) John Walker

- Sample size: **2 MB**
- Total generated: **200'000 values**
- [Ent Report -Raw](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/Ent_report.txt)
- [Ent Report Analyse](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/Ent_Report_Analyse.md)

## Dieharder Test Report

(https://webhome.phy.duke.edu/~rgb/General/dieharder.php) Robert G. Brown

- Sample size: **2 MB**
- Total generated: **200'000 values**
- [Dieharder Report - Raw](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/dieharder%20200000.txt)
- [Dieharder Report Analyses](https://github.com/MicroControleurMonde/PyBOARD_RNG/blob/main/Reports/Dieharder_Report_Analyses.md)




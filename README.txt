This program written in Python3.6 calculates the area under the Gaussian bell curve between an upper and an a lower limit (defining the interval) by using the cumulative distribution function.

INPUT: 
1. left entry field takes the lower limit (set to -infinity if left empty)
2. right entry field takes the upper limit (set to +infinity if left empty)
    
OUTPUT:
1. probability that an individual of a population resides in the interval defined by the lower and upper limit

******
In this version the following changes have been applied:
- removal of some code duplication in try-except clauses
- PhotoImage to incorporate image import of Gaussian curve
- restructured calls by adding self and replacing None->root
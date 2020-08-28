# CSVErrorGenerator
Tool that parses csv files to: 

     generate mean, norm mean, and standard deviation of the error using (Signed Percent Error, Relative Distance, Absolute Percent Error ).

     generate the pearson correlation coefficient\n

     generate the above statistics after trimming upper α/2 and lower α/2 from an array of α's\n
     


## Usage

     #python > 3
     
     python console.py -h

     usage: console.py [-h] [-p [P [P ...]]] [-o O] E D

     Generate statistical info on error from csv files.

     positional arguments:
        E                     <spe | ape | rd> ----- signed_percent_error, abs_percent_error, relative_distance
        D                     specify relative path of parent directory

     optional arguments:
        -h, --help            show this help message and exit
        -p [P [P ...]], --percents [P [P ...]]
                           floating point numbers to trim the csv data; default=[0.01, 0.025, 0.05, 0.1, 0.15]
        -o O, --output O      Name of output file; default=output_log.csv
        
Note: all *.csv in dir will be analyzed (recursive)

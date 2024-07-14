#!/usr/bin/env python

# Import the sys library 
# for writing and reading the standard input and output
import sys




# For each new line in the standard input (stdin) 
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    # strip removes whitespaces and new lines at the beginning and end of the line
    # the result is a tuple with 6 elements
    data = line.strip().split("\t")

    # Raise error if the tuple is not 6 elements
    if len(data) != 6:
        raise ValueError(f"Should be 6 elements, but got {len(data)}: {data}")

    # store the 6 elements of the tuple in seperate variables
    date, time, item, category, sales, payment = data

    # Write the key-value combination to standard output (stdout)
    # Key is the payment, value is the sales     
    # With a tab (\t) between key and value
    # New line \n means new record
    sys.stdout.write("{0}\t{1}\n".format(category, sales))

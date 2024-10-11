# gram-schmidt-calculator

README - GRAM-SCHMIDT ORTHOGONALIZATION CALCULATOR

PROJECT DESCRIPTION
The Gram-Schmidt Orthogonalization Calculator is a Python-based tool that
converts a set of vectors into an orthogonal or orthonormal set using
the Gram-Schmidt process. The new set can be rounded to a chosen value and
outputs can be saved to a CSV file. The program supports the input of 
vector sets using CSV files.


INSTALLATION

Ensure Python 3.11+ is installed. The program relies on the NumPy, argparse,
and math libraries for operation.

NumPy version 1.24.3 +
argparse version 3.2 +
math version 3.11 + (as function is built-in to Python)

To set it up, download orthogonalization_calculator.py and vector_operations.py 
into the desired directory. The files example_set.csv, example_complex_set.csv and 
program_tests.py are not required for operation but can be useful to the user.


USING THE PROGRAM

The program is to be used via the command line. To do this run the 
orthogonalization_calculator.py file with the following inputs (this 
example is for Windows PowerShell):
python orthogonalization_calculator.py [input_type] [settings] [save_output] 
•	[input_type]:  0 for CSV file input, 1 for manual input.
•	[settings]:    0 uses default settings (creates an orthonormal set rounded 
                   to 3 decimal places), 1 allows custom settings that will be inputted manually.
•	[save_output]: 0 prints the output to the console, 1 saves it to a CSV file (in 
                   addition to printing to the console).

The program will require additional inputs such as filenames, but these are stated
 and explained when required.

To test the key functionality of the program, run the program_test.py file as 
follows (this example is for Windows PowerShell):
python program_test.py
No command line arguments need to be specified when running the test file.


EXAMPLE USES

For file input with default settings and saving the output (in Windows PowerShell):
python orthogonalization_calculator.py 0 0 1 

For manual input with custom settings without saving (in Windows PowerShell):
python orthogonalization_calculator.py 1 1 0 
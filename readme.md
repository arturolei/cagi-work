
# Validations for 5-Hopkins Clinical Panel

I have prepared the following documentation to provide a gloss or better elucidate the
code that I have produced. 

## What's Included:
- 

NB: Although this repository on Github is public (and visible to anyone who knows my github address), the data
in the test files that I have created has all be fabricated by me. 


## Notes for Use/Instructions:

- The validation program is written in Python and works for **Python 3.x.** It has not been tested
for backwards compatibility. 

- The file-path in the program needs to be changed to reflect the user's file-path and name. 
See the code for more precise instructions on usage. 

- The program validates a .csv file. 
    - See the subsequent section "Justification for .csv Instead of .txt"
    
- In keeping with PEP 8 style guide for Python Code, I have opted to make the 
variable names as descriptive as possible. Hopefully, this will be evidenced in the comments
found in the code. 

- I interpreted the directive, "Please create a submission template with just 
one comment field per individual, rather than one comment field for every individual-to-disorder class match," as meaning that there should be one C field per individual (thus one C field per row of the csv table). 


### Justification For Use of .csv instead of .txt:
As this is a substantial change withr respect to precedent, some justification and clarification for 
the format change are required. It more or less comes down to "user-friendliness."

The csv or "comma seperated values" format is substantially easier to read, create, and edit for tables of data. 
CSV files can be opened, edited, and saved using MS Excel and other common spreadsheet programs. 

Lastly, I have included a file designated "csv-generator.py" which will convert a .txt file into a .csv file.
Worst case scenario: we will have an intermediary program to convert .txt to .csv. 

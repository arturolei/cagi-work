
# Validations for 5-Hopkins Clinical Panel

I have prepared the following documentation to provide a gloss or better elucidate the
code that I have produced. 

## What's Included:
- A validation program written in Python: 5-Hopkins_clinical_panel_validation_test.py
- Several test-files (csv and txt files ending with words "testfile" in name). 
    - The test-files represent several scenarios (a perfect scenario with everything passing, a near perfect
    scenario, a dimensional mismatch case or where the number of columns and rows is off, etc.)
        - Some of the test-files feature tables that are smaller; In order to carry out debugging tests, I had
        to create some fake data meeting various criteria, and I did not want to do this for a full fake data set.
-This readme file written in markdown. 
-Jupyter Notebook files; I have included these for the sake historical curiosity and 

NB: Although this repository on Github is public (and visible to anyone who knows my github address), the data
in the test files that I have created has all be fabricated by me. 


## Notes for Use/Instructions:

- The validation program is written in Python and works for **Python 3.x.** It has not been tested
for backwards compatibility. 
    - In essence, I translated/re-wrote the original Perl file into Python (again adopting the appropriate stylistic standards)
    and then modified the program accordingly. 

- The file-path in the program needs to be changed to reflect the user's file-path and name. 
See the code for more precise instructions on usage. However, here is what it looks like, where 
the first parameter of the open argument should be file-path with appropriate file-name. 

    - ```python 
       with open('5-Hopkins_clinical_panel_submission_template_testfile.csv', 'r') as my_csv_file:
          dic_patients_list = [item for item in csv.DictReader(my_csv_file)]
      ```

- The program validates a .csv file. 
    - See the subsequent section "Justification for use of .csv Instead of .txt"
    
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

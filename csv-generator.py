'''
CSV Generator:

This program converts a txt file into a csv file.  I have included it 
for the sake of completeness and thoroughness. 

I have included several 'print' statements for future debugging purposes;
I have commented them out, but they serve as a means of error-checking. 

Of course, let it be said that it's really "converter", not a "generator"
'''

import csv

with open ('5-Hopkins_clinical_panel_submission_template.txt', 'r') as my_file:
    column_headings = my_file.read().split(',')
    
print (column_headings, len(column_headings))
print (column_headings, type(column_headings))

rows_list = ['P'+ str(patient_num+1) for patient_num in range(106)]
blank_entries = ['*' for num in column_headings]
print(blank_entries)

starter_dict  = {key:value for key,value in zip(column_headings, blank_entries)}

print(starter_dict)

dict_list = []

#Create the non-header rows of csv table. 
for item in range(106):
    temp_dict = {'patient': 'P'+str(item+1), ' 1-P': '*', '1-SD': '*', '1-V': '*', ' 2-P': '*', '2-SD': '*', '2-V': '*', ' 3-P': '*', '3-SD': '*', '3-V': '*', '4-P': '*', '4-SD': '*', '4-V': '*', '5-P': '*', '5-SD': '*', '5-V': '*', '6-P': '*', '6-SD': '*', '6-V': '*', '7-P': '*', '7-SD': '*', '7-V': '*', '8-P': '*', ' 8-SD': '*', ' 8-V': '*', ' 8-C': '*', ' 9-P': '*', ' 9-SD': '*', ' 9-V': '*', ' 10-P': '*', '10-SD': '*', '10-V': '*', '10-C': '*', '11-P': '*', '11-SD': '*', ' 11-V': '*', ' 12-P': '*', '12-SD': '*', ' 12-V': '*', '13-P': '*', '13-SD': '*', '13-V': '*', ' 14-P': '*', '14-SD': '*', ' 14-V': '*', 'C': '*'}
    dict_list.append(temp_dict)
    
print (dict_list)

csv_keys = dict_list[0].keys()

#The first argument for open() is the file-path and name of file that will be created.
with open ('5-Hopkins_clinical_panel_submission_template2.csv','w') as my_new_file:
    dict_writer = csv.DictWriter(my_new_file, csv_keys)
    dict_writer.writeheader()
    dict_writer.writerows(dict_list)

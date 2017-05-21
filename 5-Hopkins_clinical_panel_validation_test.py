'''
########################################################################
#	Validations for 5-Hopkins Clinical Panel
#	Number of rows: 106 + 1 header row
#	Number of columns: 44
#   
In sets of 3:
#	1st (prediction) columns range: [0-1]
#	2nd (SD) columns range: 0+
#	3rd (variant) columns: CHROM:POS:REF:ALT, seperated by spaces
#   NB: Can do all or none, but prediction/sd/variant must come in sets
#
#For each row, there is an additional comment space. 
#C: optional, anything
#      
########################################################################
'''


import csv
import re

'''
INSTRUCTIONS:
The first argument for 'with open' is the file path. 
Write the appropriate file path for the first parameter.
NB: The default path is a "test file".

'''
with open('5-Hopkins_clinical_panel_submission_template_testfile.csv', 'r') as my_csv_file:
    dic_patients_list = [item for item in csv.DictReader(my_csv_file)]

#The following creates a list of dictionaries whose entries are the columns, e.g. patient #, 1-P, 2-P. 
patients_dict_list = [dict(item) for item in dic_patients_list]

#The rows are the patients (identified as P1-P106, a number based on CAGI-4). 

#A list of errors that will be displayed if the file fails validation and written into a text file.
error_list=[]

#Test to insure that the csv file has the proper dimensions. 

#Correct Dimensions
length_patients_dict = 3 #Based on CAGI-4 data.
num_col_standard= 44
'''
NB: 
For every disorder there are three values, P, SD, V (e.g. 1-P, 1-SD, 1-V, etc). There are 14 disorders. 
42 keys in each dictionary for each disorder, SD, and Variants. One cell for Patient designation and One
'''
misaligned_dict = False

#Check each row to make sure each row has correct number of elements. 
for patient_row in patients_dict_list:
    if len(patient_row) != num_col_standard:
        misaligned_dict = True

if (len(patients_dict_list) != length_patients_dict) or misaligned_dict == True:
    error_list.append("ERROR: The number of lines do not match the template/dimension mis-match. \nPlease try again.")

else:
    #Test to see if there are empty values in the table.
    for patient_row in patients_dict_list:
        for patient_key in patient_row.keys():
            if patient_row[patient_key] == '':
                error_list.append('ERROR: Empty value at row, column: '+ 
                                  item['patient']+" , "+ patient_file + "; Please leave '*' for empty value")

    #Appropriate P Values
    #Test probability values to make sure they are legitimate.
    for item in patients_dict_list:
        for patient_file in item.keys():
            if (patient_file[-1] =='P' and item[patient_file] != '*')and (float(item[patient_file]) > 1 or float(item[patient_file])<0):
                error_list.append('ERROR: Invalid P value for row/patient: '+ item['patient'] +
                      ', cell coordinates: '+ patient_file)      


    #SD Values:            
    #The following is a test to see if SD values are legtimate:

    patient_num_val = []
    test_dict ={}
    #The following dictionary, disorder_dict, serves to create a key for error handling.
    disorder_dict ={'0':'1', '3':'2', '6':'3', '9': '4', 
                    '12':'5', '15':'6', '18':'7', 
                    '21':'8', '24':'9','27': '10',
                   '30': '11', '33':'12', '36': '13','39':'14'}

    patient_list = [patient_row['patient'] for patient_row in patients_dict_list]

    '''
    The following loop creates a patient_val_list a list where each
    item in the list represents a subject/patient; each  item is a list
    which contains the p, sd, v. 
    '''
    for patient_row in patients_dict_list:
        patient_val_list =[]
        for patient_val in patient_row.keys():
            if (patient_val[0] != 'p' and patient_val !='C'):
                test_dict[patient_val] = patient_row[patient_val]
                patient_val_list.append(patient_row[patient_val])
        patient_num_val.append(patient_val_list)

    '''
    Using the list of p,sd,v created in the above loop, we then proceed and check
    '''
    for patient in patient_num_val:
        for position in range(len(patient)-3):
            if position % 3 == 0 and patient[position+1] =="*" and patient[position]!='*':
                error_list.append("ERROR: You can't predict a SD without a corresponding prediction in the previous column; " + 'Patient ID: '+ 
                                  patient_list[patient_num_val.index(patient)]+ 
                                  ' Disorder:'+ disorder_dict[str(position)])
            elif position % 3 == 0 and patient[position] =='*' and patient[position+1] !="*":
                error_list.append('ERROR: SD without P, '+ 
                                  'Patient ID: '+ 
                                  patient_list[patient_num_val.index(patient)]+ 
                                  ' Disorder:'+ 
                                  disorder_dict[str(position)])
            elif position % 3 == 0 and patient[position] !='*' and float(patient[position+1]) < 0:
                error_list.append('E: SD must be >=0; '+ 
                                  'Patient ID: '+ 
                                  patient_list[patient_num_val.index(patient)]+ 
                                  ' Disorder:'+ 
                                  disorder_dict[str(position)])



    #Validating Variant Values:
    #Test if for every variant, there is a p value. 

    '''
    The following FOR loop pulls out all the V, P values for each patient row.
    The results are put into a list, each item represents all 
    V,P values for each disorder for each person.
    '''

    patient_pv_list=[]

    for patient_row in patients_dict_list:
        temp_list=[]
        for patient_data in patient_row.keys():
            if patient_data[-1] =='V' or patient_data[-1]=='P':
                temp_list.append(patient_row[patient_data])
        patient_pv_list.append(temp_list)

    '''Then the program goes through the list of the list of P,V values 
    to look for moments when P does not exist, but V exists'''
    for patient_row in patient_pv_list:
        for patient_data in range(len(patient_row)):
            if patient_data % 2 ==0:
                if patient_row[patient_data] =='*' and patient_row[patient_data+1] !='*':
                    error_list.append("ERROR for Patient: " + 
                                      patient_list[patient_pv_list.index(patient_row)] 
                                      + ' for Disorder:'+ disorder_list[patient_data] + 
                                     ' You cannot have V without P.')

    

    '''The next segment of code pulls out all V values for items in the lists of patients (patients_dict_list)'''



    disorder_list = [str(item+1) for item in range(14)]

    variants_list =[] #this will be a list, whose length will = # of rows, one entry for each patient
    for person in patients_dict_list:
        temp_list =[]
        for person_key in person.keys():
            if person_key[-1] =='V': #grab all variant values
                temp_list.append(person[person_key])
        variants_list.append(temp_list)


    '''Now, with the list of variants for each patient (P1-106), 
    we will go through each variant entered, and evaluate whether that variant 
    is legitimate.'''

    #The conditions for each component of the variant data.

    #Standard Format:
    chrom_condition =r"\d+|(xy)+"
    chrom_condition_number =r"\d+"
    pos_condition =r'\d+'
    ref_condition =r'[gcat-]+' 
    alt_condition = r'[gcat\.-]+'

    cpra_format =r'^(\s*\S+:\S+:\S+:\S+\s*,?\s*)+$'

    #Simplified HGVS Format (Added for this Program):
    '''
    This was based on the example of simplified HGVS found in the technical interview question.
    '''
    simp_hgvs_format = r'^(\s*\S+:\S+\s*>\S+)+$'

    #Not Applicable or N/A
    '''
    This should be case-insensitive. 
    '''
    not_app_format= r'[na/]+'

    for patient_variant_data in variants_list:
        for variant_sublist in patient_variant_data:
            sing_variant_sublist = variant_sublist.split(" ")
            for variant in sing_variant_sublist:
                if (re.search(cpra_format, variant)):
                    variant_comp_list = variant.split(':')
                    if (re.search(chrom_condition, variant_comp_list[0], re.I)) ==None:
                        error_list.append ('Chromosome must be XY'+ 'for variant: ' + disorder_list[patient_variant_data.index(variant_sublist)] + variant)
                    if (re.search(chrom_condition_number, variant_comp_list[0], re.I)) and (int(variant_comp_list[0]) >22 or int(variant_comp_list[0]) <0):
                        error_list.append ('Chrom must be <23, for Patient: '+ 
                                           patient_list[variants_list.index(patient_variant_data)]+
                                           ', Disorder: ' + disorder_list[patient_variant_data.index(variant_sublist)]+ 
                                           ', VARIANT '+ variant)
                    if (re.search(pos_condition, variant_comp_list[1])) ==None:
                        error_list.append('Position failure for '+ 'patient:'+ patient_list[variants_list.index(patient_variant_data)], 
                              'disorder:'+ disorder_list[patient_variant_data.index(variant_sublist)]+ ' variant:'+variant)
                    if (re.search(ref_condition, variant_comp_list[2], re.I)) ==None:
                        error_list.append('Ref failure' + 'patient:'+ patient_list[variants_list.index(patient_variant_data)]+ 
                              'disorder: '+ disorder_list[patient_variant_data.index(variant_sublist)] + ' variant:'+variant)
                    if (re.search(alt_condition, variant_comp_list[3], re.I)) ==None:
                        error_list("Alt-failure for patient: " + patient_list[variants_list.index(patient_variant_data)]+ 
                              ' Disorder:'+ disorder_list[patient_variant_data.index(variant_sublist)]+ ' variant:'+ variant)
                elif variant[:3] =='chr':
                    if re.search(simp_hgvs_format,variant, re.I):
                        simp_HGVS_sequence = re.split(r'[\W]+', variant,flags = re.I)
                        #print ('HGVS Simp', patient_list[variants_list.index(patient_variant_data)], simp_HGVS_sequence)

                        if (re.search(r'[gcat-]+',simp_HGVS_sequence[2], re.I) == None):
                            error_list.append('End point must be CATG. Patient: '+patient_list[variants_list.index(patient_variant_data)] + ' Disorder: '
                                              +disorder_list[patient_variant_data.index(variant_sublist)])


                        if (re.search(r'[gcat-]+',simp_HGVS_sequence[1], re.I) == None):
                            error_list.append('Missing CATG. Patient: '+patient_list[variants_list.index(patient_variant_data)] 
                                              + ' Disorder: '
                                              +disorder_list[patient_variant_data.index(variant_sublist)])
                    else:
                         error_list.append('ERROR: Variant NOT in acceptable format, either CHOM:POS:REF:ALT or simplified HGVS or N/A '+ 
                           'for Patient: '+ patient_list[variants_list.index(patient_variant_data)] 
                                      + ', Disorder:' + disorder_list[patient_variant_data.index(variant_sublist)]
                                      + ', Variant: '+ variant)

                elif re.search(not_app_format, variant, re.I):
                    pass

                elif variant =="*":
                    pass
                elif variant !='*': 
                    error_list.append('ERROR: Variant NOT in acceptable format, either CHOM:POS:REF:ALT or simplified HGVS or N/A '+ 
                           'for Patient: '+ patient_list[variants_list.index(patient_variant_data)] 
                                      + ', Disorder:' + disorder_list[patient_variant_data.index(variant_sublist)]
                                      + ', Variant: '+ variant)


#If there are errors. An error log is created (printed in console and put into a txt file)
if len (error_list) >0:
    print('VALIDATION FAILED WITH ERRORS:', '\n')
    for item in error_list:
        print(item)
else:
    #if there are no errors. A .txt file attesting to validation is created. Message also sent to console.
    print("Validation passed with no errors.")
    
    
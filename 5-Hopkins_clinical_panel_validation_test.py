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
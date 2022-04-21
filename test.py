### Reading Large Dataset with 1M+ rows
### Filename = Business_Licenses.csv

##1. Import the library
import time
##2.  Define the filename
name = 'Business_Licenses.csv'

##3. Create the function
def csv_reader(fileName):
    for row in open(fileName, "r"):
        yield row
row = csv_reader(name)
while(True): 
    try: 
        line = next(row)
        print(line)
    except StopIteration:  
        break 
    
    
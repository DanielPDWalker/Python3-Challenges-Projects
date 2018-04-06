import re
import os
from datetime import datetime

### import the txt file - paste info into dump file

inputFile = open(r'input.txt')
#save inputFile "file" type to inputFile to be used later.

content = inputFile.read()
#save the contents of the input file

inputFile.close()
#close the inputFile for reopening in write mode.

inputFile = open(r'input.txt', 'w')
#save dumpFile "file" type to dumpFile to be used later.

inputFile.write('')
#empty the dump file.

inputFile.close()
#save the clearing of the dumpfile and close it

### email regex pattern

emailRegex = re.compile(r'''
            
[a-zA-Z+-.]+      #name part
@                  #@ symbol
[a-zA-Z+-.]+      #domain name part

''', re.VERBOSE)


### save the list of emails

extractedEmail = emailRegex.findall(content)

        
results = '\n'.join(extractedEmail)

### export the formatted list into a txt file in the output folder. >>(APPEND)<<

outputFile = open(r'output.txt', 'a')
outputFile.write('\n\n' + 'Date + Time Run: ' + datetime.now().ctime() + '\n')
outputFile.write('\n' + results)
outputFile.close()


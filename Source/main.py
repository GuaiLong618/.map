# -*- coding: utf-8 -*-
# Filename: IAR for ARM map.py
# PATH: E:\Git_repository

# refer to
import os 
import sys
import time
from __builtin__ import dict
from _ast import Dict

print "fucking high!"
print "author: Jr "

# read file per line
f = open('F:\github\Embedded_Pi\IAR_Project\Debug\List\IAP.map', 'r')
print f
print "\r\n"

# dataDict = {}
# codeDict = {}
dict = {}
lastLine = []
tempList = []
existing = False
temp = False
existing_repeatDictKey = False
while True:
    line = f.readline()
    if len(line) == 0:
        break    # Zero length indicates EOF
    else:
        # Notice comma to avoid automatic newline added by Python
        # \n or ... \n
        if existing == True:
            try:
                index_0x = line.index('0x')
                index_Space = line.index(' ', index_0x, len(line))
                key_0x = line[index_0x+2 : index_Space]
                
                #To determine dict[key] repeat
                if key_0x in dict.keys():
                    existing_repeatDictKey = True
                else:
                    existing_repeatDictKey = False
                
                #To determine two line
                if temp == True:
                    temp = False
                    lastLine = lastLine + line
                    if True == existing_repeatDictKey:
                        tempList = dict[key_0x]
                        tempList = tempList + lastLine
                        dict[key_0x] = tempList
                        #print dict[key_0x]
                    else:
                        dict[key_0x] = lastLine
                else:
                    if True == existing_repeatDictKey:
                        tempList = dict[key_0x] 
                        tempList = tempList + line
                        dict[key_0x] = tempList
                        #print dict[key_0x]
                    else:
                        dict[key_0x] = line

            except ValueError:
                #pass    #can't find 0x
                #existingSpace = (' ') in line
                if (len(line) > 21):   #and (existingSpace == False)
                    temp = True
                    lastLine = line
                    pass
                else:
                    pass
                    #print line
            except:
                f.close() #other error 
            #print line,  #print original .map
        else: 
            existing = ("*** ENTRY LIST") in line
            if existing:
                print "*** ENTRY LIST"
            else:
                pass


print "ARM memory map"
for k,v in sorted(dict.items(), key=lambda d:d[0]):
#     print k,','
    print v, 
    
f.close()






#!/usr/bin/env python

'''
Purpose:       Get key to correspond rows in subset file to main file. Return only results in the main file present
               in the subset file

Usage:         python GetIndividualGenotypes.py ...
 
Author:        et85, etsai@bwh.harvard.edu
'''
####################################################################################
#############################   Function Definitions   #############################
####################################################################################







####################################################################################
################################   Argument Parser   ###############################
####################################################################################








####################################################################################
################################    Main Function    ###############################
####################################################################################

# mainFile = '/Volumes/ppm/biobank/ref/productfiles/MEGA_Consortium_15063755_B1.csv'
mainFile = '/Users/et85/Documents/snp.array/partnersGTC/MEGA_Consortium_15063755_B1.csv'
# mainFile = '/Users/et85/testing/fwdstrand/oct2015/test.csv'
# subsetFile = '/Users/et85/testing/fwdstrand/oct2015/oct2015.snpinfo.txt'
# subsetFile = '/Users/et85/testing/fwdstrand/oct2015/mega_noref_x2954.txt'
subsetFile = '/Users/et85/testing/fwdstrand/oct2015/mega_noref_x293743.txt'

##
# outFile = '/Users/et85/testing/fwdstrand/oct2015/faketriallelic.beadsetid.txt'
outFile = '/Users/et85/testing/fwdstrand/oct2015/test.txt'


mainKeyCol = 2
subsetKeyCol = 1
mainSkipRows = 8
subsetSkipRows = 0
mainValCol = 19
mainDict = {}

mainFH = open(mainFile,'r')
subsetFH = open(subsetFile,'r')
outFH = open(outFile, 'w')

mainData = mainFH.readlines()
mainData = mainData[mainSkipRows:]
for thisEntry in mainData:
    thisEntry = thisEntry.rstrip()
    thisEntryList = thisEntry.split(',')
    if(len(thisEntryList) >= mainValCol):
        mainDict[thisEntryList[(mainKeyCol-1)]] = thisEntryList[(mainValCol-1):mainValCol]
#     if(thisEntryList[2-1] == '1:10002775-GA'):
#         print thisEntryList[(mainKeyCol-1)]
#         print mainDict[thisEntryList[(mainKeyCol-1)]]
#         print mainDict['1:10002775-GA']
#         break
# 1:10002775-GA
    
subsetData = subsetFH.readlines()
subsetData = subsetData[subsetSkipRows:]
for thisEntry in subsetData:
    thisEntry = thisEntry.rstrip()
    thisEntryList = thisEntry.split('\t')
    thisKey = thisEntryList[(subsetKeyCol-1)]
#     print thisKey
#     print mainDict[thisKey]
#     print mainDict[thisKey][0]
     
    outFH.write(thisKey + '\t' + mainDict[thisKey][0] + '\n')


outFH.close()
mainFH.close()
subsetFH.close()
# for key, val in mainDict.items():
#     print key + " : " + ";".join(val)
    










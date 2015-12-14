#!/usr/bin/env python

'''
Purpose:       Have a list of keys that are the only things you want to extract from a larger file

Usage:         python MakeSubsetFileFromKey.py ...
 
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
# mainFile = '/Users/et85/Documents/snp.array/partnersGTC/MEGA_Consortium_15063755_B1.csv'
# mainFile = '/Users/et85/testing/fwdstrand/oct2015/test.csv'
# mainFile = '/Volumes/pcpgm/et85/projects/mega/template/mega.snpinfo.anno.txt'
mainFile = '/Users/et85/testing/fwdstrand/oct2015/nov2015.fixed.snpinfo.txt'

# subsetFile = '/Users/et85/testing/fwdstrand/oct2015/oct2015.snpinfo.txt'
# subsetFile = '/Users/et85/testing/fwdstrand/oct2015/mega_noref_x2954.txt'
subsetFile = '/Volumes/pcpgm/et85/projects/mega/template/biobank_x4931_v1.snpinfo.txt'


# outFile = '/Users/et85/testing/fwdstrand/oct2015/faketriallelic.beadsetid.txt'
# outFile = '/Users/et85/testing/fwdstrand/oct2015/test.txt'
outFile = '/Users/et85/testing/fwdstrand/oct2015/nov2015.fixed.mapped.snpinfo.txt'



mainFile = '/Users/et85/testing/fwdstrand/nov2015/mega_v1b3_x1705969.snpinfo.txt' 
subsetFile = '/Users/et85/testing/fwdstrand/nov2015/biobank_x4931_v2.map'
outFile = '/Users/et85/testing/fwdstrand/nov2015/mega_v1b3_x1548495.snpinfo.txt'


mainKeyCol = 1
subsetKeyCol = 2
mainSkipRows = 0
subsetSkipRows = 0
mainDict = {}

mainFH = open(mainFile,'r')
subsetFH = open(subsetFile,'r')
outFH = open(outFile, 'w')

mainData = mainFH.readlines()
mainData = mainData[mainSkipRows:]
for thisEntry in mainData:
    thisEntry = thisEntry.rstrip()
    thisEntryList = thisEntry.split('\t')
    mainDict[thisEntryList[(mainKeyCol-1)]] = thisEntry
    
subsetData = subsetFH.readlines()
subsetData = subsetData[subsetSkipRows:]
for thisEntry in subsetData:
    thisEntry = thisEntry.rstrip()
    thisEntryList = thisEntry.split('\t')
    thisKey = thisEntryList[(subsetKeyCol-1)]
#     print thisKey
#     print mainDict[thisKey]
#     print mainDict[thisKey][0]
     
    outFH.write(mainDict[thisKey] + '\n')


outFH.close()
mainFH.close()
subsetFH.close()
# for key, val in mainDict.items():
#     print key + " : " + ";".join(val)
    










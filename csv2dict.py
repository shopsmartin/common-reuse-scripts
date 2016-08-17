#!usr/bin/python3
__author__ = 'shopsmartin'

"""written to turn a csv file file of three values into a dictionary where
one row is the key and another row is the list of values. This is specific for
mental.csv"""

import os
import csv
import sys
from pprint import pprint

if sys.version != '3.3.5 (v3.3.5:62cf4e77f785, Mar  9 2014, 01:12:57) \n[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]':
    print('This script requires Python 3.3.5')
else:
    pass


print('Python %s on %s' % (sys.version, sys.platform))


os.chdir()

def main():
    x = csv2dict()
    print(len(x.keys()))
    #pprint(x)
    newcsv(, x)






def csv2dict(filename):
    try:
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            csvdict= {}
            for row in csvreader:
                key = row[2]
                rowlist=[]
                mylist = row[1].split('|')
                for i in mylist:
                    newlist=i.split(' ')
                    for j in newlist:
                        rowlist.append(j)
                csvdict[key]=rowlist
            return csvdict
    except IOError as e:
        print('Error', e)


def newcsv(filename, csvdict):
    with open(filename, 'w', newline='\n') as fh:
        fh.write('abstract,MeSH\n')
        for key in csvdict.keys():
            fh.write(key + ',')
            for j in csvdict.get(key):
                fh.write(j + ' ')
            fh.write('\n')


if __name__ == "__main__": main()

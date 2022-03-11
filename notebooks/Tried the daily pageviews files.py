#!/usr/bin/python
"""
This program receives a bz2 file, and  FAILS TO MAKE IT LEGIBLE!
(it was supposed to output it as a dataframe, but it can't get past the bytearray format)
I'm going back to the hour files I guess.
"""
import pandas as pd
import fileinput 
jawiki = []
count = 0
for line in fileinput.input():
    count += 1
    if line[:3] == 'ja ':
        jawiki.append(line.split(' '))
df = pd.DataFrame(jawiki)
df.to_csv('mydf.csv')

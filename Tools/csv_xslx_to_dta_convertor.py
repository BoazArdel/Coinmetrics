
#csv to dta convertor

import pandas as pd
#df = pd.read_csv('C:/Users/gabriela/Google Drive/Projects/PycharmProjects/coinmetrics/out.csv')
df = pd.read_csv('out.csv')
df.to_stata('15to20.dta')
print("finished converting file")

'''
#excel xslx to dta convertor

import pandas as pd
df = pd.read_excel('10sec.xlsx', index_col=0)
print ("file is loaded")
df.to_stata('15to21cb10sec.dta')
print("finished converting file")


#xslx file merger

fout=open("d:/Files/Google Drive (gabryu@gmail.com)/Projects/PycharmProjects/coinmetrics/out.csv","a")
# first file:
for line in open("d:/Files/Google Drive (gabryu@gmail.com)/Projects/PycharmProjects/coinmetrics/sh1.csv"):
    fout.write(line)
# now the rest:
for num in range(2,5):
    f = open("d:/Files/Google Drive (gabryu@gmail.com)/Projects/PycharmProjects/coinmetrics/sh"+str(num)+".csv")
    next(f) # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()

'''
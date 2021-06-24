#txt json uploader and merger
import os, glob, json

'''
mypath = os. getcwd()
print(mypath)
'''
mypath = "/Users/gabriela/Google Drive/Projects/GitHub/Coinmetrics/Data"

count=0
mydata = [] 
for file in glob.glob(os.path.join(mypath, '*.txt')):
    #print (file)
    with open(file) as json_file:
        mydata = json.load(json_file)
    count = count + 1    
print("numer of opened files is", count)
#print(mydata)
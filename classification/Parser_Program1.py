import csv
import pandas as pd
def createCSV(filename):
    #fileobj = open(filename,encoding='cp850')
    fileobj = open(filename)
    filearr = fileobj.readlines()
    str = []
    newli = 'name'
    newstr = ""
    arr = []
    for line in filearr:
        linearr = line.split()
        for k in linearr:
            if k != 'name':
                arr.append(k)

        if newli in line:
            arr.append('name')
            str.append(arr)
            arr = []

    # print(filearr)
    #if filename=="cleveland.data":
    #    str=str[:282] #in case of cleveland.data, remove useless rows
    #print(str)
    newfilename = filename.replace(".data", ".csv")
    with open(newfilename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(str)


filename = ["cleveland.data","hungarian.data","long-beach-va.data","switzerland.data"]
for ind in range(len(filename)):
    createCSV(filename[ind])
#file1 = open(filename1,encoding = 'cp850')

#print(file1)
#Merging all four files
newfiles = ["cleveland.csv","hungarian.csv","long-beach-va.csv","switzerland.csv"]
#to empty contents of complete_data.csv
complete_filename = 'complete_data.csv'
obj = open(complete_filename,'w')
obj.close()
for ind in range(len(newfiles)):
    temp = pd.read_csv(newfiles[ind],header=None)
    with open(complete_filename, 'a',newline='') as comp_data:
        temp.to_csv(comp_data,header=None)



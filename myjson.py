import json
import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)
with open('/Users/andy/Desktop/items_rs3.json') as data_file:
    data = dict(json.load(data_file))
    i = 0
    iddict = dict()
    while (i < 32765):
        try:
            mydict = (data[str(i)])
            if (str(mydict['tradeable']) == 'False'):
                data.pop(str(i), None)
        except:
            pass
        i+=1
    i = 0
    while (i < 32765):
        try:
            print data[str(i)]
            mydict = (data[str(i)])
            iddict[str(mydict['name'])] = str(i)
            print (i,str(mydict['name']) )
        except:
            pass
        i+=1
with open('dict.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in iddict.items():
        writer.writerow([key, value])

import requests
import pprint
import datetime
import time
import json
import re
import csv
pp = pprint.PrettyPrinter(indent=4)

def getFibb(item, name):
    r = requests.get(url='http://services.runescape.com/m=itemdb_rs/api/graph/'+ item +'.json')
    jsondict = r.json()
    mydict  = jsondict['average']

    todaysprice = mydict[sorted(mydict.keys())[-1]]
    minprice = min(mydict.values())
    maxprice = max(mydict.values())
    diff = (maxprice - minprice)
    fibb1 = int(diff*.382) + minprice
    fibb2 = int(diff*.5) + minprice
    fibb3 = int(diff*.618) + minprice

    todaysprice = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % todaysprice)
    minprice = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % minprice)
    maxprice = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % maxprice)
    diff = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % diff)
    fibb1 = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % fibb1)
    fibb2 = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % fibb2)
    fibb3 = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % fibb3)
    print (name)
    print ("today's price", todaysprice, " 180 day high:", maxprice, "180 day low:", minprice, "diff:", diff)
    print ('fibb .382', fibb1, 'fibb .5', fibb2, 'fibb .618', fibb3)

with open('dict.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        iddict = dict((rows[0],rows[1]) for rows in reader)

for k, v in iddict.iteritems():
    try:
        getFibb(str(iddict[k]), str(k))
    except ValueError:
        pass
'''
#20374 cooking urn
itemid = str(20374)
getFibb(itemid, "Decorated Cooking Urn")

[s for s in my_dict if re.search('^for', s) is not None]
replace for with str(liveinput)
'''

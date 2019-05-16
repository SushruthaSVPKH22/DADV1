import csv
import urllib.request
#from urllib.request import urlopen
from bs4 import BeautifulSoup
from importlib import reload

html = urllib.request.urlopen('http://eciresults.nic.in/statewiseS29.htm?st=S29')
bsobj = BeautifulSoup(html,"lxml")
table = bsobj.findAll("table",border='1')[0]
rows = table.findAll("tr")
csvFile = open("Constituencywise_Telangana.csv",'w')
writer = csv.writer(csvFile)


import sys
reload(sys)
#sys.setdefaultencoding('utf8')

try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
print("Telangana CSV file created successfully")

html = urllib.request.urlopen('http://eciresults.nic.in/statewiseS26.htm?st=S26')
bsobj = BeautifulSoup(html,"lxml")
table = bsobj.findAll("table",border='1')[0]
rows = table.findAll("tr")
csvFile = open("Constituencywise_Chattisgarh.csv",'w')
writer = csv.writer(csvFile)

import sys
reload(sys)
#sys.setdefaultencoding('utf8')

try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
print("Chattisgarh CSV file created successfully")

html = urllib.request.urlopen('http://eciresults.nic.in/statewiseS12.htm?st=S12')
bsobj = BeautifulSoup(html,"lxml")
table = bsobj.findAll("table",border='1')[0]
rows = table.findAll("tr")
csvFile = open("Constituencywise_Madhyapradesh.csv",'w')
writer = csv.writer(csvFile)

import sys
reload(sys)
#sys.setdefaultencoding('utf8')

try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
print("Madhyapradesh CSV file created successfully")


html = urllib.request.urlopen('http://eciresults.nic.in/statewiseS16.htm?st=S16')
bsobj = BeautifulSoup(html,"lxml")
table = bsobj.findAll("table",border='1')[0]
rows = table.findAll("tr")
csvFile = open("Constituencywise_Mizoram.csv",'w')
writer = csv.writer(csvFile)

import sys
reload(sys)
#sys.setdefaultencoding('utf8')

try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

print("Mizoram CSV file created successfully")


html = urllib.request.urlopen('http://eciresults.nic.in/statewiseS20.htm?st=S20')
bsobj = BeautifulSoup(html,"lxml")
table = bsobj.findAll("table",border='1')[0]
rows = table.findAll("tr")
csvFile = open("Constituencywise_Rajasthan.csv",'w')
writer = csv.writer(csvFile)

import sys
reload(sys)
#sys.setdefaultencoding('utf8')

try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

print("Rajasthan CSV file created successfully")

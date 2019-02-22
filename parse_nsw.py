#!/usr/bin/python3

import xml.etree.ElementTree as ET
import lxml
import pandas as pd
import sqlite3


tree = ET.parse('20190215CANT0.xml')
root = tree.getroot()


mylist = ['id', 'number', 'name', 'mediumname', 'stage', 'distance', 'class', 'age', 'grade', 'weightcondition', 'totalprize',
          'first', 'second', 'third', 'fourth', 'fifth', 'time', 'bonustype', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime']

# Works to generate race info
for race in root.iter("race"):
    race_list = []
    for k,v in race.items():
        if k in mylist:
            race_list.append(v)
    # print(race_list)

horse_list = ["number" ,"saddlecloth" "horse" ,"id" ,"blinkers", "trainernumber" ,"jockeynumber" ,"barrier" ,"weight" ,"rating" ,"description" ,"owners", "dob","age", "sex" ,"career","thistrack" ,"thisdistance", "goodtrack" ,"heavytrack" ,"firstup", "secondup", "finished" ,"weightvariation" ,"variedweight", "decimalmargin" ,"penalty" ,"pricestarting" ]
short = ["number" ,"saddlecloth","horse" ,"id" ,"blinkers"]
result = []
my_tuple = ()

# Create a list parser to take in optional lists for predefined analysis or database updating
# Current works as a set list control flow. Next to take in list from a function.
# TODO: convert to a function

for race in root:
    race_id = race.attrib.get('id')
    # print(race_id)
    for nom in race:
        if nom.tag == 'nomination':
            for item in short: #input_list:
                item = nom.attrib.get(item)
                result.append(item)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield tuple(l[i:i + n])

output = (chunks(result,5))
output_list = []
for block in output:
    output_list.append(block)

print(output_list)
# Working
# for race in root:
#     race_id = race.attrib.get('id')
#     # print(race_id)
#     for nom in race:
#         if nom.tag == 'nomination':
#             number = nom.attrib.get('number')
#             horse = nom.attrib.get('horse')
#             id = nom.attrib.get('id')
#             blinkers = nom.attrib.get('blinkers')
#             result.append((race_id, number, horse, id, blinkers))
# print(result)
# print(result)

# creates a tuple of the Meeting an Race ID's
COMBINED_ID_output = []
try:
    for item in mylist:
        for i in range(1, 12):
            my_ids = (int(root.attrib['id']), int(root[i].get(item)))
            COMBINED_ID_output.append(my_ids)
except IndexError:
    pass

COMBINED_ID_output = tuple(COMBINED_ID_output)


connection = sqlite3.connect("test_database.db")
c = connection.cursor()
c.execute("DROP TABLE IF EXISTS Meeting")
c.execute(
    "CREATE TABLE Meeting(PK_Meeting INTEGER PRIMARY KEY AUTOINCREMENT, MeetingID INT, RaceID INT)")
c.executemany(
    "INSERT INTO Meeting(MeetingID, RaceID) VALUES(?,?)", ID_output)
# c.execute("SELECT MeetingID, RaceID from Meeting")
connection.commit()
connection.close()
# for row in c.fetchall():
#     print(row)


# Working
# for race in root.findall('race'):
#     my_tuple = (race.get('id'), race.get("number"),
#                 race.get('shortname'), race.get('class'))
#     race_list.append(my_tuple)
#     race_id = race_list.append(race.get('id'))
#     race_number = race_list.append(race.get("number"))
#     shortname = race_list.append(race.get('shortname'))
#     race_class = race_list.append(race.get('class'))

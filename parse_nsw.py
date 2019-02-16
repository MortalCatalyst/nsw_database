#!/usr/bin/python3

import xml.etree.ElementTree as ET
import pandas as pd
import sqlite3


tree = ET.parse('20190215CANT0.xml')
root = tree.getroot()

# mylist = ['id', 'number', 'nomnumber', 'division', 'name', 'mediumname', 'shortname', 'stage', 'distance', 'minweight', 'raisedweight', 'class', 'age', 'grade', 'weightcondition', 'trophy', 'owner', 'trainer', 'jockey',
#           'strapper', 'totalprize', 'first', 'second', 'third', 'fourth', 'fifth', 'time', 'bonustype', 'nomsfee', 'acceptfee', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime', 'formavailable', 'racebookprize']
mylist = ['id', 'number', 'name', 'mediumname', 'stage', 'distance', 'class', 'age', 'grade', 'weightcondition', 'totalprize',
          'first', 'second', 'third', 'fourth', 'fifth', 'time', 'bonustype', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime']
ID_output = []
try:
    for item in mylist:
        for i in range(1, 12):
            my_ids = (int(root.attrib['id']), int(root[i].get(item)))
            ID_output.append(my_ids)
except IndexError:
    pass

ID_output = tuple(ID_output)

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

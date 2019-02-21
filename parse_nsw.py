#!/usr/bin/python3

import xml.etree.ElementTree as ET
import lxml
import pandas as pd
import sqlite3


tree = ET.parse('20190215CANT0.xml')
root = tree.getroot()


mylist = ['id', 'number', 'name', 'mediumname', 'stage', 'distance', 'class', 'age', 'grade', 'weightcondition', 'totalprize',
          'first', 'second', 'third', 'fourth', 'fifth', 'time', 'bonustype', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime']

# print(ET.tostring(root))
# Works to generate race info
for race in root.iter("race"):
    race_list = []
    for k,v in race.items():
        if k in mylist:
            race_list.append(v)
    # print(race_list)

horse_list = ["number" ,"saddlecloth" "horse" ,"id" ,"blinkers", "trainernumber" ,"jockeynumber" ,"barrier" ,"weight" ,"rating" ,"description" ,"owners", "dob","age", "sex" ,"career","thistrack" ,"thisdistance", "goodtrack" ,"heavytrack" ,"firstup", "secondup", "finished" ,"weightvariation" ,"variedweight", "decimalmargin" ,"penalty" ,"pricestarting" ]

for item in race_list:
    for nom in root.iter("nomination"):
        nom_list = []
        nom_list.append(race_list[0])
        for k, v in nom.items():
            if k in horse_list:
                nom_list.append(v)
        # print(nom_list)
nom_list = []

for item in root.getiterator('race'):
    id_for_nom = item.get('id')
    print(id_for_nom)
    for nom in root.getiterator("nomination"):
        for k, v in nom.items():
            if k in horse_list:
                nom_list.append(v)
    my_output = (id_for_nom, nom_list)
    # print(my_output)
# for elem in root.iter("nomination"):
#     print(elem.text)
# mylist = ['id', 'number', 'nomnumber', 'division', 'name', 'mediumname', 'shortname', 'stage', 'distance', 'minweight', 'raisedweight', 'class', 'age', 'grade', 'weightcondition', 'trophy', 'owner', 'trainer', 'jockey',
#           'strapper', 'totalprize', 'first', 'second', 'third', 'fourth', 'fifth', 'time', 'bonustype', 'nomsfee', 'acceptfee', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime', 'formavailable', 'racebookprize']

RACE_ID_output = []
try:
    for item in mylist:
        for i in range(1, 12):
            my_ids = int(root[i].get(item))
            RACE_ID_output.append(my_ids)
except IndexError:
    pass

RACE_ID_output = tuple(RACE_ID_output)
print(RACE_ID_output)

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


# Collects attributes of the nomination node.
# TODO: Need to insert the race_id into each tuple of nomination detail.
# TODO: Reuse below code with modified horse_list to capture trainer and horse details

# FIXME: At root level in loop. Can take out dict find and get entire horse list.
# FIXME: Tried to hard to get it in a loop when I can create the list of the ids separately.
#FIXME: Then replace the for i in range(1,12) with the list of ids to iterate and then append the item from  that loop, Simples.
        # for k, v in root.items():
        #     if k == 'rail':
        #         print(k + ": " + v)
HORSE_output = []
try:
    for i in range(1, 12):
        for item in horse_list:
            horse_details = []
            print(root[i].attrib)
            my_ids = (race_id, horse_details)
            HORSE_output.append(my_ids)
except IndexError:
    pass

HORSE_output = tuple(HORSE_output)
print(HORSE_output)

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

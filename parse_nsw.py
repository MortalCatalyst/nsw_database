#!/usr/bin/python3

import xml.etree.ElementTree as ET
import lxml
import pandas as pd
import sqlite3


tree = ET.parse('./nsw_database/20190215CANT0.xml')
root = tree.getroot()


mylist = ['id', 'number', 'name', 'mediumname', 'stage', 'distance', 'class', 'age', 'grade', 'weightcondition', 'totalprize',
          'first', 'second', 'third', 'fourth', 'fifth', 'time', 'bonustype', 'trackcondition', 'timingmethod', 'fastesttime', 'sectionaltime']

#################################################################
# analysis lists
#################################################################
horse_list = ["number" ,"saddlecloth" "horse" ,"id" ,"blinkers", "trainernumber" ,"jockeynumber" ,"barrier" ,"weight" ,"rating" ,"description" ,"owners", "dob","age", "sex" ,"career","thistrack" ,"thisdistance", "goodtrack" ,"heavytrack" ,"firstup", "secondup", "finished" ,"weightvariation" ,"variedweight", "decimalmargin" ,"penalty" ,"pricestarting" ]
short = ["number" ,"saddlecloth","horse" ,"id" ,"blinkers"]
result = []
my_tuple = ()


# Works to generate race info
for race in root.iter("race"):
    race_list = []
    for k,v in race.items():
        if k in mylist:
            race_list.append(v)
    # print(race_list)

# Create a list parser to take in optional lists for predefined analysis or database updating
# Current works as a set list control flow. Next to take in list from a function.

def parse_noms(listInput):
    """Function to parse list of different ids """
    for race in root:
        race_id = race.attrib.get('id')
        # print(race_id)
        for nom in race:
            if nom.tag == 'nomination':
                for item in listInput: #input_list:
                    item = nom.attrib.get(item)
                    result.append(item)
    return result

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield tuple(l[i:i + n])

#######################################################################
# Choose your list to parse here with the chunk size as second argument
#######################################################################
output = (chunks(parse_noms(short),5))
output_list = []
for block in output:
    output_list.append(block)

# print(output_list)

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
            my_ids = int(root.attrib['id']), int(root[i].get(item))
            COMBINED_ID_output.append(my_ids)
            # COMBINED_ID_output.append(int(root.attrib['id']))
            # COMBINED_ID_output.append(int(root[i].get(item)))

except IndexError:
    pass

# COMBINED_ID_output = tuple(COMBINED_ID_output)

print(COMBINED_ID_output)
# print(parse_noms(horse_list))
fake_id = ('5153419', '5178566')

def insertRecords(dataList):
    try:
        connection = sqlite3.connect("racing_database.db")
        c = connection.cursor()
        print("Database created and connection successful")
        # create_table = '''CREATE TABLE Event (PK_Meeting INTEGER PRIMARY KEY AUTOINCREMENT, MeetingID INT, RaceID INT);'''
        # c.execute(create_table)
        # connection.commit()
        insert_query = """INSERT INTO Event (MeetingID, RaceID) VALUES(?, ?)"""
        data_tuple = (dataList)
        c.execute(insert_query, data_tuple)
        connection.commit()
        # c.executemany(
        #     "INSERT INTO Meeting(MeetingID, RaceID) VALUES(?,?)", COMBINED_ID_output)
  
        # sqlite_select_query = "select sqlite_version();"
        # c.execute(sqlite_select_query)
        # record = c.fetchall()
        # print("Sqlite version is ", record)
        c.close()
    except sqlite3.Error as error:
        print("Error while connecting ", error)
    finally:
        if (connection):
            connection.close()
            print("The connection is closed")

def giveID(aList):
    for item in aList:
        yield item[0], item[1]
        
for item in giveID(COMBINED_ID_output):
    insertRecords(item)
# print(giveID(COMBINED_ID_output))
    # c.execute("DROP TABLE IF EXISTS Meeting")
    # c.execute(
    #     "CREATE TABLE Meeting(PK_Meeting INTEGER PRIMARY KEY AUTOINCREMENT, MeetingID INT, RaceID INT)")
    # c.executemany(
    #     "INSERT INTO Meeting(MeetingID, RaceID) VALUES(?,?)", COMBINED_ID_output)
    # # c.execute("SELECT MeetingID, RaceID from Meeting")
    # connection.commit()
    # connection.close()




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

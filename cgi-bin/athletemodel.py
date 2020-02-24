#! /usr/local/bin/python3

import pickle
from athletelist import AthleteList
# from athletelist import get_coach_data

# def put_to_store(files_list):
#     all_athletes = {}
#     for each_file in files_list:
#         ath = get_coach_data(each_file)
#         # print(ath)
#         all_athletes[ath.name] = ath
#     try:
#         with open("athletes.pickle", "wb") as athf:
#             pickle.dump(all_athletes, athf)
#     except IOError as ioerr:
#         print("File error(put_to_store): " + str(ioerr))
#     return(all_athletes)
#
# def get_from_store():
#     all_athletes = {}
#     try:
#         with open("athletes.pickle", "rb") as athf:
#             all_athletes = pickle.load(athf)
#     except IOError as ioerr:
#         print("File error(get_from_store): " + str(ioerr))
#     return(all_athletes)

import sqlite3

db_name = 'coachdata.sqlite'

def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)

def get_namesID_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name, id FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)

def get_athlete_from_id(athlete_id):
    # print(athlete_id)
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    resultes = cursor.execute("""SELECT name, dob FROM athletes WHERE id = ?""", (athlete_id, ))
    # print(resultes.fetchone())
    (name, dob) = resultes.fetchone()
    resultes = cursor.execute("""SELECT value FROM timing_data WHERE athlete_id = ?""", (athlete_id, ))
    data = [row[0] for row in resultes.fetchall()]
    response = {
        'Name': name,
        'DOB': dob,
        'data': data,
        'top3': data[0:3]
    }
    connection.close()
    return(response)
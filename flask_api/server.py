import pymysql
from flask import Flask, jsonify
import json
import time
import os #allows import of the .env enviornment files
import itertools


port = os.getenv("port")
#print("port is: "+port)
def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]
            
def RequestInfo(query):
# this takes in a querry form ListOfQuereys and then returns the results in a json format.
    cursor.execute(query) 
    results = json.dumps(dictfetchall(cursor))
    return results
   
def RequestInfoGivenRegion(query,Region):
# this takes in a querry form ListOfQuereys and then returns the results in a json format.
    cursor.execute(query.format('Alameda')) 
    results = json.dumps(dictfetchall(cursor))
    return results

# *****NOTICE******
# Within the Administration tab on the left column of the mysql workbench
# go to users and priveleges and add an account called public
# use standard for the authentification type 
# localhost for the limit to host matching
# Covid_Analysis for the password
# then go to the administrative roles for the public user
# and click DBA for the role
# then apply
db = pymysql.connect(host = "localhost",
                     user = "public",
                     password = "Covid_Analysis",
                     db = "covid" )                 #gives access to script as root can change later
cursor = db.cursor()                                #new cursor command so we dont have to write db.cursor() all the time

query_object = {
    "get_regions":"SELECT id, name FROM region_name;",
    "get_categories":"SELECT name, MAX(confirmed), MAX(deaths), MAX(positive), MAX(suspected), MAX(icu_positive), MAX(icu_suspected) FROM region_name INNER JOIN total_count_confirmed ON region_name.id = total_count_confirmed.region_name_id INNER JOIN total_count_deaths ON region_name.id = total_count_deaths.region_name_id INNER JOIN covid19_positive_patients ON region_name.id = covid19_positive_patients.region_name_id INNER JOIN suspected_covid19_positive_patients ON region_name.id = suspected_covid19_positive_patients.region_name_id INNER JOIN icu_covid19_positive_patients ON region_name.id = icu_covid19_positive_patients.region_name_id INNER JOIN icu_covid19_suspected_patients ON region_name.id = icu_covid19_suspected_patients.region_name_id WHERE name = '{}' GROUP BY name;"
}

# #uncomment below to test
# JsonResults=RequestInfo(query_object["get_regions"])
# print(JsonResults)
#query = "SELECT id, name FROM region_name"          #specific query
#cursor.execute(query)                               # do the query
#Region = cursor.fetchall()                          # get all the results and place it into the tulep Region

app = Flask(__name__)
@app.route('/')                                     #home page
def home():       
     return('hello world') #jsonify(Region)         # return all data as json 

@app.route('/regions',methods=['GET'])
def regions():
    JsonResults=RequestInfo(query_object["get_regions"])
    return(JsonResults)

@app.route('/<string:Region>', methods=['GET'])
def get_Region(Region):
    data=RequestInfoGivenRegion(query_object["get_categories"], Region)
    return (data)         

@app.route('/about') # about page
def about():
    return 'The About Page'

@app.route('/time')
def get_current_time():
    return {'time': time.ctime()}

@app.route('/egg')
def egg():
    return('three fucking monkeys-by deaf')

if __name__=='__main__':
    app.run()
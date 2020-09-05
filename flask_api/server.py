import pymysql
from flask import Flask, jsonify, request
import json
import time
import os #allows import of the .env enviornment files
import itertools
from datetime import date, datetime


port = os.getenv("port")
#print("port is: "+port)
def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall()]

# for serializing things to json
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


def RequestInfo(query):
# this takes in a querry form ListOfQuereys and then returns the results in a json format.
    resultObj = {}
    cursor.execute(query.format(rTable=regionTable)) 
    rowList =dictfetchall(cursor)
    for rowObj in rowList:
        for col in rowObj:
            if col in resultObj:
                resultObj[col].append(rowObj[col])
            else:
                resultObj[col]=[]
    return json.dumps(resultObj)
   
def RequestInfoGivenRegion(query,Region):
# this takes in a querry form ListOfQuereys and then returns the results in a json format.
    resultsList = []
    resultObj = {}
    for i in range(len(colList)):
        newQuery= query.format(region =Region,col=colList[i],table=tableList[i],rTable=regionTable)
        cursor.execute(newQuery) 
        resultRows = dictfetchall(cursor)
        if len(resultRows)!=0:
            resultObj[colList[i]]={
                "Min":resultRows[0]["Min"],
                "Max":resultRows[0]["Max"]
            }
        
    return json.dumps(resultObj)

def RequestDataGivenFilters(Filters):
# this takes in a querry form ListOfQuereys and then returns the results in a json format.
    resultsList = []
    resultObj = {}
    print("FilterObj: "+str(Filters))
    for i in range(len(colList)):
        newQuery= query_object["get_data"].format(value=colList[i],table=tableList[i],rTable=regionTable)
        where = ""
        #print("Query: "+newQuery)
        where = query_object["get_data_region_where"].format(name=Filters["name"],rTable=regionTable)
        newQuery = " ".join([newQuery,where])

        # use the where statement if given a filter
        if Filters and colList[i] in Filters:
            where = query_object["get_data_where"].format(value=colList[i],max=Filters[colList[i]]["Max"],min=Filters[colList[i]]["Min"])
            newQuery = " ".join([newQuery,where])
        
        print("Query: "+newQuery)
        cursor.execute(newQuery) 
        resultRows = dictfetchall(cursor)
        #print("Resultrows: "+str(resultRows))
        print("Resulting "+colList[i]+" len: "+ str(len(resultRows)))
        if len(resultRows)!=0:
            if "filteredData" not in resultObj:
                resultObj["filteredData"]={}
            resultObj["filteredData"][colList[i]]=resultRows

    resultObj["filters"]=Filters
    return json.dumps(resultObj,default=json_serial)
# *****NOTICE******
# Within the Administration tab on the left column of the mysql workbench
# go to users and priveleges and add an account called public
# use standard for the authentification type 
# localhost for the limit to host matching
# Covid_Analysis for the password
# then go to the administrative roles for the public user
# and click DBA for the role
# then apply
db = pymysql.connect(host = "covid-project.cni5jxwbesmd.us-west-1.rds.amazonaws.com",
                    port=3308,
                     user = "public",
                     password = "passypass",
                     db = "covid",
                     connect_timeout = 60
                      )                   #gives access to script as root can change later
cursor = db.cursor()                                #new cursor command so we dont have to write db.cursor() all the time
regionTable="region_name"
colList = ["confirmed","deaths","positive", "suspected","icu_positive", "icu_suspected"]
tableList =["total_count_confirmed","total_count_deaths","covid19_positive_patients","suspected_covid19_positive_patients","icu_covid19_positive_patients","icu_covid19_suspected_patients"]

query_object = {
    "get_regions":"SELECT name FROM {rTable};",
    "get_category":"SELECT MAX({col}) as 'Max', MIN({col}) as 'Min' FROM {rTable} INNER JOIN {table} ON {rTable}.id = {table}.{rTable}_id  WHERE name = '{region}' GROUP BY name;",
    "get_data":"select {table}.{value}, {table}.{value}_date from {rTable} INNER JOIN {table} on {rTable}.id={table}.{rTable}_id",
    "get_data_region_where":"where {rTable}.name='{name}'",
    "get_data_where":"and {value} >= {min} and {value} <= {max}",
    "limit": "Limit {value}"
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

@app.route('/regions:<string:Region>', methods=['GET'])
def get_Region(Region):
    data=RequestInfoGivenRegion(query_object["get_category"], Region)
    return (data)         
@app.route('/regionData', methods=['POST'])
def get_RegionData():
    #print(request.data)
    filterData = request.get_json()
    data=RequestDataGivenFilters(filterData)
    return  (data)

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
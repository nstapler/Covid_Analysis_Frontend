import pymysql
from flask import Flask, jsonify
import json
import time
import os #allows import of the .env enviornment files
app = Flask(__name__)

port = os.getenv("port")
#print("port is: "+port)

db = pymysql.connect(host = "localhost",
                     user = "root",
                     password = "Covid_Analysis",
                     db = "covid" )                 #gives access to script as root can change later
cursor = db.cursor()                                #new cursor command so we dont have to write db.cursor() all the time

query = "SELECT id, name FROM region_name"          #specific query
cursor.execute(query)                               # do the query
Region = cursor.fetchall()                          # get all the results and place it into the tulep Region


@app.route('/')                                     #home page
def home():       
     return jsonify(Region)                         # return all data as json 

@app.route('/<int:Region_id>', methods=['GET'])
def get_Region(Region_id):
    if 0<Region_id<=len(Region):                    # if region id matches range then give specific json object
        return jsonify(Region[Region_id-1])         #return specific json object starting from 1
    else:                                           #otherwise retun 404 for error
        return ('404')
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
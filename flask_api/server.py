from flask import Flask
import time
import os #allows import of the .env enviornment files
app = Flask(__name__)

port = os.getenv("port")
print("port is: "+port)
@app.route('/') #home page
def home():       
    return 'Hello World'

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
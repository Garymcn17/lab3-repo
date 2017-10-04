
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10091997'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.217.169'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add/<username>/<email>")
def add(username , email) :
	cur = mysql.connection.cursor()
	cur.execute('''INSERT INTO students (studentName, email) values ('%s','%s'")''' % (username,email))
	cur.execute('commit;')
	return 'Added new student x'

@app.route("/update")
def update() :
        cur = mysql.connection.cursor()
        cur.execute('''UPDATE students SET studentName = "Gary" WHERE studentName LIKE "Another one x"''')
        cur.execute('commit;')
        return 'Updated student x'

@app.route("/delete")
def delete() :
        cur = mysql.connection.cursor()
        cur.execute('''DELETE FROM students WHERE studentName LIKE "Gary"''')
        cur.execute('commit;')
        return 'Student Deleted'

@app.route("/help")
def help() :
	
	return app.send_static_file('index.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000


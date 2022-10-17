from flask import Flask, redirect,render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'flaskdb.chxoadgv4baq.ap-northeast-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'flaskdb123'
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

def getTextFromDb():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT text FROM testtable WHERE id = 1''')
    newText =  cursor.fetchone()
    cursor.close()
    return newText

@app.route('/admin/', methods = ['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        text = request.form['text']
        cursor = mysql.connection.cursor()
        cursor.execute(''' UPDATE testtable SET text = %s WHERE id = 1''',[text])
        mysql.connection.commit()
        newText = getTextFromDb()
        cursor.close()
        return redirect(url_for('admin'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    newText = getTextFromDb()
    return newText[0]
 
app.run()

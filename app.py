from flask import Flask, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': 'password',
    'database': 'mydatabase'
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # Add authentication logic here
    return redirect(url_for('index'))

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


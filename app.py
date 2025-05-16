from flask import Flask, render_template, jsonify
from configs.db import db, cursor  # ✅ Corrected import path

from backend.pst import signup_bp;

app = Flask(__name__)

app.register_blueprint(signup_bp)

# Sample Data
Data = [ 
    {
        'name': "Gaurav",
        'Age': 22,
        'Current-status': 'Pursuing B.Tech',
        'Address': 'LAx'
    },
    {
        'name': "Saurav",
        'Age': 18,
        'Current-status': 'Pursuing NEET',
        'Address': 'Laxmipur Naya'
    },
    {
        'name': "Sachin",
        'Age': 16,
        'Current-status': 'Intermediate',
        'Address': 'Laxmipur Naya Tola Siwan'
    },
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home2():
    return render_template('home2.html', Data=Data)

@app.route('/json')
def jsonData():
    return jsonify(Data)

# Example route using the database
@app.route('/dbtest')
def dbtest():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

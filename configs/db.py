import mysql.connector

# Create and export db and cursor
db = mysql.connector.connect(
    host="localhost",
    user="flaskuser",
    password="Gk022135@",
    database="flask_app"
)

cursor = db.cursor()

from flask import Flask, render_template

app = Flask(__name__)

Data = [ 
    {
        'name' : "Gaurav",
        'Age' : 22,
        'Current-status' : 'Persuing B.Tech',
        'Address' : 'LAx'
    },
    {
        'name' : "Saurav",
        'Age' : 18,
        'Current-status' : 'Persuing NEET',
        'Address' : 'Laxmipur Naya'
    },
    {
        'name' : "Sachin",
        'Age' : 16,
        'Current-status' : 'Intermediate',
        'Address' : 'Laxmipur Naya Tola Siwan'
    },
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home2():
    return render_template('home2.html', Data = Data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

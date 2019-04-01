from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>Welcome to Communal Table!</h1>
            <nav><ul><li><a href="/meals.html">Meals</a></li><li><a href="/host.html">Host</a></li></ul></nav>'''

@app.route('/meals.html')
def meals():
    mealsList = []
    conn = sqlite3.connect('communaltable.db')
    cur = conn.cursor()
    queryAllMeals = '''SELECT * FROM events'''
    cur.execute(queryAllMeals)
    for row in cur:
        mealDict = {}
        mealDict["description"] = row[12]
        mealDict["address1"] = row[1]
        mealDict["zipcode"] = row[5]
        mealsList.append(mealDict)
    conn.close()
    hostList = ['Bob', 'Bri']
    return render_template('meals.html',title="Meals Around", meals = mealsList)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

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
    hostList = []
    userIDList = []
    conn = sqlite3.connect('communaltable.db')
    cur = conn.cursor()
    queryAllMeals = '''SELECT * FROM events'''
    cur.execute(queryAllMeals)
    for row in cur:
        print(row)
        mealDict = {}
        mealDict["description"] = row[12]
        mealDict["address1"] = row[1]
        mealDict["zipcode"] = row[5]
        mealDict["seats"] = row[19]
        userID = row[18]
        mealDict['host_id'] = userID
        userIDList.append(userID)
        mealsList.append(mealDict)
    for i in userIDList:
        queryHost = "SELECT firstname, lastname FROM users WHERE users_id =" + str(i)
        cur.execute(queryHost)
        for row in cur:
            fullname = row[0] + " " + row[1]
            hostList.append(fullname)
    index = 0
    for meal in mealsList:
        meal['host'] = hostList[index]
        index = index+1

    conn.close()
    return render_template('meals.html',title="Meals Around", meals = mealsList)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

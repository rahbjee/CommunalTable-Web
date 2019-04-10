from flask import Flask, render_template,request
import sqlite3
from wtforms import Form, SubmitField, IntegerField, HiddenField, validators
app = Flask(__name__)

class RSVPForm(Form):
    rsvpNumber = IntegerField('# Attending', [validators.NumberRange(0,100,'invalid input for rsvp')])
    rsvpMealID = HiddenField()
    rsvpSubmit = SubmitField('RSVP')


@app.route('/')
def index():
    return '''<h1>Welcome to Communal Table!</h1>
            <nav><ul><li><a href="/meals.html">Meals</a></li><li><a href="/host.html">Host</a></li></ul></nav>'''

@app.route('/meals.html', methods = ['GET', 'POST'])
def meals():
    rsvpform = RSVPForm()
    mealsList = []
    hostList = []
    userIDList = []
    conn = sqlite3.connect('communaltable.db')
    cur = conn.cursor()
    queryAllMeals = '''SELECT * FROM events'''
    cur.execute(queryAllMeals)
    for row in cur:
        mealDict = {}
        mealDict["meal_id"] = row[0]
        mealDict["description"] = row[12]
        mealDict["address1"] = row[1]
        mealDict["zipcode"] = row[5]
        mealDict["seats"] = row[19]
        time = row[20]
        print(time)
        y = time[0:4]
        m = time[5:7]
        d = time[8:10]
        t = time[11:16]
        t_formatted = t+" on " +m+"/"+d+'/'+y
        mealDict['time'] = t_formatted
        userID = row[18]
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
    if request.method == "POST" and rsvpform.validate():
        rsvp_num = request.form.get('rsvpNumber')
        rsvp_meal = request.form.get('rsvpMealID')
        querySeats = "SELECT seats FROM events WHERE events_id =" + rsvp_meal
        cur.execute(querySeats)
        for seat in cur:
            mealCap = seat[0]
        if int(rsvp_num) > mealCap:
            message = "Error!"
            print(message)
        else:
            queryRSVP = "UPDATE events SET seats = " + str(mealCap-int(rsvp_num))+ " WHERE events_id = " + rsvp_meal
            cur.execute(queryRSVP)
            conn.commit()
    conn.close()
    return render_template('meals.html',title="Meals Around", meals = mealsList, form = rsvpform)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

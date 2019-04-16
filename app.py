from flask import Flask, render_template, request, url_for
import sqlite3
from wtforms import Form, SubmitField, IntegerField, HiddenField, validators
app = Flask(__name__)

class RSVPForm(Form):
    rsvpNumber = IntegerField('# Attending', [validators.NumberRange(1,100,message='invalid input for rsvp'), validators.Optional()])
    rsvpMealID = HiddenField()
    rsvpSubmit = SubmitField('RSVP')



@app.route('/', methods = ["GET", "POST"])
def index():
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
        mealDict["name"] = row[21]
        time = row[20]
        mealDict['date'] = time[0:10]
        mealDict['time'] = time[11:16]
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
    if request.method == "POST":
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
    return render_template('index.html', meals = mealsList)

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
        mealDict["name"] = row[21]
        time = row[20]
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

@app.route('/newevent.html', methods = ["GET", "POST"])

def newevent():
    if request.method == "POST":
        conn = sqlite3.connect('communaltable.db')
        cur = conn.cursor()
        neweventName = request.form.get('eventName')
        neweventDes = request.form.get('eventDes')
        neweventDate = request.form.get('date')
        neweventTime = request.form.get('time')
        neweventMealTime = neweventDate + " " + neweventTime
        neweventAddr = request.form.get('addr')
        neweventAddr2 = request.form.get('addr2')
        neweventCity= request.form.get('city')
        neweventState = request.form.get('state')
        neweventZip = request.form.get('zip')
        neweventCap = request.form.get('seat')
        queryState = "SELECT state_id FROM state WHERE name "
        queryAddEvent = "INSERT INTO events (address1, address2, zipcode, description, seats, user_id, mealTime,  name) VALUES ('"+ str(neweventAddr) + "','" + str(neweventAddr2) + "'," + str(neweventZip) + ", '"+ str(neweventDes) + "',"+ str(neweventCap) + ",1,'" + str(neweventMealTime) + "','" + str(neweventName) +"');"
        print(queryAddEvent)
        cur.execute(queryAddEvent)
        conn.commit()
        queryCity = "SELECT city_id FROM city WHERE name = '" + str(neweventCity) + "'"
        cur.execute(queryCity)
        for row in cur:
            city_id = row[0]
            queryCityUpdate = "UPDATE events SET city = " + str(city_id) + " WHERE name = '" + str(neweventName) +"'"
            cur.execute(queryCityUpdate)
            conn.commit()
        conn.close()
    return render_template('newevent.html',title="New Event Form")

@app.route('/host.html')
def host():
    render_template('host.html')

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

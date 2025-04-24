from flask import Flask

app = Flask(__name__)

@app.route('/event-list')
def event_list():
    return [{'name' : 'Motor bilke event', 'startDate' : '01/01/2025', 'endDate' : '05/01/2025'}]

@app.route('/create-event')
def create_event():
    return 'event created'

@app.route('/update-event')
def update_event():
    return 'event updated'

@app.route('/delete-event')
def delete_event():
    return 'delete event'

@app.route('/user-login')
def user_login():
    return 'user logged in'

@app.route('/user-signup')
def user_signup():
    return 'user signup'

@app.route('/user-logout')
def user_logout():
    return 'user logout'



if __name__ == '__main__':
    app.run()

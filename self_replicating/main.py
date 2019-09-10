from flask import Flask, url_for, escape, render_template, request, session
import configparser
import requests as requests_client
import json

app = Flask(__name__)
app.secret_key = 'doesn\'t matter if this is secret'

cfparser = configparser.ConfigParser()
cfparser.read('secrets.ini')
client_ID = cfparser['GITHUB']['client_ID']
client_Secret = cfparser['GITHUB']['client_Secret']

"""
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/username', methods = ['GET', 'POST'])
def username():
    if request.method == 'POST':
        print(str(request.form))
        username = request.form['username']
        return str(request.form['username'])
    else:
        return "Please input a valid username"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
"""

@app.route('/')
def github_auth():
    return render_template('github_auth.html', client_ID = client_ID)

@app.route('/callback', methods = ['GET', 'POST'])
def callback():
    if request.method == 'POST':
        print(str(request.form))
        return str(request.form)
    else:
        print(str(request.args))
        code = request.args['code']
        r = requests_client.post('https://github.com/login/oauth/access_token',
                                 data = {
                                    'client_id': client_ID,
                                    'client_secret': client_Secret,
                                    'code': code,
                                    'accept': 'json'
                                 })
        r = r.text
        r = r.split('&')
        r_dict = {}
        for form_attrib in r:
            split = form_attrib.split('=')
            r_dict[split[0]] = split[1]
        access_token = r_dict['access_token']
        session['access_token'] = access_token
        return render_template('ready_to_fork.html')

@app.route('/copy')
def copy():
    if 'access_token' in session:
        r = requests_client.post('https://api.github.com/repos/octocat/Hello-World/forks',
                             params = {
                                 'access_token': session['access_token']
                             })
        print(r.status_code)
        if int(r.status_code) <= 202:
            jsoned_r = json.loads(r.text)
            html_url = jsoned_r['html_url']
            return render_template('succesful_fork.html', html_url = html_url)
        else:
            print("need to redirect")
            return "need to redirect"
    else:
        print("need to redirect")
        return "need to redirect"
        #github_auth()

@app.route('/failure')
def failure_redirect():
    return "click here to go to the start"


#with app.app_context(), app.test_request_context():
#    url = url_for('static', filename = 'welcome.html')
#    print(url)
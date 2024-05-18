from flask import Flask, render_template
from flask import request
from flask_bootstrap5 import Bootstrap
import simplejson as json
import requests
import random
import variables

apikey = variables.apikey

header = {
    'Authorization' : "Key {}".format(apikey)
}


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/payment/approve', methods=['POST'])
def approve():
    # Build the header for user authentication
    accessToken = request.form.get('accessToken')
    userheader = {
        'Authorization' : f"Bearer {accessToken}"
    }
    paymentId = request.form.get('paymentId')
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/approve"
    response = requests.post(approveurl, headers = header)
    userurl = "https://api.minepi.com/v2/me"
    userresponse = requests.get(userurl, headers = userheader)
    userjson = json.loads(userresponse.text)
    return(response.text)

@app.route('/payment/complete', methods=['POST'])
def complete():   
    # Build the header for user authentication
    accessToken = request.form.get('accessToken')
    userheader = {
        'Authorization' : f"Bearer {accessToken}"
    }
    paymentId = request.form.get('paymentId')
    txid = request.form.get('txid')
    userurl = "https://api.minepi.com/v2/me"
    userresponse = requests.get(userurl, headers = userheader)
    data = {'txid': txid}
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/complete"
    response = requests.post(approveurl, headers = header, data = data)
    return(response.text)

@app.route('/payment/cancel', methods=['POST'])
def cancel():    
    paymentId = request.form.get('paymentId')
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/cancel"
    response = requests.post(approveurl, headers = header)
    return(response.text)

@app.route('/payment/error', methods=['POST'])
def error():    
    paymentId = request.form.get('paymentId')
    approveurl = f"https://api.minepi.com/v2/payments/{paymentId}/cancel"
    response = requests.post(approveurl, headers = header)
    return(response.text)

@app.route('/me', methods=['POST'])
def getme():
    userurl = "https://api.minepi.com/v2/me"
    response = requests.post(userurl, headers = header)
    return(response.text)

@app.route('/save_email', methods=['POST'])
def save_email():
    email = request.form.get('email')
    if email:
        with open('emails.txt', 'a') as f:
            f.write(email + '\n')
        return 'Email saved successfully!', 200
    return 'Email not provided!', 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

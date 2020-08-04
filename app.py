from flask import Flask, render_template, url_for, request ,redirect
from markupsafe import escape
import csv
from emailsender import send_emails
app = Flask(__name__)

@app.route('/<string:page_name>')
def web_url(page_name):
	return render_template(page_name)
@app.route('/')
def redirect_to_home( ):
	return redirect('/index.html')

@app.route('/submit_data',methods=['POST'])
def submit_data():
	data = request.form.to_dict()
	print(data)
	if data['first-name'] == '' or data['last-name'] == '' or data['email'] == '':
		return redirect('/tryagain.html')
	else:
		with open('database.csv','a') as csv_file:
			csv_reader = csv.writer(csv_file)
			csv_reader.writerow([data['first-name'],data['email']])

	return redirect('/successful.html')


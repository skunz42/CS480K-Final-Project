from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def generate_result():
	city_name = request.form['city_name']
	state_abrv = request.form['state_abrv']
	print(city_name)
	print(state_abrv)
	#ToDo: Send "city_name" and "state_abrv" to function here
	return render_template('result.html')


#Not working as intented --> favicon received but not displayed
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
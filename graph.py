from flask import Flask,render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import prettyplotlib as prettyplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
import MySQLdb
app = Flask(__name__)

@app.route('/')
def home():
	
	db = MySQLdb.connect(host='127.0.0.1', user='root',passwd='@romeo123', db='guado')
	cur = db.cursor()
	cur.execute('SELECT  ( SELECT COUNT(*)FROM gd_sms_incoming) AS total_incoming_sms,( SELECT COUNT(*)FROM gd_sms_outgoing) AS total_outgoing_sms;')
	result = cur.fetchone()
	result=list(result)
	#print(result)

	objects = ('incoming','outgoing')
	y_pos = np.arange(len(objects))
	performance = result[0:]
 
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Total')
	plt.title('Total Incoming and Outgoing Messages')
 
	plt.show()


	return render_template("home.html")
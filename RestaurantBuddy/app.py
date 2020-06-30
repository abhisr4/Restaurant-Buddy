from flask import *
import pandas as pd
import numpy as np
from findLocation import scrapper,findKNearestNeighbor


#__name__==__main__
app=Flask(__name__)

@app.route('/')
def homePage():
	return  render_template("index.html")
@app.route('/home')
def returnHome():
	return redirect('/')

@app.route('/submit',methods=['POST'])
def submitData():
	if request.method=='POST':
		address=request.form['inputAddress'] #got the input from the user
		#main process logic
		x,y=scrapper(address)
		nearestNeighbor=findKNearestNeighbor([[x,y]])
		return render_template("index.html",yourAddress=nearestNeighbor)

if __name__=="__main__":
	app.run(debug=True)
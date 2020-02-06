# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def landing():
	return render_template('landing.html')


if __name__ == '__main__':
	print("Starting webapp...")
	app.run(debug=True)

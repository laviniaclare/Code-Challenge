# -*- coding: utf-8 -*-
from app_settings import app, db
from flask import render_template


@app.route('/')
def landing():
	return render_template('landing.html')


if __name__ == '__main__':
	print("Starting webapp...")
	app.run(debug=True)

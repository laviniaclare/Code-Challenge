# Take Home

This is the beginnings of an app that would allow a person to search for a room to rent.

## Getting Started

To run locally, first clone or fork this repo. Ideally you should set up a virtual environment with
Python 3 to run this in. You can find instructions for setting that up here: https://docs.python.org/3/tutorial/venv.html


### Prerequisites

The required packages are listed in requirements.txt. You can install them by running (make sure your virtual environment is activate first if you are using one):

```
pip install -r requirements.txt
```

### What this code does
This repo contains the basic set up for a flask app and a script to seed the squlite3 database with appartment data from the given CSV. Basic data models for appartments and hosts are defined in models.py. There is a single route definited in the routes.py file.


### What is left to do
* An endpoint should be created that can search the database for appartments
* In order to allow searches by distance it might be useful to use a mapping API of some sort
* A simple ui should be created to allow easier search
* Tests should be writted for all parts of the code


### How to run the code

You can seed the database by running the following in your terminal:
```
python seed.py
```

The app can be run with the following terminal command:
```
python routes.py
```
When the app is running you can visit http://127.0.0.1:5000/ in your browser. You should see a mostly empty page that says "Welcome". Once the search and ui is implemented this page should contain a simple form for searching for appartments.

Since the one existing route doesn't touch the database it doesn't matter which order you run them in, but if the search were implemnted you would need to run seed.py as part of your initial set up.

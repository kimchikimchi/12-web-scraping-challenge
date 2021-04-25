# Import libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo

import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="...")

# Routes

# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route('/')
def index():
    pass

# Create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
@app.route('/scrape')
def scrape():
    pass
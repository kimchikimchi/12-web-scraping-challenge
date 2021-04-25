# Import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
mars  = mongo.db.mars

# Drop collection if available to remove dups
mars.drop()

# Routes

# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route('/')
def index():
    mars_data = mars.find()
    # return render_template("index.html", mars_data=mars_data)
    return render_template("index.html")

# Create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
@app.route('/scrape')
def scrape():
    # Collect data from websites
    data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars.update({}, data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
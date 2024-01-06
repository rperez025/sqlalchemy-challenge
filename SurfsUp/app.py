# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
app = Flask(__name__)

# home route
@app.route("/")
def home():
    return("Welcome to the Hawaii Climate Analysis Local API!")

if __name__ == '__main__':
    app.run()

# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################

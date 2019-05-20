"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request, redirect, url_for, render_template
from pymongo import MongoClient
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import logging
import os

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.brevetsdb

###
# Pages
###
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('calc.html'), 200

@app.route("/<filepath>")
def found(filepath):
    if ((".." in filepath) or ("//" in filepath) or ("~" in filepath)):
        return render_template('403.html'), 403
    if os.path.isfile("templates/" + filepath):
        return render_template(filepath), 200
    else:
        return render_template('404.html'), 404

@app.route("/display")
def display():
    app.logger.debug("Display page entry")
    _times = db.brevetsdb.find()
    times = [time for time in _times]
    return render_template('display.html', times=times), 200

###
# AJAX request handlers
###
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    date = request.args.get('dt', type=str)
    brev = request.args.get('bv', type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, brev, date)
    close_time = acp_times.close_time(km, brev, date)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/_submit")
def submit():
    app.logger.debug("Got a JSON request")
    distance = request.args.get("d")
    name = request.args.get("n")
    openTime = request.args.get("o")
    closeTime = request.args.get("c")
    time_doc = {
        'dist': distance,
        'name': name,
        'open': openTime,
        'close':closeTime
    }
    app.logger.debug("Inserting...")
    db.brevetsdb.insert_one(time_doc)
    app.logger.debug("success")
    return flask.jsonify()
    
###
# Error Handlers
###
@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden_request(error):
    app.logger.debug("Forbidden request")
    flask.session['linkback'] = flask.url_for("index")
    return render_template('403.html'), 403

###############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(debug=True, port=CONFIG.PORT, host="0.0.0.0")

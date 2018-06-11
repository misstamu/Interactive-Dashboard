# import necessary libraries
import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

## read in csv files
bbdsamples = pd.read_csv("belly_button_biodiversity_samples.csv")
bbdotu = pd.read_csv("belly_button_biodiversity_otu_id.csv")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def sample():
    bbdnames = pd.DataFrame(bbdsamples.columns[1:154])
    #print(bbdnames)
    return jsonify(bbdnames)    

@app.route("/otu")
def description():
    otud = pd.DataFrame(bbdotu['lowest_taxonomic_unit_found'])
    #print(otud)
    return jsonify(otud) 

@app.route("/metadata/sample")
def sampledata():
    results = db.session.query(samples_metadata).filter(samples_metadata.sampleid=='input')
    for result in results.all()
    sd = pd.DataFrame(result.age, result.bbtype, result.ethnic, result.gender, result.loccation, result.sampleid)
    return jsonify(sd)

 
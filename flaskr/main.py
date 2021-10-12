"""Main module with flask blueprints for routes"""


import pandas as pd
from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify
from flaskr.graphics import graph_bar, graph_heat, graph_scat
from flaskr import db
from sqlalchemy import select
from .models import Insurance


main = Blueprint('main', __name__)

#Read tables from csv files.
data = pd.read_csv(
    '/home/Farwander/mysite/graphics/flaskr/static/flight_delays.csv',
    index_col='Month')

#The following data is in sql database also.
#Current version is using sql query to get this data.
#data_2 = pd.read_csv('/home/Farwander/mysite/graphics/flaskr/static/insurance.csv')

@main.route('/')
def index():
    """Route for main page"""
    return render_template('index.html')

@main.route('/pyt')
def pyt():
    """Route for page with graphics made using sns in real time"""

    table = [data.columns.values.tolist()]+data.values.tolist()

    #List of column names.
    names = list(data.columns)

    #Default column.
    column = 'NK'

    #Dictionary of the sns objects for barplot, heatplot and scatterplot.
    picture = {}
    picture['bar'] = graph_bar(data, column)
    picture['heat'] = graph_heat(data)

    #Query table.
    s = Insurance.query.order_by(Insurance.id)

    #Get the list of column names.
    column_lst = Insurance.__table__.columns.keys()

    #Comprehend a dict in a form column_name:column.
    dict = {name:[getattr(i, name) for i in s.all()] for name in column_lst}

    #Transform dict to pandas dataframe.
    data_2 = pd.DataFrame.from_dict(dict)

    #Finally append a scatterplot to the dictionary.
    picture['scat'] = graph_scat(data_2, 'bmi', 'charges', 'smoker')

    return render_template(
        'sns.html', picture=picture,
        column=column, names=names, table=table)

@main.route('/r')
def r():
    """Route for graphics made in R"""
    return render_template('r.html')

@main.route('/getbar')
def bar():
    """Route for json response"""

    #Get column.
    col = request.args.get('col', 0)

    #If column not empty then call a graph_bar to draw barplot for this column.
    if col != 0:
        b = graph_bar(data, col)
    else:
        b = 0

    #Return jsonified response.
    resp = {'picture': b}
    return jsonify(resp)

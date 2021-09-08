from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify
from flaskr.graphics import graph_bar, graph_heat, graph_scat
from flaskr import db
from .models import Insurance
import pandas as pd

"""main module with flask blueprints for routes"""

main = Blueprint('main', __name__)

#read tables from csv files
data = pd.read_csv('/home/Farwander/mysite/graphics/flaskr/static/flight_delays.csv',index_col='Month')
#data_2 = pd.read_csv('flaskr/static/insurance.csv')

#main page route
@main.route('/')
def index():
    return render_template('index.html')

#route for page with graphics made right here
@main.route('/pyt')
def pyt():
    #pandas to list
    table = [data.columns.values.tolist()]+data.values.tolist()
    #list of column names
    names = list(data.columns)
    #default column
    column = 'NK'
    #dictionary of the sns objects for barplot, heatplot and scatterplot
    picture = {}
    picture['bar'] = graph_bar(data, column)
    picture['heat'] = graph_heat(data)
    #picture['scat'] = graph_scat(data_2,'bmi','charges','smoker')
    #query table
    s = db.session.query(Insurance)
    column_lst = [i['name'] for i in s.column_descriptions]
    query_dict = {name:[j.name for j in s] for name in column_lst}
    data_2 = pd.DataFrame.from_dict(query_dict)
    #data_2 = pd.DataFrame.from_records(s.all())
    picture['scat'] = graph_scat(data_2,'bmi','charges','smoker')
    return render_template('sns.html', picture = picture, column=column, names=names, table=table)

#route for graphics made in R
@main.route('/r')
def r():
    return render_template('r.html')

#route for json response
@main.route('/getbar')
def bar():
    #get column
    col = request.args.get('col',0)
    # if column not empty then call a graph_bar function to draw barplot for this column
    if col !=0:
        b = graph_bar(data, col)
    else:
        b = 0
    #return jsonified response
    resp = {'picture': b}
    return jsonify(resp)

from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify
from flaskr.graphics import graph_bar, graph_heat, graph_scat
import pandas as pd
main = Blueprint('main', __name__)
data = pd.read_csv('flaskr/tables/flight_delays.csv',index_col='Month')
data_2 = pd.read_csv('flaskr/tables/insurance.csv')
@main.route('/')
def index():
    names = list(data.columns)
    column = 'NK'
    picture = {}
    picture['bar'] = graph_bar(data, column)
    picture['heat'] = graph_heat(data)
    picture['scat'] = graph_scat(data_2,'bmi','charges','smoker')
    #picture = graph()
    #print('this is bytes', picture)
    return render_template('index.html', picture = picture, column=column, names=names)



@main.route('/getbar')
def bar():
    #print('hello')
    col = request.args.get('col',0)
    #print(col)
    if col !=0:
        b = graph_bar(data, col)
    else:
        b = 0
    #print(b)
    resp = {'picture': b}
    return jsonify(resp)

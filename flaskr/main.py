from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify
from flaskr.graphics import graph_bar, graph_heat, graph_scat
from flaskr import db
from .models import Insurance
import pandas as pd

main = Blueprint('main', __name__)

data = pd.read_csv('flaskr/static/flight_delays.csv',index_col='Month')
data_2 = pd.read_csv('flaskr/static/insurance.csv')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pyt')
def pyt():
    table = [data.columns.values.tolist()]+data.values.tolist()
    names = list(data.columns)
    column = 'NK'
    picture = {}
    picture['bar'] = graph_bar(data, column)
    picture['heat'] = graph_heat(data)
    picture['scat'] = graph_scat(data_2,'bmi','charges','smoker')
    s = db.session.query(Insurance).filter_by(id=1).all()
    print(s[0])
    return render_template('sns.html', picture = picture, column=column, names=names, table=table)

@main.route('/r')
def r():
    return render_template('r.html')


@main.route('/getbar')
def bar():
    col = request.args.get('col',0)
    if col !=0:
        b = graph_bar(data, col)
    else:
        b = 0
    resp = {'picture': b}
    return jsonify(resp)

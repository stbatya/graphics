from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify, Response
from flaskr.graphics import graph
import pandas as pd
main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = pd.read_csv('flaskr/tables/flight_delays.csv')
    column = 'NK'
    picture = {}
    picture['bar']=graph(data, 'bar', column)
    #picture = graph()
    print('this is bytes', picture)

    return render_template('index.html', picture = picture)

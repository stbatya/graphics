""""Module with blueprints for drawing graphics with Seaborn"""


import base64
import io
import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
import seaborn as sns
from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify, Response, make_response
from matplotlib.figure import Figure
from matplotlib import pyplot as plt


graphics = Blueprint('graphics', __name__)

graphtypes={'bar': sns.barplot, 'heat': sns.heatmap}

def tobase64(f):
    """Converts graphics to base 64"""
    iobyte=io.BytesIO()
    f.savefig(iobyte, format="png")
    iobyte.seek(0)
    base = str(base64.b64encode(iobyte.read()), 'utf-8').strip()
    iobyte.close()
    return base

def graph_bar(data, column='NK'):
    """Draw a graph bar for a specified column in table"""
    plt.figure(figsize=(6.4, 4.8))
    s = sns.barplot(x=data.index, y=data[column])
    s.set_title('Barplot')
    output_data = tobase64(s.figure)
    s.get_figure().clf()
    return output_data

def graph_heat(data):
    """Draw a heatmap"""
    s = sns.heatmap(data=data, annot=True)
    iobyte=io.BytesIO()
    s.figure.savefig(iobyte, format="png")
    iobyte.seek(0)
    output_data = str(base64.b64encode(iobyte.read()),'utf-8').strip()
    iobyte.close()
    s.get_figure().clf()
    return output_data

def graph_scat(data, x, y, hue):
    """Draw a scatter plot for x and y columns with categorical levels hue"""
    s = sns.lmplot(data=data, x=x, y=y, hue=hue)
    output_data = tobase64(s)
    s.fig.clf()
    return output_data

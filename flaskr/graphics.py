from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify, Response, make_response
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import io
import base64
import seaborn as sns
import pandas as pd
graphics = Blueprint('graphics', __name__)

graphtypes={'bar': sns.barplot, 'heat': sns.heatmap}

def tobase64(f):
    iobyte=io.BytesIO()
    f.savefig(iobyte, format="png")
    iobyte.seek(0)
    base = str(base64.b64encode(iobyte.read()),'utf-8').strip()
    iobyte.close()
    return base

def graph_bar(data, column=None):
    # Generate the figure **without using pyplot**.
    #sns.set(rc={'figure.figsize':(6.4, 4.8)})
    plt.figure(figsize=(6.4,4.8))
    s = sns.barplot(x=data.index, y=data[column])
    s.set_title('Barplot')
    output_data = tobase64(s.figure)
    s.get_figure().clf()
    return output_data

def graph_heat(data):
    # Generate the figure **without using pyplot**.
    s = sns.heatmap(data=data,annot=True)
    iobyte=io.BytesIO()
    s.figure.savefig(iobyte, format="png")
    iobyte.seek(0)
    output_data = str(base64.b64encode(iobyte.read()),'utf-8').strip()
    iobyte.close()
    #s.figure.savefig('b2.png')
    s.get_figure().clf()
    return output_data
#def bar(data, column):

def graph_scat(data, x, y, hue):
    #s = sns.FacetGrid()
    s = sns.lmplot(data=data, x=x, y=y, hue=hue)
    #s.set_title('lmplot')
    output_data = tobase64(s)
    s.fig.clf()
    return output_data

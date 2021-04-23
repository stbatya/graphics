from flask import Blueprint
from flask import Flask
from flask import render_template, request, jsonify, Response, make_response
from matplotlib.figure import Figure
import numpy as np
import io
import base64
import seaborn as sns
import pandas as pd
graphics = Blueprint('graphics', __name__)

graphtypes={'bar': sns.barplot, 'heat': sns.heatmap}

def graph(data, graphtype='bar', column=None):
    # Generate the figure **without using pyplot**.
    f = graphtypes[graphtype]
    if not column:
        s = f(data)
    else:
        s = f(x=data.index, y = data[column])
    s.set_title('TITLE')
    iobyte=io.BytesIO()
    s.figure.savefig(iobyte, format="png")
    iobyte.seek(0)
    output_data = str(base64.b64encode(iobyte.read()),'utf-8').strip()
    iobyte.close()
    return output_data

#def bar(data, column):

import setup_analysis
import numpy as np # matrices, arrays, operators,
import matplotlib.pyplot as plt # basic visualization took
import seaborn as sns # visualization
import pandas as pd # ML, data science

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    healthList = setup_analysis.hospitalWorkerList
    
    covidPosList = []
    for doctor in healthList:
        
        covidPosList  = doctor.covidPositive
        
    covidGraph = np.random.normal(covidPosList)
    
    plt.hist(covidGraph)
    plt.show() 
    
    
    return "<p>Hello, World!</p>"

# import io
# from flask import Response
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from flask import Flask
# import numpy as np
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# app = Flask(__name__)
# @app.route('/print-plot')
# def plot_png():
#    fig = Figure()
#    axis = fig.add_subplot(1, 1, 1)
#    xs = np.random.rand(100)
#    ys = np.random.rand(100)
#    axis.plot(xs, ys)
#    output = io.BytesIO()
#    FigureCanvas(fig).print_png(output)
#    return Response(output.getvalue(), mimetype='image/png')
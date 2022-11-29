from flask import Flask
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



app = Flask(__name__)

@app.route("/members")
def members():
    members = {"members": ["mem1", "mem2", "mem3"]}
    return members

@app.route("/plot")
def plot_test():
    data1 = {"x":[1,2,3,4,5], "y": [2,3,4,5,6]}
    data2 = {"x":[1,2,3,4,5], "y": [2,3,4,5,6]}
    data3 = {"x":[1,2,3,4,5], "y": [2,3,4,5,6]}

    fig1 = px.scatter(data1, x="x", y="y")
    fig2 = px.scatter(data2, x="x", y="y")
    fig3 = px.scatter(data3, x="x", y="y")



    fig = make_subplots(rows=1, cols=3)

    for d in fig1.data:
        fig.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=1)
    for d in fig2.data:
        fig.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=2)
    for d in fig3.data:
        fig.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=3)
    
    graphJSON = plotly.io.to_json(fig)
    return graphJSON






if __name__ == "__main__":
    app.run(debug=True)



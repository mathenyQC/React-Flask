from flask import Flask
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datautils.repository import InfluxDBRepository, PostgresRepository
from datautils.decorators import DatautilsConfig
from data_transform import *





app = Flask(__name__)

# @app.route("/members")
# def members():
#     members = {"members": ["mem1", "mem2", "mem3"]}
#     return members

# @app.route("/plot")
# def plot_test():
#     data1 = {"x":[1,2,3,4,5], "y": [2,3,4,5,6]}
#     data2 = {"x":[1,2,3,4,5], "y": [2,3,4,5,6]}
#     data3 = {"x":[1,2,3,4,5], "y": [2,3,4,5,6]}

#     fig1 = px.scatter(data1, x="x", y="y")
#     fig2 = px.scatter(data2, x="x", y="y")
#     fig3 = px.scatter(data3, x="x", y="y")



#     fig = make_subplots(rows=1, cols=3)

#     for d in fig1.data:
#         fig.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=1)
#     for d in fig2.data:
#         fig.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=2)
#     for d in fig3.data:
#         fig.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=3)
    
#     graphJSON = plotly.io.to_json(fig)
#     return graphJSON

@app.route("/plot_datautils")
def plot():

    config_file = f'C:/Users/Mitchell.Matheny/code/datautils/example/mitchvm_datautils_config.ini'

    influxdb_repo = InfluxDBRepository(config=DatautilsConfig(config_file=config_file))
    zones = ['G1','G2','G3','G4','G5']

    result_df = influxdb_repo.read(experiment_name='example_experiment', limit=1)
    if result_df.loc[0]['task']:
        last_results_timestamp = result_df.loc[0]['time']
    print(last_results_timestamp)
    # print(config_file)
    postgres_repo = PostgresRepository(config=DatautilsConfig(config_file=config_file))
    results = postgres_repo.read(timestamp=last_results_timestamp)
    df = pd.DataFrame(results)

    # df_t = DataTransformation.transform_data(df,zones)


    d = {}
    for zone in zones:
        d["{0}".format(zone)]= {"x":df[zone]['x'], "y":df[zone]['y'] }

    f = make_subplots(rows = 1, cols = 5)
    i =1 
    for x in d: 
        px.scatter(d[x])
        f.add_trace((go.Scatter(x=d[x]['x'], y=d[x]['y'], name = x)), row=1, col=i)
        i += 1
    f.update_xaxes(title_text=" pi time")
    f.update_layout(height=600, width=800, title_text=df.loc['jobname'][0])

    graph = plotly.io.to_json(f)
    return graph





if __name__ == "__main__":
    app.run(debug=True)



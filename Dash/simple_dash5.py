import random
import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash(__name__)
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names=names)
app.layout = html.Div(
    [
        html.Div([
            dcc.Dropdown(
                id='ddl_x',
                options=[{'label': i, 'value': i} for i in names],
                value='sepal-width',
                style={'width':'50%'}
            ),
            dcc.Dropdown(
                id='ddl_y',
                options=[{'label': i, 'value': i} for i in names],
                value='petal-width',
                style={'width':'50%'}
            ),
        ],style={'width':'100%','display':'inline-block'}),
        html.Div([
            dcc.Graph(id='graph1')
        ],style={'width':'100%','display':'inline-block'})
    ]
)

@app.callback(
    Output(component_id='graph1', component_property='figure'),
    [
        Input(component_id='ddl_x', component_property='value'),
        Input(component_id='ddl_y', component_property='value')
    ]
)
def update_output(ddl_x_value, ddl_y_value):
    figure={
        'data': [
            go.Scatter(
                x=data[data['class'] == cls][ddl_x_value],
                y=data[data['class'] == cls][ddl_y_value],
                mode='markers',
                marker={ 'size': 15 },
                name=cls
            ) for cls in data['class'].unique()
        ],
        'layout':
            go.Layout(
                height= 350,
                hovermode= 'closest',
                title=go.layout.Title(text='Dash Interactive Data Visualization',xref='paper', x=0)
            )

    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True, port=8080, host='0.0.0.0')

import pandas as pd
import plotly.graph_objects as go
import dash
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv('OldFaithful.csv')

xAxis1 = go.Scatter(x=df['X'], y=df['Y'], mode='markers')

data = [xAxis1]
layout = go.Layout(title='Volcano eruptions', xaxis=dict(title='Duration of Eruption'), yaxis=dict(title='Wait time'))

figure = go.Figure(data=data, layout=layout)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(
        children='First Graph',
        style={
            'textAlign': 'center',
            'color': '#7FDBFF',
            'border': '2px green solid'}),

    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'),

    dcc.Graph(
        id='graph',
        figure={
            'data': data,
            'layout': layout
        }
    ),

    html.Label('Slider'),
    html.P(
        dcc.Slider(
            min=-5, max=10, step=1, value=-3
        )),

    dcc.Input(id='ip1', value='Initial Value', type='text'),
    html.Div(id='op1')


])


@app.callback(Output(component_id='op1', component_property='children'),
              [Input(component_id='ip1', component_property='value')])
def update_one(input_text):
    return 'You entered {}'.format(input_text)


if __name__ == '__main__':
    app.run_server()

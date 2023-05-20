import pandas as pd
import plotly.graph_objects as go
import dash
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv('gapminderDataFiveYear.csv')

app = Dash(__name__)
app.layout = html.Div(

    children=[
        html.H1(
            children='First Graph',
            style=dict(textAlign='center', color='#7FDBFF', border='2px green solid')
        ),

        html.Label(
            children='Select Year',
            style=dict(color='blue', fontSize=18)
        ),
        dcc.Dropdown(
            id='dropdown',
            options=[dict(label=str(year), value=year) for year in df['year'].unique()],
            value=df['year'].max()
        ),

        dcc.Graph(
            id='graph'
        )
    ]
)


@app.callback(Output(component_id='graph', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def update_graph(selected_year):
    f_df = df[df['year'] == selected_year]
    data = []
    for continent in f_df['continent'].unique():
        c_f_df = f_df[f_df['continent'] == continent]
        trace = go.Scatter(x=c_f_df['gdpPercap'],
                           y=c_f_df['lifeExp'],
                           mode='markers',
                           opacity=0.7,
                           marker=dict(size=15),
                           name=continent)
        data.append(trace)
        layout = go.Layout(title='Plots', xaxis=dict(title='GDP per Capital',), yaxis=dict(title='Life Expectancy'))
    return dict(data=data, layout=layout)


if __name__ == '__main__':
    app.run_server()

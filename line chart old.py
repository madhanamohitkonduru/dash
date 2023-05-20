import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

df=pd.read_csv('nst-est2017-alldata.csv')
df2=df[df['DIVISION'] == '1']
df2.set_index('NAME', inplace=True)
lis=[]
for col in df.columns:
    if col.startswith('POP'):
        lis.append(col)
df2=df2[lis]
data=[]
for name in df2.index:
    add_data=go.Scatter(x=df2.columns,y=df2.loc[name],mode='lines')
    data.append(add_data)
pyo.plot(data)
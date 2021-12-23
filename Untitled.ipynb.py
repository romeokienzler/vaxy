#!/usr/bin/env python
# coding: utf-8

# In[8]:


import dash
from dash import dash_table
import pandas as pd
import dash_html_components as html
from dash.dependencies import Input, Output


# In[9]:


df = pd.read_csv('data.csv')


# In[10]:


app = dash.Dash(__name__)

table = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    sort_action="native",
    sort_mode="multi"
)


# In[11]:


import dash_core_components as dcc
import plotly.graph_objs as go

fig = go.Figure(data=[go.Bar(x=df['vaccine'], y=df['severe_percenage'])])

graph = dcc.Graph(figure=fig)


# In[12]:


app.layout = html.Div(children=[
    html.H1(children='Shall I get vaccinated?'),

    html.Div(children='''
        Probability for severe (reported) side effect case in Switzerland
    '''),
    table,
    graph,
    dcc.Input(
            id="input",
            type='number'
        )
])


# In[13]:


@app.callback(
    Input("input", "value")         
)
def cb_render(*vals):
    app.layout = html.Div(children=[
        html.H1(children='Shall I get vaccinated?'),

        html.Div(children='''
            Probability for severe (reported) side effect case in Switzerland
        '''),
        table
    ])


# In[ ]:



if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8318)


# In[14]:


get_ipython().system('jupyter nbconvert Untitled.ipynb --to python --output Untitled.ipynb.py')


# In[ ]:





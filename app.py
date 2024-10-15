import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample Data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2],
})

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='My Dash App'),

    dcc.Graph(
        id='example-graph',
        figure=px.bar(df, x='Fruit', y='Amount', title='Fruit Amounts')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


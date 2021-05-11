import plotly.graph_objects as go
import numpy as np

np.random.seed(42)

# declaring size of arr
size = 7

x = np.arange(10)
y = x ** 2

fig = go.Figure(data=go.Scatter(x=x, y=x**2))

# Modifying the tickangle of the xaxis, and adjusting width and height of the image
fig.layout.template = 'plotly_dark'
fig.update_layout(
    title='Line Chart',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    xaxis_tickangle=-45,
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()

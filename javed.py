# library for manipulating the csv data
import pandas as pd
# library for scientific calculations on numbers + linear algebra
import numpy as np
import math
# library for regular plot visualizations
import matplotlib.pyplot as plt
# library for responsive visualizations
import plotly.express as px

data = pd.read_csv('swedish_insurance.csv')
data.info()

print(data.columns)
data.head(10)

fig = px.box(data['X'], points='all')
fig.update_layout(title=f'Distribution of X', title_x=0.5, yaxis_title="Number of Insurance Claims")
fig.show()
fig = px.box(data['Y'], points='all')
fig.update_layout(title=f'Distribution of Y', title_x=0.5, yaxis_title="Amount of Insurance Paid")
fig.show()

fig = px.scatter(x=data['X'], y=data['Y'])
fig.update_layout(title='Swedish Automobiles Data', title_x=0.5, xaxis_title=
"Number of Claims", yaxis_title="Payment in Claims", height=500, width=
                  700)
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.show()

data['Y']

mean_x = np.mean(data['X'])
mean_y = np.mean(data['Y'])
var_x = np.var(data['X'])
var_y = np.var(data['Y'])
print('x stats: mean= %.3f variance= %.3f' % (mean_x, var_x))
print('y stats: mean= %.3f variance= %.3f' % (mean_y, var_y))

def covariance(x, y):
 mean_x = np.mean(x)
 mean_y = np.mean(y)
 covar = 0.0
 for i in range(len(x)):
  covar += (x[i] - mean_x) * (y[i] - mean_y)
  return covar/len(x)
covar_xy = covariance(data['X'], data['Y'])
print(f'Cov(X,Y): {covar_xy}')

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['X'], y=data['Y'], name='train', mode='markers',marker_color='rgba(152, 0, 0, .8)'))
fig.update_layout(title = f'Swedish Automobiles Data\n (visual comparison for correctness)',title_x=0.5, xaxis_title= "Number of Claims", yaxis_title="Payment in Claims")
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.show()

import plotly.express as px

random_x = [0.2667, 0.6186, 0.1412, 0.2262, 1.1475, 0.1918]
names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5', 'an_6']

fig = px.pie(values=random_x, names=names)
fig.write_image("fig2.png")

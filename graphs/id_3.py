import plotly.express as px

random_x = [0.262, 0.1846, 0.1592, 0.2703, 0.1022, 0.6931]
names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5', 'an_6']

fig = px.pie(values=random_x, names=names)
fig.write_image("fig3.png")
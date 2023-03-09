import plotly.express as px

random_x = [0.1626, 0.249, 1.4634, 0.1859, 0.2006, 0.2602]
names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5', 'an_6']

fig = px.pie(values=random_x, names=names)
fig.write_image("fig1.png")
import plotly.express as px

random_x = [0.9231, 0.4138, 0.4587, 0.2006, 0.4142]
names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5']

fig = px.pie(values=random_x, names=names)
fig.write_image("fig4.png")

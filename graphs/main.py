import plotly.express as px

def plotly_id_1():
    random_x = [0.1626, 0.249, 1.4634, 0.1859, 0.2006, 2.321]
    names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5', 'an_6']

    fig = px.pie(values=random_x, names=names)
    fig.write_image("fig1.png")


def plotly_id_2():
    random_x = [0.2667, 0.6186, 0.1412, 0.2262, 1.1475, 0.1918]
    names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5', 'an_6']

    fig = px.pie(values=random_x, names=names)
    fig.write_image("fig2.png")


def plotly_id_3():
    random_x = [0.262, 0.1846, 0.1592, 0.2703, 0.1022, 0.6931]
    names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5', 'an_6']

    fig = px.pie(values=random_x, names=names)
    fig.write_image("fig3.png")


def plotly_id_4():
    random_x = [0.9231, 0.4138, 0.4587, 0.2006, 0.4142]
    names = ['an_1', 'an_2', 'an_3', 'an_4', 'an_5']

    fig = px.pie(values=random_x, names=names)
    fig.write_image("fig4.png")

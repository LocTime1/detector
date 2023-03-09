from flask import Flask, render_template, request
from draw_map import draw_map

app = Flask(__name__)


def is_correct(pos):
    pos = list(pos)
    print(pos)
    if pos[0] != '' and pos[1] != '':
        return True
    return False


@app.route("/")
def map():
    return render_template('v2.html')


@app.route("/diag")
def print_diag():
    return render_template('v1.html')

@app.route("/map", methods=["POST"])
def map_2():
    if request.method == 'POST':
        start_point_x = request.form.get('start_point_x')
        start_point_y = request.form.get('start_point_y')
        end_point_x = request.form.get('end_point_x')
        end_point_y = request.form.get('end_point_y')
        if is_correct((start_point_x, start_point_y)) and is_correct((end_point_x, end_point_y)):
            draw_map((int(start_point_x), int(start_point_y)), (int(end_point_x), int(end_point_y)))
            return render_template('map.html')
        else:
            return render_template('v2.html')
    return render_template('v2.html')


if __name__ == "__main__":
    app.run(debug=True)

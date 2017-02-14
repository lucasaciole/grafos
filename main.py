from flask import Flask, render_template, url_for
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('/home/lucassug/code/grafos/articles.json') as data_file:
        articles = json.load(data_file)

    return render_template("index.html", articles=articles['articles'])

@app.route('/projects/<name>/')
def projects(name):
    if name == "markov-snakes-ladders":
        return render_template("markov.html")

    if name == "mst-prim":
        return render_template("prim.html")

    if name == "mst-dijkstra":
        return render_template("dijkstra.html")

    if name == "caxeiro-viajante":
        return render_template("caxeiro.html")

    return render_template("404.html"), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)
from flask import Flask, render_template, url_for, redirect
import json
app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/areadetrabalho/article/<article_name>')
def unavailable_article(article_name):
    return render_template("unavailable_article.html")

@app.route('/areadetrabalho/')
def index():
    with open('articles.json') as data_file:
        articles = json.load(data_file)

    return render_template("index.html", articles=articles['articles'])

@app.route('/about/')
def about():
    return render_template("alunos.html")

@app.route('/areadetrabalho/projects/<name>/')
def projects(name):
    if name == "markov-snakes-ladders":
        return render_template("markov.html")

    if name == "mst-prim":
        return render_template("prim.html")

    if name == "mst-dijkstra":
        return render_template("dijkstra.html")

    if name == "metodo-hungaro":
        return render_template("unavailable_article.html")

    return render_template("404.html"), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)
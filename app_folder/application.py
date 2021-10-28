from flask import Flask, render_template, request
from simple_recommender import get_recommendation

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html", title = "Pseudo Saffron")


@app.route('/recommendations')
def recommender():
    form_data = dict(request.args)
    recommended_films = get_recommendation(form_data)

    return render_template("recommendations.html",
    title="Saffron Recommender",
    movies=recommended_films)



if __name__=="__main__":
    app.run("0.0.0.0")

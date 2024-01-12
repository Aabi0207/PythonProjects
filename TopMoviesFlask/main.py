from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = "72b091ffa36a724f5918040593a62c6a"
TMDB_API_READ_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MmIwOTFmZmEzNmE3MjRmNTkxODA0MDU5M2E2MmM2YSIsInN1YiI6IjY0ZjIwOTcwNWYyYjhkMDBhYmM5YjJhZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.t8crOmnwMJ-U5E2guD7YkwjhRnfw2KWBVYBpHUvuIF0"
URL_FOR_TMDB = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///My-Top-Ten-Movies.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class EditForm(FlaskForm):
    rating = StringField('Your rating out of 10 eg.7.5', [DataRequired()])
    review = StringField("Your review", [DataRequired()])
    update = SubmitField('Done')


class AddForm(FlaskForm):
    movie_name = StringField('Movie Title', [DataRequired()])
    add = SubmitField('Add')

# If running first time uncomment the following code and run only once

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    with app.app_context():
        results = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
        all_movies_list = []
        for movie in results:
            all_movies_list.append(movie)
        for ranking in range(len(all_movies_list), 0, -1):
            all_movies_list[ranking-1].ranking = ranking
    return render_template("index.html", movies=results.__reversed__())


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        with app.app_context():
            movie_to_update = db.get_or_404(Movie, id)
            movie_to_update.rating = rating
            movie_to_update.review = review
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    id = int(request.args.get('id'))
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.movie_name.data
        response = requests.get(URL_FOR_TMDB, params={"api_key": TMDB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/add/<int:movie_id>")
def add_new_movie(movie_id):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_READ_ACCESS_TOKEN}"
    }
    response = requests.get(f"{MOVIE_DB_INFO_URL}/{movie_id}", headers=headers).json()
    new_movie_to_add = Movie(
        title=response["title"],
        year=response["release_date"].split("-")[0],
        img_url=f"{MOVIE_DB_IMAGE_URL}{response['poster_path']}",
        description=response["overview"]
    )
    with app.app_context():
        db.session.add(new_movie_to_add)
        db.session.commit()
    with app.app_context():
        result = db.session.execute(db.select(Movie).where(Movie.title == response["title"])).scalar()
    return redirect(url_for('edit', id=result.id))


if __name__ == '__main__':
    app.run()

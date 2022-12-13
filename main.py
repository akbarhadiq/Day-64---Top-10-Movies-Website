from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import requests
from forms import EditForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
Bootstrap(app)
db = SQLAlchemy(app)

# Movies database model 

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description=db.Column(db.String(1000), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)



@app.route("/")
@app.route("/home")
def home():

    # new_movie=Movies(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone both, pinned by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )

    # db.session.add(new_movie)
    # db.session.commit()

    all_movies = Movies.query.all()

    return render_template("index.html", all_movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form=EditForm()

    if request.method == "POST":
        rating = form.rating.data
        review = form.review.data
        movie_id = form.hidden_id.data
        # take releveant information from the form

        movie_to_update = Movies.query.get(movie_id)
        # get the movie by querying database via movie id

        # update it
        movie_to_update.rating = rating
        movie_to_update.review = review

        # commit the database
        db.session.commit()
        return redirect(url_for('home'))

    movie_id=request.args.get("id")
    movie = Movies.query.get(movie_id)
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete", methods=["POST","GET"])
def delete():
    # get the id
    movie_id = request.args.get("id")
    # query the movie data from the database by id
    movie_to_delete = Movies.query.get(movie_id)
    # delete the movie
    db.session.delete(movie_to_delete)
    # commit database
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
    # db.create_all() database created. comment this out

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import Movie, app, db

with app.app_context():
    results = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    for result in results:
        print(result.rating)



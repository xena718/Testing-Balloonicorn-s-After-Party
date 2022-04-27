from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    
    Game.query.delete()

    sev = Game(name="7 Wonders",description="exploring 7 wonders of the world and build the best wonder to beat other players ")
    uno = Game(name="Uno", description="play a card game called uno")
    sushigo = Game(name="sushi go", description="not about eating sushi at all.")

    db.session.add_all([sev, uno, sushigo])
    db.session.commit()

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")

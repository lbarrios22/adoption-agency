from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

class Pet(db.Model):
    '''Shows a pet that is eligble for adoption'''

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<Pet id={self.id}, name={self.name}, species={self.species}, photo_url={self.photo_url}, age={self.age}, notes={self.notes}, available={self.available}'

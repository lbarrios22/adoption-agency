from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
from forms import NewPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'skjdb23432'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('all_pets.html', pets=pets)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def view_pet(pet_id):

    pet = Pet.query.get(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        
        return redirect('/')

    else:
        return render_template('view_pets.html', pet=pet, form=form)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    
    form = NewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('new_pet_form.html', form=form)




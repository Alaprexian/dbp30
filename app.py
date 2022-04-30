from flask import (
    Flask,
    abort,
    jsonify,
    redirect, 
    render_template, 
    request,
    url_for
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5051111@localhost:5432/lab30'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Formulario(db.Model):
    __tablename__="formulario"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(40),nullable = False)
    apellidos = db.Column(db.String(40),nullable = False)
    sexo = db.Column(db.String(40),nullable = False)
    email = db.Column(db.String(40),nullable = False)
    ndocumento=db.Column(db.Integer,nullable = False)
    calificacion=db.Column(db.Integer,nullable = False)
    def __repr__(self):
        return f'Formulario: {self.id},{self.name},{self.apellidos},{self.sexo},{self.email},{self.ndocumento},{self.calificacion}'

    db.create_all()

    @app.route('/elecc1')
    def eleccion1():
        return render_template('elecc1.html')

    @app.route('/datos')
    def datos():
        return render_template('datos.html', data=Formulario.query.all())   

@app.route('/create/formulario', methods=['POST'])
def formulario():
    name = request.get_json()['name']
    apellidos = request.get_json()['apellidos']
    sexo = request.get_json()['sexo']
    email = request.get_json()['email']
    ndocumento= request.get_json()['ndocumento']
    calificacion=request.get_jason()['calificacion']
    fun = Formulario(name = name,apellidos = apellidos, sexo = sexo, email = email, ndocumento = ndocumento, calificacion = calificacion)
    db.session.add(fun)
    db.session.commit()
    db.session.close()
    return jsonify()

@app.route('/')
def index():
    return render_template('index.html')
if __name__ =='__main__':
    app.run(port = 5003, debug=True)
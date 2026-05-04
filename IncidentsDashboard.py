from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
db = SQLAlchemy(app)

class Incidents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.String)
    Type = db.Column(db.String)
    Severity = db.Column(db.String)
    Affected_area = db.Column(db.String)
    Description = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route('/')
def route():
    return render_template('index.html')

@app.route('/api/tipos')
def get_types():
    incidents = Incidents.query.all()
    tipos = {}
    for incident in incidents:
        tipo = incident.Type
        if tipo in tipos:
            tipos[tipo] += 1
        else:
            tipos[tipo] = 1
    return jsonify(tipos)

@app.route('/api/severidade')
def get_severity():
    incidents = Incidents.query.all()
    severidades = {}
    for incident in incidents:
        severidade = incident.Severity
        if severidade in severidades:
            severidades[severidade] +=1
        else:
            severidades[severidade] = 1
    return jsonify(severidades)

@app.route('/api/meses')
def get_months():
    incidents = Incidents.query.all()
    meses = {}
    for incident in incidents:
        mes = incident.Date[:7]
        if mes in meses:
            meses[mes] +=1
        else:
            meses[mes] = 1
    meses = dict(sorted(meses.items()))
    return jsonify(meses)


if __name__ == '__main__':
    app.run()



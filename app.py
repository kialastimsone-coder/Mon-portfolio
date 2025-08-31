from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/competence')
def competence():
    return render_template('competence.html')


@app.route('/projet')
def projet():
    return render_template('projet.html')


@app.route('/apropos')
def apropos():
    return render_template('APropos.html')


@app.route('/contact')
def contact():
    return render_template('Contact.html')


@app.route('/service')
def service():
    return render_template('service.html')


if __name__ == '__main__':
    app.run(debug=True)

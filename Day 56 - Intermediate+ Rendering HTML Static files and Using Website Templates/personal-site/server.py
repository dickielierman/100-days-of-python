from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/elements')
def elements_page():
    return render_template('elements.html')

@app.route('/generic')
def generic_page():
    return render_template('generic.html')

if __name__ == '__main__':
    app.run(debug=True)
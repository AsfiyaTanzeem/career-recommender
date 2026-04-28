from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # The pure Welcome Page
    return render_template('index.html')

@app.route('/choose')
def choose():
    # The separate Selection Page
    return render_template('choose.html')

@app.route('/10th')
def tenth():
    return render_template('10th.html')

@app.route('/intermediate')
def intermediate():
    return render_template('intermediate.html')

@app.route('/degree')
def degree():
    return render_template('degree.html')

@app.route('/diploma')
def diploma():
    return render_template('diploma.html')

@app.route('/vocational')
def vocational():
    return render_template('vocational.html')

##if __name__ == '__main__':
    ##app.run(debug=True)

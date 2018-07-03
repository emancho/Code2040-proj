from flask import Flask, render_template, url_for

app = Flask(__name__)
links_to_code = ['https://www.codecademy.com/','https://www.codewars.com/dashboard','https://codefights.com/']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coding')
def coding():
    return render_template('coding.html',links_to_code=links_to_code)

@app.route('/jobs')
def jobs():
    return render_template('job.html')

@app.route('/housing')
def housing():
    return render_template('housing.html')

if __name__ == '__main__':
    app.run(debug=True)

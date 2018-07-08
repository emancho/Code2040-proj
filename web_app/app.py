from flask import Flask, render_template, url_for

app = Flask(__name__)
links_to_code = ['https://www.codecademy.com/','https://www.codewars.com/dashboard','https://codefights.com/']
housing_links = ['https://larkinstreetyouth.org/','http://lyric.org/','http://www.homelessyouthalliance.org/','http://www.firstplaceforyouth.org/','https://atthecrossroads.org/','https://www.ccsf.edu/en/student-services/student-counseling/guardians-scholars-program.html']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coding')
def coding():
    return render_template('coding.html',links_to_code=links_to_code)

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/housing')
def housing():
    return render_template('housing.html',housing_links=housing_links)

if __name__ == '__main__':
    app.run(debug=True)

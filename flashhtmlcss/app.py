from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/user/<namePython>")
def user(namePython):
    return render_template('user.html', namehtml=namePython)

@app.route('/info/<name>/<int:age>')
def info(name, age):
    return render_template('info.html', namehtml=name, agehtml=age)


if __name__ == '__main__':
    app.run(debug=True) 
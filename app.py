from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search", methods=['GET','POST'])
def search():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
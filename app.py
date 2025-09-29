# cv_extractor/app.py
from flask import Flask, render_template
from router import api_bp as api_app

app = Flask(__name__)
app.register_blueprint(api_app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
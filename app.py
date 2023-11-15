from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9002))
    app.run(debug=True, host="0.0.0.0", port=port)
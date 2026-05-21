from flask import Flask
import sys

app = Flask(__name__)

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

print(sys.executable)

app.run(host="0.0.0.0", port=5000, debug=False)

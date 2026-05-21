from flask import Flask
import sys

app = Flask(__name__)

@app.route("/api")
def api():
    return {
        "name": "Hackup",
        "course": "Python"
    }

print(sys.executable)

app.run(host="0.0.0.0", port=5000, debug=False)

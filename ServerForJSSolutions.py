from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

#Euler Solutions
@app.route('/')
def root():
    return render_template('EulerSolutions.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)

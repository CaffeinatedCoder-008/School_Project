from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('circle.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    radius = float(request.form.get('radius'))
    circumference = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    return jsonify({'circumference': circumference, 'area': area})

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Run on a different port to avoid conflict

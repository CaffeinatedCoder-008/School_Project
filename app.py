from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    n = int(request.form.get('number'))
    fib_series = fibonacci(n)
    return jsonify(fib_series)

if __name__ == '__main__':
    app.run(debug=True)

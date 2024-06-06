from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('marks.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    marks = [int(request.form.get(f'subject{i}')) for i in range(1, 6)]
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    return jsonify({'total': total_marks, 'average': average_marks})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run on a different port to avoid conflict

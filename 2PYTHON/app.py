import json
from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('json')
    json_data = json.loads(data)
    response = json.dumps(json_data, separators=(',', ':'))
    return Response(response, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)



# Run Terminal  "py app.py"
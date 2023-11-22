from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    result = a + b

    response = f'Here is the sum of a + b: {result}'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
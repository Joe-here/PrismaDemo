from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/unsafe-eval', methods=['POST'])
def unsafe_eval():
    # Intentionally insecure: Using eval on user input
    return str(eval(request.data))

if __name__ == '__main__':
    app.run()


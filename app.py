from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome to gandhi Final Test API Server"

@app.route('/host')
def host():
    return "Host route works!"

@app.route('/ip')
def ip():
    return "IP route works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
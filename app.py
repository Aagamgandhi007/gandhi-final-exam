from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to gandhi Final Exam Test API Server"

@app.route('/host')
def host():
    hostname = socket.gethostname()
    return f"Host route works! Hostname: {hostname}"

@app.route('/ip')
def ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    return f"IP route works! IP: {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
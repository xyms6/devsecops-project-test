from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, DevSecOps!"

@app.route('/admin')
def admin():
    
    password = os.getenv("ADMIN_PASSWORD", "senha_nao_definida")
    return f"Área admin — senha: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
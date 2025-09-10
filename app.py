from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, DevSecOps!"

@app.route('/admin')
def admin():
    # ISSO É UMA VULNERABILIDADE INTENCIONAL — VAMOS DETECTAR DEPOIS!
    password = "senha123"
    return f"Área admin — senha: {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
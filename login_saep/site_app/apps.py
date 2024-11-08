from django.apps import AppConfig


class SiteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_app'
# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os usuários cadastrados
usuarios = []

@app.route('/')
def index():
    return render_template('index.html', usuarios=usuarios)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    if nome and email:
        usuarios.append({'nome': nome, 'email': email})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

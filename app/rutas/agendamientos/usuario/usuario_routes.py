from flask import Blueprint, render_template, request, redirect, url_for, flash

usuario_bp = Blueprint('usuario', __name__, template_folder='templates')

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de inicio de sesión aquí
        flash("Inicio de sesión exitoso")
        return redirect(url_for('index'))  # Redirigir a la página de inicio
    return render_template('login.html')

@usuario_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Lógica de registro aquí
        flash("Registro exitoso")
        return redirect(url_for('usuario.login'))  # Redirigir a la página de inicio de sesión
    return render_template('registro.html')


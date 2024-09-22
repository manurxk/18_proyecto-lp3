from flask import Blueprint, render_template, jsonify
from app.dao.referenciales.direccion.DireccionDao import DireccionDao

dirmod = Blueprint('direccion', __name__, template_folder='templates')

@dirmod.route('/direccion-index')
def direccionIndex():
    dirdao = DireccionDao()
    return render_template('direccion-index.html', lista_direcciones=dirdao.getDirecciones())
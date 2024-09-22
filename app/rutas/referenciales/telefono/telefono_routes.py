from flask import Blueprint, render_template, jsonify
from app.dao.referenciales.telefono.TelefonoDao import TelefonoDao

telmod = Blueprint('telefono', __name__, template_folder='templates')

@telmod.route('/telefono-index')
def telefonoIndex():
    teldao = TelefonoDao()
    return render_template('telefono-index.html', lista_telefonos=teldao.getTelefonos())
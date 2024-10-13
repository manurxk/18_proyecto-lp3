from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.usuario.UsuarioDao import UsuarioDao
from werkzeug.security import generate_password_hash, check_password_hash

usuarios_api_bp = Blueprint('usuarios_api', __name__)

# Crear un nuevo usuario
@usuarios_api_bp.route('/crear', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    usuariodao = UsuarioDao()

    campos_requeridos = ['nombre_usuario', 'contrasena']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_usuario = data['nombre_usuario']
        contrasena = generate_password_hash(data['contrasena'])  # Encriptar la contraseña

        usuario_id = usuariodao.guardarUsuario(nombre_usuario, contrasena)

        if usuario_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': usuario_id, 'nombre_usuario': nombre_usuario},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el usuario. Consulte con el administrador.' }), 500

    except Exception as e:
        app.logger.error(f"Error al crear usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Iniciar sesión
@usuarios_api_bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    usuariodao = UsuarioDao()

    campos_requeridos = ['nombre_usuario', 'contrasena']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_usuario = data['nombre_usuario']
        contrasena = data['contrasena']

        usuario = usuariodao.getUsuarioByNombre(nombre_usuario)

        if usuario and check_password_hash(usuario['contrasena'], contrasena):
            return jsonify({
                'success': True,
                'data': {'id': usuario['id'], 'nombre_usuario': nombre_usuario},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Credenciales incorrectas. Por favor, verifique su nombre de usuario o contraseña.'
            }), 401

    except Exception as e:
        app.logger.error(f"Error al iniciar sesión: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Obtener un usuario por ID
@usuarios_api_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    usuariodao = UsuarioDao()

    try:
        usuario = usuariodao.getUsuarioById(usuario_id)

        if usuario:
            return jsonify({
                'success': True,
                'data': usuario,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el usuario con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualizar un usuario
@usuarios_api_bp.route('/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    data = request.get_json()
    usuariodao = UsuarioDao()

    campos_requeridos = ['nombre_usuario']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_usuario = data['nombre_usuario']

        if usuariodao.updateUsuario(usuario_id, nombre_usuario):
            return jsonify({
                'success': True,
                'data': {'id': usuario_id, 'nombre_usuario': nombre_usuario},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el usuario con el ID proporcionado o no se pudo actualizar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al actualizar usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Eliminar un usuario
@usuarios_api_bp.route('/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    usuariodao = UsuarioDao()

    try:
        if usuariodao.deleteUsuario(usuario_id):
            return jsonify({
                'success': True,
                'mensaje': f'Usuario con ID {usuario_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el usuario con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar usuario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

from flask import Flask

app = Flask(__name__)
    
# importar referenciales
from app.rutas.referenciales.index.index_routes import indmod #index
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod #ciudad
from app.rutas.referenciales.paises.pais_routes import paimod #pais
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod  #nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocupmod  #ocupacion
from app.rutas.referenciales.estado_civil.estado_civil_routes import estacivmod  #estado civil
from app.rutas.referenciales.sexo.sexo_routes import sexmod  #sexo
from app.rutas.referenciales.especialidad.especialidad_routes import especimod  #especialidad
from app.rutas.referenciales.dia.dia_routes import diamod  #dia
from app.rutas.referenciales.estado_cita.estado_cita_routes import estacitmod  #estado de la cita
from app.rutas.referenciales.duracion_consulta.duracion_consulta_routes import duraconsumod  #duracion de la consulta
from app.rutas.referenciales.diagnostico.diagnostico_routes import diagmod  # diagnostico
from app.rutas.referenciales.turno.turno_routes import turmod # turno

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(indmod, url_prefix=f'{modulo0}/index') #index
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad') #ciudad
app.register_blueprint(paimod, url_prefix=f'{modulo0}/paises') #paises
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona') #persona
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')  #nacionalidad
app.register_blueprint(ocupmod, url_prefix=f'{modulo0}/ocupacion')  #ocupacion
app.register_blueprint(estacivmod, url_prefix=f'{modulo0}/estadocivil')  #estado civil
app.register_blueprint(sexmod, url_prefix=f'{modulo0}/sexo')  #sexo
app.register_blueprint(estacitmod, url_prefix=f'{modulo0}/estadocita')  #estado de la cita
app.register_blueprint(especimod, url_prefix=f'{modulo0}/especialidad') #especialidad
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia') #dia
app.register_blueprint(duraconsumod, url_prefix=f'{modulo0}/duracionconsulta') #duracion de la consulta
app.register_blueprint(diagmod, url_prefix=f'{modulo0}/diagnostico')  # diagnostico
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')  # turno



#ciudad
from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
#pais
from app.rutas.referenciales.paises.pais_api import paisapi
#persona
from app.rutas.referenciales.persona.persona_api import perapi
#nacionalidad
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacioapi
#nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_api import ocupapi
#estado civil
from app.rutas.referenciales.estado_civil.estado_civil_api import estacivapi
#sexo
from app.rutas.referenciales.sexo.sexo_api import sexapi
#estado de la cita
from app.rutas.referenciales.estado_cita.estado_cita_api import estacitapi
#especialidad
from app.rutas.referenciales.especialidad.especialidad_api import especiapi
#dia
from app.rutas.referenciales.dia.dia_api import diaapi
#duracion de la consulta
from app.rutas.referenciales.duracion_consulta.duracion_consulta_api import duraconsuapi
# diagnostico
from app.rutas.referenciales.diagnostico.diagnostico_api import diagapi  
# turno
from app.rutas.referenciales.turno.turno_api import turnoapi 


# APIS v1
#Ciudad
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

#Pais
version1 = '/api/v1'
app.register_blueprint(paisapi, url_prefix=version1)


#persona
version1 = '/api/v1'
app.register_blueprint(perapi, url_prefix=version1)


#nacionalidad
version1 = '/api/v1'
app.register_blueprint(nacioapi, url_prefix=version1)

#ocupacion
version1 = '/api/v1'
app.register_blueprint(ocupapi, url_prefix=version1)


#Estado civil
version1 = '/api/v1'
app.register_blueprint(estacivapi, url_prefix=version1)

#sexo
version1 = '/api/v1'
app.register_blueprint(sexapi, url_prefix=version1)

#Estado de la cita
version1 = '/api/v1'
app.register_blueprint(estacitapi, url_prefix=version1)

#especialidad
version1 = '/api/v1'
app.register_blueprint(especiapi, url_prefix=version1)

#dia
version1 = '/api/v1'
app.register_blueprint(diaapi, url_prefix=version1)


#duracion de la consulta
version1 = '/api/v1'
app.register_blueprint(duraconsuapi, url_prefix=version1)

# Diagnóstico
version1 = '/api/v1'
app.register_blueprint(diagapi, url_prefix=version1)  # diagnóstico


# Turno
version1 = '/api/v1'
app.register_blueprint(turnoapi, url_prefix=version1) 






























from flask import render_template, request, redirect, url_for

@app.route('/buscar', methods=['GET'])
def buscar():
    # Obtener el término de búsqueda del formulario
    termino = request.args.get('termino').lower()

    # Definir las rutas posibles
    rutas = {
        'ciudad': 'ciudad.ciudadIndex',
        'pais': 'pais.paisIndex',
        'nacionalidad': 'nacionalidad.nacionalidadIndex',
        'ocupacion': 'ocupacion.ocupacionIndex',
        'estado civil': 'estadocivil.estadocivilIndex',
        'sexo': 'sexo.sexoIndex',
        'persona': 'persona.personaIndex',
        'cita': 'estadocita.estadocitaIndex',
        'especialidad': 'especialidad.especialidadIndex',
        'dias': 'dia.diaIndex',
    }

    # Verificar si el término coincide con alguna clave en rutas
    if termino in rutas:
        # Redirigir a la página correspondiente
        return redirect(url_for(rutas[termino]))
    else:
        # Renderizar una página con un mensaje de "no encontrado"
        return render_template('no_encontrado.html', termino=termino)
    
from flask import render_template, request, redirect, url_for

@app.route('/login')
def login():
    return render_template('login.html')

      # Importar el blueprint de rutas principales

def create_app():
    app = Flask(__name__)
    
    # Registrar los Blueprints
    app.register_blueprint()

    return app












# from flask import Flask, render_template, request, redirect, url_for, flash

# app = Flask(__name__)
# app.secret_key = 'mi_secreto'  # Necesario para mostrar mensajes flash

# # Usuarios de ejemplo (puedes conectar a una base de datos)
# users = {
#     'admin': '6814403',
#     'usuario': '6814403'
# }

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Validar credenciales
#         if username in users and users[username] == password:
#             return redirect(url_for('dashboard'))
#         else:
#             error = 'Credenciales inválidas. Intente de nuevo.'
    
#     return render_template('login.html', error=error)

# @app.route('/dashboard')
# def dashboard():
#     return "¡Bienvenido al Dashboard!"

# if __name__ == '__main__':
#     app.run(debug=True)

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
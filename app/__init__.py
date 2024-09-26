from flask import Flask

app = Flask(__name__)
    





  # Importar el blueprint de rutas principales

def create_app():
    app = Flask(__name__)
    
    # Registrar los Blueprints
    app.register_blueprint()

    return app






# importar referenciales

from app.rutas.referenciales.index.index_routes import indmod

from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.paises.pais_routes import paimod
from app.rutas.referenciales.correo.correo_routes import cormod
from app.rutas.referenciales.telefono.telefono_routes import telmod
from app.rutas.referenciales.direccion.direccion_routes import dirmod
from app.rutas.referenciales.persona.persona_routes import permod
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import naciomod  #nacionalidad
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocupmod  #ocupacion
from app.rutas.referenciales.estado_civil.estado_civil_routes import estacivmod  #estado civil
from app.rutas.referenciales.sexo.sexo_routes import sexmod  #sexo
# registrar referenciales
modulo0 = '/referenciales'

app.register_blueprint(indmod, url_prefix=f'{modulo0}/index')

app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/paises')
app.register_blueprint(cormod, url_prefix=f'{modulo0}/correo')
app.register_blueprint(telmod, url_prefix=f'{modulo0}/telefono')
app.register_blueprint(dirmod, url_prefix=f'{modulo0}/direccion')
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')
app.register_blueprint(naciomod, url_prefix=f'{modulo0}/nacionalidad')  #nacionalidad
app.register_blueprint(ocupmod, url_prefix=f'{modulo0}/ocupacion')  #ocupacion
app.register_blueprint(estacivmod, url_prefix=f'{modulo0}/estadocivil')  #estado civil
app.register_blueprint(sexmod, url_prefix=f'{modulo0}/sexo')  #sexo
 

#ciudad
from app.rutas.referenciales.ciudad.ciudad_api import ciuapi

#pais
from app.rutas.referenciales.paises.pais_api import paisapi

#correo
from app.rutas.referenciales.correo.correo_api import correoapi

#telefono
from app.rutas.referenciales.telefono.telefono_api import telapi

#direccion
from app.rutas.referenciales.direccion.direccion_api import dirapi

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

# APIS v1
#Ciudad
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

#Pais
version1 = '/api/v1'
app.register_blueprint(paisapi, url_prefix=version1)

#correo
version1 = '/api/v1'
app.register_blueprint(correoapi, url_prefix=version1)


#telefono
version1 = '/api/v1'
app.register_blueprint(telapi, url_prefix=version1)

#direccion
version1 = '/api/v1'
app.register_blueprint(dirapi, url_prefix=version1)

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
from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
from app.rutas.referenciales.paises.pais_routes import paimod
from app.rutas.referenciales.correo.correo_routes import cormod
from app.rutas.referenciales.telefono.telefono_routes import telmod
from app.rutas.referenciales.direccion.direccion_routes import dirmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(paimod, url_prefix=f'{modulo0}/paises')
app.register_blueprint(cormod, url_prefix=f'{modulo0}/correo')
app.register_blueprint(telmod, url_prefix=f'{modulo0}/telefono')
app.register_blueprint(dirmod, url_prefix=f'{modulo0}/direccion')

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
from flask import Blueprint, render_template

indmod = Blueprint('index', __name__, template_folder='templates')

@indmod.route('/index-index')
def indexIndex():
    return render_template('index-index.html')



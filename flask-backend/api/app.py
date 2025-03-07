from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)

    from modules.pacientes import bp as bppacientes
    from modules.medicamentos import bp as bpmedicamentos
 
    app.register_blueprint(bppacientes)
    app.register_blueprint(bpmedicamentos) 

    return app

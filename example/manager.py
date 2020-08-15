from flask_pastedeploy import PasteDeployWrapper
from werkzeug.serving import run_simple
from app import app

paste = PasteDeployWrapper()
deploy = paste.setup_app(app)
run_simple("localhost", 9999, deploy)


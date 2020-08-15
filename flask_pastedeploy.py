from paste import deploy
import os

FLASK_PASTEDEPLOY_FILE = "flask_pastedeploy.app"


class PasteDeployWrapper(object):

    def __init__(self, *local_cfg):
        # app 类的参数，不能存在app参数，必须不含参数或者为关键字
        pass

    def setup_app(self, app):
        PASTE_URL = app.config.get("PASTE_DEPLOY_CFG")
        PASTE_NAME = app.config.get("PASTE_DEPLOY_NAME", "main")
        app_url = app.config.get("APP_URL")
        if not app_url:
            raise Exception("APP_URL can not be None")
        self.write_app(app_url)
        if not os.path.exists(PASTE_URL):
            self.write_cfg(PASTE_URL, PASTE_NAME)
        return deploy.loadapp("config:%s" % PASTE_URL, PASTE_NAME)

    def write_cfg(self, file_path, paste_name):
        api_paste_filename = os.path.basename(file_path)
        api_app_name = api_paste_filename.split(".")[0]
        with open(file_path, 'w+') as f:
            f.write("[pipeline:%s]\npipeline = %s\n\n"
                    % (paste_name, api_app_name))
            f.write("[app:%s]\npaste.app_factory = "
                    "flask_pastedeploy:PasteDeployWrapper\n"
                    % api_app_name)

    def write_app(self, app_url):
        with open(FLASK_PASTEDEPLOY_FILE, 'w') as f:
            f.write(app_url)

    def read_app(self):
        with open(FLASK_PASTEDEPLOY_FILE) as f:
            return f.read()

    def load_app(self, module_app):
        str_module = module_app.split(":")[0]
        str_app = module_app.split(":")[1]
        module = __import__(str_module)
        return getattr(module, str_app)

    def __call__(self, environ, start_response):
        module_app = self.read_app()
        app = self.load_app(module_app)
        return app.wsgi_app(environ, start_response)

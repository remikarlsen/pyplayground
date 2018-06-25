import yaml


class AppConfig:

    __conf = {}

    __cred = {}

    _models = {
        "MODEL_PATH": "models/the_model.pb"
    }

    __setters = ["username", "password", "url"]


    @staticmethod
    def config(name):
        return AppConfig.__conf[name]

    @staticmethod
    def set(name, value):
        if name in AppConfig.__setters:
            AppConfig.__conf[name] = value
        else:
            raise NameError("Name not accepted in set() method")

    @staticmethod
    def load_credentials(file):
        try:
            with open(file) as creds:
                AppConfig.__cred.update(yaml.load(creds.read()))
        except Exception as e:
            print(e)
        print(AppConfig.__cred)

    @staticmethod
    def load_app_settings(file):
        try:
            with open(file) as config:
                AppConfig.__conf.update(yaml.load(config.read()))
        except Exception as e:
            print(e)
        print(AppConfig.__conf)

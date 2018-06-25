from config import AppConfig


AppConfig.load_credentials(file='../config/credentials.yml')
AppConfig.load_app_settings(file='../config/app_settings.yml')
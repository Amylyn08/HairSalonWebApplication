import secrets

#this is the config to use when under DEVeloppment
class ConfigDev:
    secret_key = secrets.token_hex(16)
    SECRET_KEY=secret_key
    DEBUG = True

#this is the config to use when PRODUCTION i.e. when deployemen.
class ConfigProd(ConfigDev):
    DEBUG = False
    Testing = False

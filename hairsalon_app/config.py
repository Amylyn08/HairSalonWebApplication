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

          # <!-- <a href="{{ url_for('') }}">BOOK NOW </a> -->
        #       <div id="session-info">
        #     {% block content_session %}
        #     <!-- default view -->
        #     <p>Project w24 Visitor view</p>
        #     <!-- Session view to override if needed: INSERT WHAT THE VIEW IS, admin? member?prof? super? -->
        #     {% endblock %}
        #     <p>Hi {{current_user.username}}</p>
        # </div>
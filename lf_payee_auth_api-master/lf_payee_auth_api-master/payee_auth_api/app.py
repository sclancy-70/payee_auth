import hyperwallet
from .config import Config
from flask import Flask
from flask import jsonify
from flask_cors import CORS

import logging
logging.basicConfig(level=logging.INFO,
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()


CONFIG = Config()
hw_api = hyperwallet.Api(
    CONFIG.api_user,
    CONFIG.api_password,
    CONFIG.program_token,
    CONFIG.api_url
)

cors_config = {
    'methods': ['GET', 'OPTIONS'],
    "origins": CONFIG.cors_origins
}

def create_app():
    app = Flask(__name__)
    CORS(app, **cors_config)

    @app.route('/')
    def default():
        resp = jsonify({'message': 'Please use /auth'})
        return resp

    @app.route('/auth')
    def getAuthToken():
        try:
            auth_token = hw_api.getAuthenticationToken(CONFIG.user_token)
        except Exception as err:
            logger.error(err)
            resp = jsonify({'error': 'An unexpected error occured.'})
            resp.status_code=500
            resp.mimetype='application/json'
            return resp

        resp = jsonify({"token": auth_token.value})
        resp.status_code=200
        resp.mimetype='application/json'
        return resp
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
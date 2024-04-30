from flask import Blueprint, request, jsonify, current_app

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
        return jsonify({'message': 'Welcome to the {} API'.format(current_app.config['API_NAME'])})

@main_bp.route('/about')
def about():
        return jsonify({
                'API_Version': current_app.config['API_VERSION'],
                'API_NAME': current_app.config['API_NAME'],
                'API_URL': current_app.config['API_URL']
        })
from flask import Blueprint, request, jsonify
from app.models import db, User
import jwt
from datetime import datetime, timedelta  
import random
import string
from  app.forgot_password import send_reset_password_email
auth_bp = Blueprint('auth', __name__)
def generate_random_password():
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    password_characters = f'{letters}{numbers}{special_characters}'
    password = ''.join(random.choice(password_characters) for i in range(10))
    return password
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password'] 
    username = data['username']

    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']
    address = data['address']
    avatar = data['avatar']
    loginType = data['loginType']
    
    if loginType in ['Google', 'Facebook']:
        password = f"{loginType}LoginPasswordForMazadMarket"
    
    if not (email and password and username  and first_name and last_name and phone and address and avatar and loginType):
        return jsonify({'message': 'All fields are required'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    new_user = User(
        email=email,
        password=password,
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        address=address,
        avatar=avatar,
        loginType=loginType
    )
    
    db.session.add(new_user)
    db.session.commit()

    secret_key = 'MazadMarket2025@youfucksys'
    token = jwt.encode({'id': new_user.id, 'exp': datetime.utcnow() + timedelta(days=30)}, secret_key, algorithm="HS256")
    return jsonify({'token': token, 'user': new_user.serialize()}), 201

@auth_bp.route('/check_token', methods=['POST'])
def check_token():
    data = request.get_json()
    token = data['token']
    secret_key = 'MazadMarket2025@youfucksys'
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        user = User.query.get(payload['id'])
        if user:
            return jsonify({'user': user.serialize()}), 200
        return jsonify({'message': 'User not found'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401   

@auth_bp.route('/login', methods=['POST'])
def login():
    secret_key = 'MazadMarket2025@youfucksys'
    data = request.get_json()
    username = data['username']
    password = data['password']
    loginType = data['login_type']
    try :
        if not (username):
            return jsonify({'message': 'All fields are required'}), 400
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User.query.filter_by(email=username).first()
            if not user:
                user = User.query.filter_by(phone=username).first()
                if not user:
                    return jsonify({'message': 'user is not found'}), 404
        if user.loginType != loginType:
            return jsonify({'message': 'user is not found'}), 
        elif user.loginType == loginType:
            if user.loginType == "Google" or user.loginType == 'Facebook':
                token = jwt.encode({'id': new_user.id, 'exp': datetime.utcnow() + timedelta(days=30)}, secret_key, algorithm="HS256")
                return jsonify({'token': tocken, 'user': user.serialize()}), 201
            elif user.loginType == 'Form':
                if user.password == password:
                    token = jwt.encode({'id': new_user.id, 'exp': datetime.utcnow() + timedelta(days=30)}, secret_key, algorithm="HS256")
                    return jsonify({'token': tocken, 'user': user.serialize()}), 201
                return jsonify({'message': 'Invalid password'}), 401
    except :
        return jsonify({'message': 'Invalid username'}), 401
@auth_bp.route('/forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data['email']
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    new_password = generate_random_password()
    user.password = new_password
    db.session.add(user)
    db.session.commit()
    print(new_password)
    send_reset_password_email(email, new_password)
    return jsonify({'message': 'Reset password link has been sent to your email'}), 200
@auth_bp.route('/delete_account', methods=['POST'])
def delete_account():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    if user.password != password:
        return jsonify({'message': 'Invalid password'}), 401
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Account deleted successfully'}), 200

@auth_bp.route('/edit_account', methods=['POST'])
def edit_account():
    data = request.get_json()
    tocken = data['tocken']
    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']
    address = data['address']
    avatar = data['avatar']
    secret_key = 'MazadMarket2025@youfucksys'
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        user = User.query.get(payload['id'])
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.address = address
            user.avatar = avatar
            db.session.add(user)
            db.session.commit()
            return jsonify({'user': user.serialize()}), 200
        return jsonify({'message': 'User not found'}), 404
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401  


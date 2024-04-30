from flask import Blueprint, render_template, session, request,redirect
from app.models import AdminAcconts
from datetime import timedelta
admin_bp = Blueprint('admin', __name__)

# Set session lifetime to 30 days
admin_bp.permanent_session_lifetime = timedelta(days=30)
# ============ Auth ============
@admin_bp.route('/login')
def admin_login():
    return render_template('login.html')

@admin_bp.route('/login', methods=['POST'])
def admin_login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    user = AdminAcconts.query.filter_by(email=username, password=password).first()
    print(f"username and password are: {username} and {password}")
    if not user:
        return render_template('login.html', message='Invalid Credentials')

    # Setting session data
    session['logged_in'] = True
    session['user_id'] = user.id
    session['email'] = user.email
    session['name'] = user.first_name + ' ' + user.last_name
    session.permanent = True  # Make session permanent
    
    return redirect('/admin/dashboard')
@admin_bp.route('/logout')
def admin_logout():
        session.pop('logged_in', None)
        session.pop('user_id', None)
        session.pop('email', None)
        session.pop('name', None)
        return redirect('/admin/login')
# =========== mains =======================
@admin_bp.route('/dashboard')
def admin_dashboard():
    if 'logged_in' in session:
        return render_template('index.html', title='Dashboard')
    return redirect('/admin/login')

@admin_bp.route('/settings')
def admin_settings():
    return render_template('index.html')

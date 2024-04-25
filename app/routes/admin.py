from flask import Blueprint,render_template,session


admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login')
def admin_login():
        return render_template('login.html')

@admin_bp.route('/dashboard')
def admin_dashboard():
        return render_template('index.html',title='Dashboard')

@admin_bp.route('/settings')
def admin_settings():
        return render_template('index.html')
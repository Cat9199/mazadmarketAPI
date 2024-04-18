from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
def admin_dashboard():
        return "Admin Dashboard"

@admin_bp.route('/settings')
def admin_settings():
        return "Admin Settings"
# Path: app/routes/auth.py
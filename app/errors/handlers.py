from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    """View function for error 404"""
    return render_template("404.html"), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """View function for error 500"""
    db.session.rollback()
    return render_template("500.html"), 500


@bp.app_errorhandler(413)
def too_large(error):
    return render_template("413.html"), 413

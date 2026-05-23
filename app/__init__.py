from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123' # need this for session to work

    # bootstrap = Bootstrap5(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from .auth import auth_login_bp
    from .auth import auth_register_bp
    from .home import home_bp
    from .listings import listings_bp
    from .bookmarks import bookmarks_bp
    from .details import details_bp

    app.register_blueprint(auth_login_bp, url_prefix = '/login')
    app.register_blueprint(auth_register_bp, url_prefix = '/auth/register')
    app.register_blueprint(listings_bp, url_prefix = '/listings')
    app.register_blueprint(bookmarks_bp, url_prefix = '/bookmarks')
    app.register_blueprint(details_bp, url_prefix = '/properties')
    app.register_blueprint(home_bp)

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("errors/404.html"),404

    @app.errorhandler(500)
    def internal_error(e):
      return render_template("errors/500.html"),500

    return app
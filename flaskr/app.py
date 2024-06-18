import os

from flask import Flask, render_template, Blueprint

STATIC_DIR = os.path.abspath('/media/khoa/Download/FrontEnd_URL_Shortener/flaskr/static')

app = Flask(__name__)

product_blueprint = Blueprint('products', __name__, template_folder='/templates', url_prefix='/products')
tools_blueprint = Blueprint('tools', __name__, template_folder='/templates', url_prefix='/tools')
password_blueprint = Blueprint('password', __name__, template_folder='/templates', url_prefix='/password')


@app.route('/')
def homepage():
    return render_template('index.html')


@product_blueprint.route('/link-management')
def link_management():
    return render_template('link_management.html')


@product_blueprint.route('/one-links')
def one_links():
    return render_template('OneLinks.html')


@tools_blueprint.route('/screenshot-website')
def screenshot_website():
    return render_template('screenshot.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/faq')
def faq():
    return render_template('frequently_asked_questions.html')


@app.route('/affiliates')
def affiliates():
    return render_template('affiliate.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('sign_up.html')


@password_blueprint.route('/reset')
def reset():
    return render_template('password_reset.html')


@app.route('/tools')
def tools():
    return render_template('tool.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

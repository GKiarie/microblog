Flask Web Frame Work
Configuration of a flask app - refers to the way the app is set up and organized, including its settings and parameters.

Config can be done in several ways, most common is to use a configuration file.
Configuration file - file that contains key value pairs of configuration settings.
The settings can include things like the database connection string, secret keys, debug mode and other application specific settings.

e.g.

# DEBUG = True
# SECRET_KEY = 'mysecrekey'
# DATABASE_URI = 'sqlite:///mydatabase.db'

to use in your flask application:
# app.config.from_pyfile('config.py')

another way to specify configuration options:
# Define variables as keya in app.config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

using a class to class to store confoguration variables:

-> import os

->class Config(object):
->	SECRET_KEY os.environ.get('SECRET_KEY') or 'you-will-never-guess'



import os 

class Config(object):
    # Using a system environment variable would be best practice here
    # If it's not set, then just use the SQLlite db in this directory
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'siip.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
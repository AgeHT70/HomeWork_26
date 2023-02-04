class Config:
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    # SQLALCHEMY_DATABASE_URI = "sqlite:///./movies.db"
    SQLALCHEMY_DATABASE_URI = \
        "postgresql://flask_app:Pv3tDf18@localhost/flask_app"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig:
    POSTGRESQL_USER = "chanyuyang"
    POSTGRESQL_PASS = ""
    POSTGRESQL_HOST = "127.0.0.1"
    POSTGRESQL_PORT = 5432
    DATABASE_NAME = "rent"
    SQLALCHEMY_DATABASE_URI = \
        "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
            POSTGRESQL_USER,
            POSTGRESQL_PASS,
            POSTGRESQL_HOST,
            POSTGRESQL_PORT,
            DATABASE_NAME,
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

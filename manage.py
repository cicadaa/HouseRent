from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from rentapp import create_app, config
from rentapp.model import db
from gevent.pywsgi import WSGIServer

from rentapp import model


app = create_app(config.LocalConfig)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver(port=8800, host='0.0.0.0'):
    http_server = WSGIServer((host, int(port)), app)
    http_server.serve_forever()


if __name__ == "__main__":
    manager.run()

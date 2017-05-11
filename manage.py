from flask_script import Manager
from flask_script import Server
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from app import create_app
from app import db
from app.models import *


app = create_app()

manager = Manager(app)
migrate    = Migrate(app, db)

manager.add_command("runserver", Server(host="127.0.0.1", port=8002))
manager.add_command('db', MigrateCommand)

@manager.command
def init_db():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()

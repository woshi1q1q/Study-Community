from flask_script import Manager
from app import app
from flask_migrate import Migrate,MigrateCommand
from app import db
from app.models import User,Post,Comment
manager = Manager(app)
# init  migrate upgrade
# 模型 -> 迁移文件 -> 表
# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db',MigrateCommand)

if __name__ =='__main__':
    manager.run()
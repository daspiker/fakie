from app import db

class SyslogSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serverIP = db.Column(db.String(64), index=True, unique=True)

class ApiSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workspaceId = db.Column(db.String(64), index=True, unique=True)
    workspaceKey = db.Column(db.String(128))

db.create_all()

'''
def init_db():
    db.create_all()
    # fill in initial data
    syslogsettings = SyslogSettings(serverIP="enter server IP or hostname")
    db.session.add(syslogsettings)
    apisettings = ApiSettings(workspaceId="enter log analytics workspace ID", workspaceKey="enter log analytics workspace Key")
    db.session.add(apisettings)
    db.session.commit()


if __name__ == '__main__':
    init_db()
'''
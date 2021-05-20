from app import db

class SyslogSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serverIP = db.Column(db.String(64), index=True, unique=True)

class ApiSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workspaceId = db.Column(db.String(64), index=True, unique=True)
    workspaceKey = db.Column(db.String(128))

db.create_all()
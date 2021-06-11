from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class video_text(db.Model):
    __tablename__ = 'hw_video_text'

    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, nullable=False)
    segment_number = db.Column(db.Integer, nullable=False)
    full_text = db.Column(db.Text, nullable=False)
    starttime = db.Column(db.Time , nullable=False)
    endtime = db.Column(db.Time , nullable=False)

    def __init__(self, id, video_id, segment_number, full_text, starttime, endtime):
        self.id = id
        self.video_id= video_id
        self.segment_number = segment_number
        self.full_text = full_text
        self.starttime = starttime
        self.endtime = endtime



    




    
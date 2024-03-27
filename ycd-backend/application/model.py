from config import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=True)
    channel_id = db.Column(db.String(100), nullable=True)
    channel_title = db.Column(db.String(100), nullable=True)
    published_at = db.Column(db.String(100), nullable=True)
    comments = db.relationship('Comment', backref='video', lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'video_id': self.video_id,
            'title': self.title,
            'channel_id': self.channel_id,
            'channel_title': self.channel_title,
            'published_at': self.published_at
        }
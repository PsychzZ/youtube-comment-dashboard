from flask import request, jsonify, make_response
from controller.comment_controller import CommentController
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ycd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

@app.route('/videos', methods=['POST'])
def create_video():
    try:
      video_id = request.args.get('v')
      comment_sentiments = CommentController.controller(video_id)
      
      return comment_sentiments
    except Exception as e:
        return make_response(jsonify({'message' : 'error getting Comments from the Video', 'error': str(e)}), 500)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
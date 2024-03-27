from flask import request, jsonify, make_response
from controller.comment_controller import CommentController
from config import app, db


@app.route('/videos', methods=['POST'])
def create_video():
    try:
      video_url = request.get_json()['videoUrl']
      comment_sentiments = CommentController.controller(video_url)
      return comment_sentiments
    except Exception as e:
        return make_response(jsonify({'message' : 'error getting Comments from the Video', 'error': str(e)}), 400)



with app.app_context():
    db.create_all()

app.run(debug=True)
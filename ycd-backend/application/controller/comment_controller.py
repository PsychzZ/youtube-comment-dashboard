import requests
from dotenv import load_dotenv
import os
from controller.analyse_comments import predict_comment

load_dotenv()
api_key = os.getenv("API_KEY")

class CommentController:
    #gets a videoId and gives back the comments of the youtube video as dictionary
    def get_comments(video_id):
        base_url = "https://www.googleapis.com/youtube/v3/commentThreads"
        params = {
            'key': api_key,
            'videoId': video_id,
            'part': "snippet",
            'maxResults': 100
        }

        all_comments = []

        while True:
            response = requests.get(base_url, params=params)
            data = response.json()

            all_comments.extend(data['items'])

            if 'nextPageToken' in data:
                params['pageToken'] = data['nextPageToken']
            else:
                break
        return all_comments
    
    #gets full comment dictionaary and clean it to have only the commentsTexts
    def clean_comments(comments:dict):
        key = "snippet"
        subkey1 = "topLevelComment"
        subkey2 = "snippet"
        final_key = "textOriginal"
        clean_comments = [item.get(key, {}).get(subkey1, []).get(subkey2, {}).get(final_key) for item in comments]
        return clean_comments
    
    def controller(videoUrl):
        test = videoUrl.split("v=")[1]
        video_id = test.split("&")[0]
        comments = CommentController.get_comments(video_id)
        return predict_comment(CommentController.clean_comments(comments))
        #print(CommentController.clean_comments(comments))


# zum Testen: Video = https://www.youtube.com/watch?v=8WZ-4JiwFIo
if __name__ == '__main__':
    CommentController.controller("8WZ-4JiwFIo")
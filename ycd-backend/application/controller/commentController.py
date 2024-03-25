import requests

class CommentController:
    #gets a videoId and gives back the comments of the youtube video as dictionary
    def get_comments(video_id):
        base_url = "https://www.googleapis.com/youtube/v3/commentThreads"
        params = {
            'key': "AIzaSyCSwEhTATLxgxwpti-WLy0-8ylt4onPizg",
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
    
    def controller(video_id):
        comments = CommentController.get_comments(video_id)
        print(CommentController.clean_comments(comments))


# zum Testen: Video = https://www.youtube.com/watch?v=Yxt_ieWY4LM
CommentController.controller("Yxt_ieWY4LM")
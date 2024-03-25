import googleapiclient.discovery



class CommentController:
    #gets a videoId and gives back the comments of the youtbe video in json format
    def get_comments(video_id):
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyCSwEhTATLxgxwpti-WLy0-8ylt4onPizg"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY
        )
        request = youtube.commentThreads().list(part="snippet", videoId=video_id)
        response = request.execute()

        return response
    
    def controller(video_id):
        comments_json = CommentController.get_comments(video_id)


print(CommentController.controller("Yxt_ieWY4LM"))
from TwitterTweetSentimentalAnalysis import Model
import getpass


class app(object):

    @staticmethod
    def run_app():
        try:
            candidate_key = getpass.getpass(prompt='enter your candidate Key : ')
            candidate_sec = getpass.getpass(prompt='enter your candidate secret Key : ')
            access_key = getpass.getpass(prompt='enter your access Key : ')
            access_sec = getpass.getpass(prompt='enter your access secret Key : ')

        except Exception as E:
            print('There is an Error : ', E)
        else:
            model_object = Model.model(candidate_key, candidate_sec, access_key, access_sec)
            print(model_object.get_authenticated_api())
            text = input(" Enter the tag you want to perform sentimental analysis on :  ")
            result = model_object.detailed_analysis_tweet_data(text)
            for i in result:
                print(i)


if __name__ == "__main__":
    object = app()
    object.run_app()

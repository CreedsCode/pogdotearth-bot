import cv2 as cv
import mediapipe as mp
import tweepy
import os
from dotenv import load_dotenv
import time 

load_dotenv()

API_KEY = os.getenv('twitter_api_key')
API_SECRET = os.getenv('twitter_api_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
TOKEN_SECRET = os.getenv('twitter_access_token_secret')

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hand_detector = mp_hands.Hands(
      static_image_mode=True,
      max_num_hands=8,
      min_tracking_confidence=0.15,
      min_detection_confidence=0.1
)

def hand_detection(image_file):
  print("Starting hand detection")
  image = cv.flip(cv.imread(image_file), 1)
  
  hsv_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  detection_result = hand_detector.process(hsv_image)
  
  if not detection_result.multi_hand_landmarks:
    return False

  return True

def grass_detection():
  print("Starting grass detection")

if __name__ == "__main__":
  



  twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)
  twitter_api = tweepy.API(twitter_oauth)

  try:
    print(twitter_api.verify_credentials())
    print("Successfully logged in")
  except tweepy.TweepError as e:
    print(e)
  except Exception as e:
    print(e)

  bot_id = int(twitter_api.verify_credentials().id_str)
  mention_id = 1
  mentions = twitter_api.mentions_timeline(since_id=mention_id)
  while True:
    for mention in mentions:
      print("mention tweet found!")
      mention_id = mention.id

      image_file = "images/tests/manuel/penis.png"

      contains_hand = hand_detection(image_file)
      
      if not contains_hand:
        print("no hand")
        continue
      
      surrounded_by_grass = grass_detection(image_file)

      if not surrounded_by_grass:
        print("no grass")
        continue

      try:
        print("retweeting")
        twitter_api.retweet(mention.id)
      except Exception as err:
        print(err)

    time.sleep(20)
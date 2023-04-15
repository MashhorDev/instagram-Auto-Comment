from instagrapi import Client
import time
import random

num = 0
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
cl = Client()
cl.login(USERNAME, PASSWORD)


# Comment Section add whatever comment you want

comments = [
  'Senpai !', "I'm a lovely bot", 'Nice post!', 'Keep up the great work!',
  'One Piece is the GOAT. ', ' CR7 Best Player .']

# Post link

media = cl.media_pk_from_url("https://www.instagram.com/p/Cq0rLUMIALw/")

# Comments Loop

while True:
  try:
    comment = random.choice(comments)
    coma = cl.media_comment(media, comment)
    num += 1
    print('Comment Number: ', num)
    time.sleep(60 * 15)
  except Exception as e:
    print('Comment Error ! :', e, ' Retrying in 1 Hour...')
    time.sleep(60 * 60)

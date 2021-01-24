# Created by Koutyan.S (https://kosukelab.com/)
# This is main program.

import pyperclip
import re
import nph_config
from twitter import Twitter, OAuth

# Text generation functions for each application.
def vox_app(original_text):
  try:
    pre_post_text = re.split(' - ', original_text, 1)
    created_text = "#NowPlaying " + pre_post_text[1] + " - " + pre_post_text[0]
    print("Nowplaying text generated!")
    return created_text
  except Exception as e:
    print("Error: Failed to generate text.")
    print(e)


# Auto tweet function.
def auto_tweet(post_text):
  try:
    t = Twitter(auth = OAuth(nph_config.ACCESS_TOKEN, nph_config.ACCESS_TOKEN_SECRET, nph_config.API_KEY, nph_config.API_SECRET))
    tweet_contents = t.statuses.update(status=post_text)
    print("Tweet success!")
    print(tweet_contents['user']['screen_name'])
    print(tweet_contents['text'])
  except Exception as e:
    print("Error: Failed to tweet.")
    print(e)


if __name__ == '__main__':
    original_text = pyperclip.paste().replace('\n', '')
    post_text = vox_app(original_text)  # Specify text generation function.
    pyperclip.copy(post_text)
    if nph_config.AUTO_TWEET == 1:
      auto_tweet(post_text)

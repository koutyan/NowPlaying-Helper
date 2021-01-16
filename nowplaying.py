# Created by Koutyan.S (https://kosukelab.com/)
# This is main program.

import pyperclip
import re

# Text generation functions for each application.
def vox_app(original_text):
  pre_post_text = re.split(' - ', original_text, 1)
  created_text = "#NowPlaying " + pre_post_text[1] + " - " + pre_post_text[0]
  return created_text


if __name__ == '__main__':
    original_text = pyperclip.paste().replace('\n', '')
    post_text = vox_app(original_text)
    pyperclip.copy(post_text)

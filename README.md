# NowPlaying Helper

Create nowplaying music text.

## Overview

Mac環境においてiTunes以外の楽曲再生ソフト(私の場合はVOX)で視聴した際に、NowPlaying投稿を楽に行う手段が現状ないため代替手段として作成。どのOSでも使用できる。

I created this as an alternative to the current lack of an easy way to post NowPlaying on Mac environment when listening songs with a software other than iTunes (VOX in my case). It can be used on any OS.

楽曲情報をクリップボードにコピーして本プログラムを実行すると、NowPlayingタグをつけて整形したテキストを生成し、クリップボードに保存する。これを貼り付けてツイートするなりFacebook投稿するなりすれば良い。

If you copy the song information to the clipboard and run this program, it will generate a formatted text with NowPlaying tag and save it to the clipboard. You can then paste it into a tweet or post it on Facebook.

v1.1からは、自動ツイート機能にも対応した。自身のアクセストークンを設定ファイルに記述すると、自動でツイートされるようになる。

From v1.1, the automatic tweeting function is also supported. If you enter your own access token in the configuration file, you will be able to tweet automatically.

現状、VOXに最適化した設計となっているが、状況に応じて対応ソフトを拡充予定。

Currently, it is designed to be optimized for VOX, but there are plans to expand the compatible software depending on the situation.

## Preparation

* Require Python 3.x
* Repuire pip
  * For Mac, install as follows (command execution results are omitted)
  
  ```(text)
  $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  
  $ python3 get-pip.py

  $ echo 'export PATH="$HOME/Library/Python/3.8/bin:$PATH"' >> ~/.bash_profile    # The version part should be changed to suit your personal environment.

  ### Restart Terminal.app

  $ pip -V
  ### If the version information of pip is displayed, it is OK.
  ```

* If use auto tweet function, edit `nph_config.py`

  ```(text)
  # Auto tweet setting. (enable = 1, disable = 0)
  AUTO_TWEET = 0

  # Enter your twitter token.
  ACCESS_TOKEN = ""
  ACCESS_TOKEN_SECRET = ""
  API_KEY = ""
  API_SECRET = ""
  ```

  * Obtain your own access token in advance.
  ![twitter_accesstoken](https://apps.kosukelab.com/images/nowplaying-helper/img00.png)

## How to use

* Execute the following command for **the first use only**.
  
  ```(texy)
  $ pip install -r requirements.txt
  ```

* Copy the song information, then run this program on Terminal.app

  ![copy_clipboard](https://apps.kosukelab.com/images/nowplaying-helper/img01.png)

  ```(text)
  $ python3 nowplaying.py
  ```

* The text will be saved to the clipboard and you can post it. If you enable auto tweet function, auto-tweeting is also confirmed. (Twitter user screen name and tweeted text are printed.)
  
  ![auto_tweet](https://apps.kosukelab.com/images/nowplaying-helper/img02.png)

# NowPlaying Helper

Create nowplaying music text.

## Overview

Mac環境においてiTunes以外の楽曲再生ソフト(私の場合はVOX)で視聴した際に、NowPlaying投稿を楽に行う手段が現状ないため代替手段として作成。どのOSでも使用できる。

I created this as an alternative to the current lack of an easy way to post NowPlaying on Mac environment when listening songs with a software other than iTunes (VOX in my case). It can be used on any OS.

楽曲情報をクリップボードにコピーして本プログラムを実行すると、NowPlayingタグをつけて整形したテキストを生成し、クリップボードに保存する。これを貼り付けてツイートするなりFaceｂook投稿するなりすれば良い。

If you copy the song information to the clipboard and run this program, it will generate a formatted text with NowPlaying tag and save it to the clipboard. You can then paste it into a tweet or post it on Facebook.

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

## How to use

* Execute the following command for the first use only.
  
  ```(texy)
  $ pip install -r requirements.txt
  ```

* Copy the song information, then run this program on Terminal.app
  
  ```(text)
  $ python3 nowplaying.py
  ```

* The text will be saved to the clipboard and you can post it.

## Donate

* Bitcoin (BTC) : `3DNbg5HHP5WMX9kNqpGZm3QP731cHxMqDs`
* Ethereum (ETH) : `0xb6E6260ed00044De7f5DC6cFbE6261d1c5fB37D2`
* Ripple (XRP) : `rLyDwmsfT7whYmENkh8kKQQc7eahZk1xPB`

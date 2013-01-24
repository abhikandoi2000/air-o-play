air-o-play
==========

Stream media files over WiFi for instant access.

dependencies
==========
  node
  node-static
  python >=2.7


Files Supported
==========

Video
  avi, mkv, mp4

Audio
  mp3, ogg, m4a

Images
  png", jpeg, gif, jpg


usage
==========

Clone the repo and change to air-o-play directory
  git clone https://github.com/abhikandoi2000/air-o-play.git
  cd air-o-play

Add your media files to the folder "media"
  
Use generatehtml.py file to generate html files
  python generatehtml.py

Start the app
  node app.js

Open the webpage ipaddress:8008 on your device using a modern browser(should support audio formats atleast) for instant media access

For Android
  Opera Mobile 12

Could not try on other devices

TODO
==========

rework on UX
test on multiple devices
add support for more formats
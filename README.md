# air-o-play

Stream media files over WiFi for instant access.

## Dependencies
* node (>=0.6.0)
*	node-static
*	python >=2.7


## Supported File Formats

### Video

	avi, mkv, mp4

### Audio

	mp3, ogg, m4a

### Images

	png, jpeg, gif, jpg


## Usage

### Clone

Clone the repo and change to air-o-play directory

	git clone https://github.com/abhikandoi2000/air-o-play.git
	cd air-o-play
	npm install

Add your media files to the folder `media`
  
Use generate.py file to generate html files

	python generate.py

Start the app

	node app.js

Open the webpage ipaddress:8080 on your device using a modern browser(should support audio formats atleast) for instant media access.

## Tested Devices

### Android

	Opera Mobile 12

Could not test on other devices since it was a hackathon.

## TODO

	* rework on UX
	* test on multiple devices
	* add support for more formats
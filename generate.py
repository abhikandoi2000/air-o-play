'''
	Hackathon(Syntax Error 2.0) - Air-o-Play html files generator
	Usage : python generate.py
	Created : Jan 19 10:00PM - Jan 20 10:00AM 2013
'''
import os
#import argparse

from flask import Flask

#configuration
BASEPATH = "media"
SITE_NAME = "Air-o-Play"


#commented coz I droped the idea of generating seperate pages for video, audio and images
#media type for which to generate html pages
'''
parser = argparse.ArgumentParser(description="Generate HTML files for media folders")
parser.add_argument('mediatype')
args = parser.parse_args()
mediatype = args.mediatype

if mediatype == "video":
	exts = [".avi", ".mkv"]
elif mediatype == "audio":
	exts = [".mp3", ".ogg"]
elif mediatype == "image":
	exts = [".png", ".jpeg", ".gif", ".jpg"]
else:
	print "no such media type, pick b/w video, audio and image"
'''

exts_video = [".avi", ".mkv", ".mp4"]
exts_audio = [".mp3", ".ogg", ".m4a"]
exts_image = [".png", ".jpeg", ".gif", ".jpg"]
exts = exts_video + exts_audio + exts_image

'''
def contains_media(path, mediatype):
	#whether or not the folder contains any file having mediatype data
	media = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and os.path.splitext(file)[1] in exts ]
	if media.length > 0:
		return true
	return false
'''

#return a link to the folder
def link_folder(folder):
	html = '<div class="folder">'
	html = html + '<a href="' + folder + '/index.html">'
	html = html + str.capitalize(folder)
	html = html + '</a>'
	html = html + '</div>'
	return html


def gen_html(path):
	#seperate current directory from the rest of the path
	rest, curr = os.path.split(path)

	#generate a list of folders containing same type of data
	folders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder)) ]
	print folders

	#start generating the html content
	html = '<!DOCTYPE html>\n'
	html = html + '<html>\n'
	base_path = os.path.relpath(BASEPATH, path)
	html = html + '<head><title>' + str.capitalize(curr) + ' - ' + SITE_NAME + '</title><link rel="stylesheet" href="' + base_path + '/style.css' + '" type="text/css" /><script src="' + base_path + '/resize.js' + '"></script></head>'
	html = html + '<body>'
	html = html + '<!-- header starts  --><div id="header-wrapper"><div id="header"><h1 class="logo"><a href="' + base_path + '/index.html' + '" title="' + SITE_NAME + '">' + SITE_NAME + '</a></h1><div class="caption">Airing the fun.</div></div></div><!-- header ends -->'
	html = html + '<div id="content-wrapper"><div id="content">'

	#create folder list for each folder found containing data of same type
	for folder in folders:
		html = html + link_folder(folder)
		gen_html(os.path.join(path, folder))

	#generate a list of all the media files present in that folder
	media = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and os.path.splitext(file)[1] in exts ]
	print "Media:",media

	if len(media) == 0 and len(folders) == 0:
		#no media files found in that folder
		html = html + "<div>No media content found.</div>"
	else:
		#generate html content for each media item found
		for file in media:
			extension = os.path.splitext(file)[1]
			if extension in exts_video:
				mediatype = "video"
			elif extension in exts_audio:
				mediatype = "audio"
			elif extension in exts_image:
				mediatype = "image"
			html = html + gen_media(os.path.join(path, file), mediatype)

	html = html + '</div></div>'
	html = html + '<div id="footer-wrapper"><div id="footer">Crafted with a love for media</div></div>'
	html = html + '</body></html>'
	print "Opening file"

	#generate filename to open the file
	filename = path + "/" + "index.html"
	print filename
	file = open(filename, 'w')
	file.write(html)
	print html
	file.close()
	print "Closing file"


def gen_media(path, type):
	rest, file = os.path.split(path)
	print "complete path:", path
	html = '<div class="' + type + '">'
	ext = os.path.splitext(file)[1]
	if type == "video":		
		#extract video frame for preview
		'''
		stream = pyffmpeg.VideoStream()
		stream.open('myvideo.avi')
		image = stream.GetFrameNo(0)
		image.save(os.path.splitext(file)[0] + '.png')
		'''

		#html = html + '<span class="filename"><a href="' + file + '">'
		html = html + '<a href="' + file + '">'
		html = html + file
		#html = html + '</a></span>'
		html = html + '</a>'
		mimetype = "unknown"
		if ext == ".mkv":
			mimetype = "x-matroska"
		elif ext == ".avi":
			mimetype = "x-msvideo"
		
		html = html + '<video style="display:none;" controls autoplay>'
		html = html + '<source src="' + file + '" type="video/' + mimetype + '">'
		#html = html + '<title '
		html = html + '</video>'
		#html = html + '<output style="display:none;"></output>'
		html = html + ''
	elif type == "audio":
		html = html + '<span class="filename">' + file + '</span><br>'
		html = html + '<audio controls>'
		mimetype = "unknown"
		if ext == ".mp3":
			mimetype = "mp3"
		elif ext == ".ogg":
			mimetype = "ogg"
		html = html + '<source src="' + file + '" type="audio/' + mimetype + '">'
		html = html + 'Sorry but the <code>audio</code> element is not supported in your browser.'
		html = html + '</audio>'
	elif type == "image":
		html = html + '<span class="filename">' + file + '</span><br><img src="' + file + '" alt="' + os.path.splitext(file)[0] + '" />'
	html = html + '</div>'
	print html
	return html


#
folders = [folder for folder in os.listdir(BASEPATH) if os.path.isdir(os.path.join(BASEPATH, folder)) ]

print folders

gen_html(BASEPATH)

for folder in folders:
	gen_html(os.path.join(BASEPATH, folder))
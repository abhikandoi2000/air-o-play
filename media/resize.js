/*
 * Air-o-Play
 * Syntax Error 2.0
 * TODO : Extract Sample Images from Video Files
*/

window.onload = function() {
	/* tried to extract sample image from videos, didn't work for the initial trial
	var videos = document.getElementsByTagName('video');
	var output = document.getElementsByTagName('output');
	for(i = 0; i < videos.length; ++i) {
		var canvas = document.createElement('canvas');
		var w = videos[i].width;
		var h = videos[i].height;
		canvas.width = w;
		canvas.height = h;
		//videos[i].style.display = "none";
		var ctx = canvas.getContext('2d');
		ctx.drawImage(videos[i], 0, 0, w, h);
		output[i].appendChild(canvas);
	}
	*/

	images = document.images;
	for(i = 0; i < images.length; ++i) {
		width = images[i].width;
		height = images[i].height;
		ratio = height/width;
		if (width > 400) {
			width = 400;
			height = ratio * width;
		}
		images[i].width = width;
		images[i].height = height;
	}
	
}
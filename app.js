/*
  Syntax Error 2.0
  node-static backend
*/
var nodestatic = require('node-static');
var http = require('http');

var server = new (nodestatic.Server)('./media');

var httpServer = http.createServer(function(req, res){
	req.addListener('end', function(){
		server.serve(req, res);
	} ).resume();
});

httpServer.listen(8080);
console.log("Airing on port number 8080. Stream through!");

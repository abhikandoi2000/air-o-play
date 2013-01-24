/*
  Syntax Error 2.0
  node-static backend
*/
var static = require('node-static');
var http = require('http')

var server = new (static.Server)('media');

var httpServer = http.createServer(function(req, res){
	req.addListener('end', function(){
		server.serve(req, res);
	} );
});

httpServer.listen(8008);
console.log("Airing at ipaddress:8008, stream through.");

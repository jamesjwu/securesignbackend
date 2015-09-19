var express = require('express');
var path = require('path');
var logger = require('morgan');
var fs = require('fs');
var routes = require('./routes/index');

var app = express();
// Socket IO for broadcasting update
var server = require('http').Server(app);

var mongo = require('mongoskin');
var db = mongo.db("mongodb://root:15122@proximus.modulusmongo.net:27017/aranut7I", {native_parser:true});



server.listen(process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');


app.use('/', routes);


module.exports = app;

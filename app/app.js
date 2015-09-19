var express = require('express');
var path = require('path');
var logger = require('morgan');
var fs = require('fs');
var routes = require('./routes/index');

var app = express();
// Socket IO for broadcasting update
var server = require('http').Server(app);

server.listen(process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');


app.use('/', routes);


module.exports = app;

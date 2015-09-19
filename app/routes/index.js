'use strict';

var express = require('express');

var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  scriptPath: './python',
};


var router = express.Router();

router.get('/', function (req, res) {
	PythonShell.run('trainer.py', options, function (err, results) {
    if (err) console.log(err);
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
    });
    res.render("index", {title:"asldijaslidj"});
});


router.post('/api/predict', function(req, res) {
    var id = req.body.personID;
    var url = req.body.imageURL;
    
});
module.exports=router;

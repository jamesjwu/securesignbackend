'use strict';

var express = require('express');

var PythonShell = require('python-shell');




var router = express.Router();

router.get('/', function (req, res) {
    var options = {
    mode: 'text',
    scriptPath: './python',
    pythonOptions: ['-u'],
    args: ['--userid '+req.body.personID, "--imgurl "+req.body.imageURL],
    };
    PythonShell.run('train_models.py', options, function (err, results) {
    if (err) console.log(err);
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
      var options_add = {
        mode: 'text',
        scriptPath: './python',
        pythonOptions: ['-u'],
        args: ['--userid '+req.body.personID, "--imgurl "+req.body.imageURL, "--add", "--is_pos"],
        };
        PythonShell.run('train_models.py', options_add, function (err, results) {
            if (err) console.log(err);
            console.log('image added to training set');
        });
    });
    res.render("index", {title:"asldijaslidj"});
});


router.post('/api/predict', function(req, res) {
    var id = req.body.personID;
    var url = req.body.imageURL;
    
});
module.exports=router;

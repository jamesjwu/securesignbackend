var express = require('express');
'use strict';

var router = express.Router();

router.get('/', function (req, res) {
	var id = req.body.personID;
	var url = req.body.imageURL;
	var isAuthenticated = test(id, url); 
    res.send(isAuthenticated.toString());
});

module.exports=router;

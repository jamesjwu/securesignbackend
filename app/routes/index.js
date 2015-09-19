var express = require('express');
var router = express.Router();
var mongo = require('mongoskin');
var db = mongo.db("mongodb://aiiyoh:aiiyoh@apollo.modulusmongo.net:27017/ozE6nori", {native_parser:true});


router.get('/', function (req, res) {
    res.render('index', {title: 'SecureSign', body:''});
    console.log(db.collection('userlist').find());
});

module.exports=router;

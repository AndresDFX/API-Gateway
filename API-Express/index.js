

var express = require('express') 
var bodyParser = require('body-parser')
var app = express() 
var router = express.Router()    
var port = process.env.PORT || 5003 
var axios = require('axios');
//var { test, getAllRandoms } = require('./functions.js');

//Use libraries
app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())   
app.use('/api', router)

//Routes
router.get('/', async(req, res) => {
    let response = await axios.get('https://randomuser.me/api/');
    let data = response.data;
    res.json(data);
})

router.get('/:nombre', function(req, res) {
    res.json({ mensaje: '¡Hola' + req.params.nombre });    
})

router.post('/', function(req,res) { 
    res.json({mensaje: req.body.name});
})


//Start server
app.listen(port)
console.log('API escuchando en el puerto ' + port)
var express = require('express'); 
var app = express(); 
  

app.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 
  
app.get('/takeoff', callName); 
  
function callName(req, res) { 
  
    var spawn = require("child_process").spawn; 
    var process = spawn('python3',["./takeoff_and_land.py", 
                           ] ); 
     process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
} 

app.get('/mission', callName); 
  
function callName(req, res) { 
  
    var spawn = require("child_process").spawn; 
    var process = spawn('python3',["./mission.py", 
                           ] ); 
     process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
} 
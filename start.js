var express = require('express'); 
var app = express(); 
  

app.listen(3400, function() { 
    console.log('server running on port 3000'); 
    
} ) 
  

  let i =1;
  callName();

function callName() { 
  
    var spawn = require("child_process").spawn; 
    var process = spawn('python3',["./getparam.py", ] ); 
     process.stdout.on('data', function(data) { 
        //  res.writeHead(200,{'Content-Type': 'application/json'});
        //  jsonStr = JSON.stringify(data) + '\n'
        //  jsonStr.toStream().pipe(res)

        //  res.send(data.toString()); 
        
        console.log(i + " "+ data)
        i++
    } ) 
} 


// app.get('/gimbal', callName); 
  
// function callName(req, res) { 
  
//     var spawn = require("child_process").spawn; 
//     var process = spawn('python3',["./gimbal.py", 
//                            ] ); 
//      process.stdout.on('data', function(data) { 
//         res.send(data.toString()); 
//     } ) 
// } 


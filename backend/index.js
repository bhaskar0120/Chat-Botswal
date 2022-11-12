const express = require('express');
const app = express();
const bodyParser = require('body-parser');

const PORT = 6969;
const jsonParser = bodyParser.json()


app.listen(PORT, ()=>{
    console.log(`Listening to port ${PORT}`);
});

app.post('/text', jsonParser, (req,res)=>{
  console.log(req.body);
  res.send(req.body.data)
});

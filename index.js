const express = require('express')
const app = express()
const mysql = require('mysql2/promise');
const cors = require('cors')
const port = 3300
const bluebird = require('bluebird');

app.use(cors())
// respond with "hello world" when a GET request is made to the homepage
app.get('/', async function (req, res) {
  const connection = await mysql.createConnection({host:'localhost', user: 'root', database: 'fask', Promise: bluebird})
  const { limit, offset, type } = req.query
  if(limit && offset && type){
    const [rows, fields] = await connection.execute(`SELECT * FROM ${type} limit ${limit} offset ${offset}`);
    res.send(rows)
  }else{
    res.status(404).send()
  }
  connection.end()
})


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

0
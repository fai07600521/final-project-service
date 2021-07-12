const express = require('express')
const app = express()
const mysql = require('mysql2/promise');
const cors = require('cors')
const config = require('./config')
const port = 3000
const bluebird = require('bluebird');

app.use(cors())
// respond with "hello world" when a GET request is made to the homepage
app.get('/', async function (req, res) {
  try{
    const connection = await mysql.createConnection({
      host: config.mysql.host, 
      user: config.mysql.user, 
      password: config.mysql.password,
      database: config.mysql.database, 
      port: config.mysql.port,
      Promise: bluebird
    })
    const { limit, offset, type } = req.query
    if(limit && offset && type){
      const [rows, fields] = await connection.execute(`SELECT * FROM ${type} limit ${limit} offset ${offset}`)
      connection.end()
      res.send(rows)
    }else{
      res.status(404).send()
    }
  }catch(e){
    console.log(err.message)
    res.status(404).send()
  }
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

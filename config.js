const environment = process.env.NODE_ENV

let config = {}

if(environment === "prod"){
  config = {
    mysql: {
      host:'103.74.253.121', 
      user: 'root',
      port: 3306,
      password: '123456',
      database: 'fask'
    }
  }
}else{
  config = {
    mysql: {
      host:'localhost', 
      user: 'root', 
      database: 'fask'
    }
  }
}

module.exports = {
  ...config
}
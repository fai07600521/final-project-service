

const express = require('express')
const app = express()
const mysql = require('mysql2/promise');
const cors = require('cors')
const config = require('./config')
const port = 3000
const bluebird = require('bluebird');
var torchjs = require('@idn/torchjs');
var script_module = new torchjs.ScriptModule('resnet18.pt');
var tensor = torchjs.ones([1, 3, 224, 224], false);

const { performance } = require('perf_hooks');

// Comment this out if you don't have cuda
script_module.cuda();
let start, end;
start = performance.now();
let otensor = script_module.forward(tensor);
end = performance.now();
console.log(`      gpu: ${end - start} ms`);
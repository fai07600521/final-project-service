const spawn = require("child_process").spawn;

const pythonProcess = spawn('python', ["generate.py"])
pythonProcess.stdout.on('data', (data) => {
  console.log(data.toString());
});
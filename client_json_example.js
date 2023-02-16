// Client example -- Node.js
// Based on Node.js client example in ZeroMQ get started guide
const zmq = require('zeromq');
const reqMsg = "";

async function runClient() {
    const clientSock = new zmq.Request();
    console.log('Connecting to server...');
    await clientSock.connect('tcp://localhost:5555');

    console.log(`Sending data: ${reqMsg}`);
    await clientSock.send(reqMsg);
    const receivedData = await clientSock.receive();
    const receivedJson = JSON.parse(receivedData);
    console.log(`Your list of numbers is ${receivedData}`); // Shows the array structure
    console.log(receivedJson[1]); // After JSON.parse, you can index into the array
}

runClient();
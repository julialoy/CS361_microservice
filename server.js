// Server for microservice
const zmq = require('zeromq');

const PORT = 5555   //Change this value if a different port number is desired

/*
* Generates and returns 3 pseudorandom integers between 1 and 500 (inclusive)
* Based on examples from MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
* params: none
* returns: array of 3 pseudorandom integers
*/
const generateRandomNums = () => {
    let numArray = [];
    while (numArray.length < 3) {
        let candidateNum = parseInt(Math.random() * (501 - 1) + 1);
        if (!numArray.includes(candidateNum)) {
            numArray.push(candidateNum);
        }
    }

    return numArray;
}

/*
* Opens a socket on the specified port, listens for connections, and upon request
* sends client an array of 3 pseudorandom numbers as a JSON object.
* Based on example server code from ZeroMQ docs: https://zeromq.org/get-started/?language=nodejs#
* params: none
* returns: none
*/
const runServer = async () => {
    const servSock = new zmq.Reply();
    await servSock.bind(`tcp://*:${PORT}`);
    console.log(`Listening for connections on port ${PORT}...`);

    for await (const [msg] of servSock) {
        console.log(`Received request: ${msg.toString()}`);

        if (msg.toString().toLowerCase() === 'q') {
            await servSock.send(JSON.stringify("Terminating connection."));
            console.log(`\nTerminating connection on client request.`);
            break;
        }

        const servData = generateRandomNums();
        await servSock.send(JSON.stringify(servData));
        console.log(`Sent data: ${servData}`);
    }

    console.log("All connections closed. Server shutting down. Goodbye.");
}

runServer();